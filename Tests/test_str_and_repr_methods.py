from datetime import datetime
from assistant import Birthday, Name, Phone, Record


def test():
    print('Test of str and repr methods of classes Name, Phone, Birthday and Record .....', end=' ')
    birth_date = datetime(year=1996, month=10, day=15, hour=2, minute=34)
    birth = Birthday(birth_date)
    name = Name('Vasya')
    phone_number = Phone('+38 (096) 700-80-90')
    rec = Record(name, birthday=birth, phone=phone_number)
    another_phone = Phone(45632376335)
    rec.add_phone(another_phone)
    assert str(name) == 'Name: Vasya'
    assert repr(name) == 'Name(Vasya)'
    assert str(phone_number) == 'Phone: 380967008090'
    assert repr(phone_number) == 'Phone(\'380967008090\')'
    assert str(another_phone) == 'Phone: 45632376335'
    assert repr(another_phone) == 'Phone(\'45632376335\')'
    assert str(birth) == '15.10.1996'
    assert repr(birth) == 'Birthday(datetime.datetime(1996, 10, 15, 2, 34))'
    assert str(rec) == 'Vasya               |  15.10.1996  |  380967008090, 45632376335'
    assert repr(rec) == "Record(Name(Vasya), [Phone('380967008090'), Phone('45632376335')], Birthday(datetime.datetime(1996, 10, 15, 2, 34))"
    print(' passed')


if __name__ == '__main__':
    test()
