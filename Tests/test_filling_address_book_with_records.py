from random import randint, choice
from string import ascii_lowercase, digits
from datetime import datetime
from assistant import AddressBook, Birthday, Name, Phone, Record


def test():
    my_address_book = AddressBook()

    number_or_records = randint(40, 60)
    for _ in range(number_or_records):
        name_str = ''.join(choice(ascii_lowercase) for _ in range(randint(3, 18))).title()
        name = Name(name_str)

        birth = None
        if choice([1, 1, 1, 0, 1, 1, 1, 0, 0, 1]):
            birth_date = datetime(year=randint(1900, 2022),
                                  month=randint(1, 12),
                                  day=randint(1, 28),
                                  hour=randint(0, 23),
                                  minute=randint(0, 59))
            birth = Birthday(birth_date)

        rec = Record(name, birthday=birth)
        my_address_book.add_record(rec)

    records = list(my_address_book.data.values())
    for _ in range(number_or_records * 3 // 2):

        phone_str = ''.join(choice(digits) for _ in range(randint(7, 12)))
        phone_number = Phone(phone_str)

        choice(records).add_phone(phone_number)

    print(my_address_book)
    print('Random filling of AdressBook complete!')

    while True:
        try:
            num = input('Enter the number N of records to show at each time: ')
            my_address_book.number_records_return = int(num)
            break
        except ValueError:
            print('Enter correct number: ')

    for part in my_address_book:
        input(f"Press Enter to show next {my_address_book.number_records_return} records: ")
        for obj in part:
            print(repr(obj))


if __name__ == '__main__':
    test()
