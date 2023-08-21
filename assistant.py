from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.value = value


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)

    def change_value(self, new_value):
        self.value = new_value


class Record:
    def __init__(self, name: Name, phone=None):
        self.name = name
        self.phones = list()
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone: Phone) -> None:
        self.phones.append(phone)

    def delete_phone(self, phone: Phone) -> None:
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise ValueError(f'{self.name} does not have such phone number {phone.value}')

    def delete_all_phones(self) -> None:
        self.phones.clear()

    def change_phone(self, phone: Phone, new_value: str) -> None:
        phone.change_value(new_value)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
