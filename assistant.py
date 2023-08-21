from collections import UserDict
from datetime import datetime, date


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __repr__(self):
        return f'Field({repr(self.value)})'

    def __str__(self):
        return f'This is Field with value: {self.value}'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f'Name({self.value})'

    def __str__(self):
        return f'Name: {self.value}'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, name: str):
        if type(name) is not str:
            raise TypeError('Name must be string')
        if len(name) < 2:
            raise ValueError('Name is too short. Must be minimum 3 characters')
        if not name.isalnum():
            raise ValueError('Name contains not allowed signs')
        self.__value = name


class Phone(Field):
    def __init__(self, phone: str):
        super().__init__(phone)

    def __repr__(self):
        return f'Phone({repr(self.value)})'

    def __str__(self):
        return f'Phone: {self.value}'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, phone: str | int):
        phone = str(phone)
        phone = self._sanitize_phone_number(phone)
        if len(phone) < 7:
            raise ValueError('Phone is too short. Must be minimum 7 digits')
        if not phone.isdigit():
            raise ValueError('Phone contains not allowed signs')
        self.__value = phone

    def _sanitize_phone_number(self, phone: str):
        new_phone = (
            phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )
        return new_phone


class Birthday(Field):
    def __init__(self, birthday: datetime):
        super().__init__(birthday)

    def __repr__(self):
        return f'Birthday({repr(self.value)})'

    def __str__(self):
        return f'{self.value.strftime("%d.%m.%Y")}'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, birthday: datetime):
        if type(birthday) is not datetime:
            raise TypeError('Birthday must be date object')
        curr_datetime = datetime.now()
        if birthday > curr_datetime:
            raise ValueError('Birthday cannot be the date after today')
        if curr_datetime.year - birthday.year > 150:
            raise ValueError('Person cannot be such old')
        self.__value = birthday


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        self.__name = None
        self.__birthday = None
        self.name = name
        self.birthday = birthday

        self.phones = list()
        if phone and type(phone) is Phone:
            self.phones.append(phone)

    def __repr__(self):
        return f'Record({repr(self.name)}, {self.phones}, {repr(self.birthday)}'

    def __str__(self):
        return (f'{self.name.value:<20}|  '
                f'{str(self.birthday) if self.birthday else "":<12}|  ' +
                ', '.join(phone.value for phone in self.phones))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: Name):
        if self.__name is not None:
            raise AttributeError('Name already setted')
        if type(new_name) is not Name:
            raise TypeError('Wrong type of given name')
        self.__name = new_name

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birth: Birthday):
        if type(birth) is Birthday:
            self.__birthday = birth

    def add_phone(self, phone: Phone) -> None:
        self.phones.append(phone)

    def change_phone(self, phone: Phone, new_value: str) -> None:
        phone.value = new_value

    def delete_phone(self, phone: Phone) -> None:
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise ValueError(f'{self.name} does not have such phone number {phone.value}')

    def delete_all_phones(self) -> None:
        self.phones.clear()

    def days_to_birthday(self) -> int | None:
        if not self.birthday:
            return None
        curr_date = datetime.now().date()
        curr_year = curr_date.year
        birthday_in_curr_year = self.birthday.value.date().replace(year=curr_year)
        if curr_date <= birthday_in_curr_year:
            delta = birthday_in_curr_year - curr_date
            return delta.days
        birthday_in_next_year = birthday_in_curr_year.replace(year=curr_year + 1)
        delta = birthday_in_next_year - curr_date
        return delta.days


class AddressBook(UserDict):

    def __init__(self, number_records_return=1):
        super().__init__()
        self.number_records_return = number_records_return
        self.__counter = 0

    def __iter__(self):
        self.__counter = 0
        # uncomment proper line
        self.records = self.__get_lines()  # when needed list of string representations of N records
        # self.records = list(self.data.values())  #when needed list of N Record objects
        return self

    def __next__(self):
        if self.__counter >= len(self.records):
            raise StopIteration
        start = self.__counter
        self.__counter += self.number_records_return
        return self.records[start:self.__counter]

    def __repr__(self):
        return f'AddressBook({repr(self.data)})'

    def __str__(self):
        h_line = '-----|--------------------|--------------|------------------------------------------\n'
        res = [h_line, '  #  |        Name        |   Birthday   |  Phones\n', h_line]
        res.extend(self.__get_lines())
        res.append(h_line)
        return ''.join(res)

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def __get_lines(self) -> list[str]:
        i, lines = 1, []
        for name in sorted(self.data.keys()):
            lines.append(f'{i:>4} |' + str(self.data[name]) + '\n')
            i += 1
        return lines


if __name__ == '__main__':
    # ALL THE TESTS ARE IN SEPARATE FILES
    from Tests.test import test as test1
    from Tests.test_days_to_birthday import test as test2
    from Tests.test_str_and_repr_methods import test as test3
    from Tests.test_filling_address_book_with_records import test as test4

    test4()
    test1()
    test2()
    test3()
