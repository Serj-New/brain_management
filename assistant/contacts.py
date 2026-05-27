from collections import UserDict
from datetime import datetime, timedelta, date


# Базовий клас для всіх полів
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# Клас для імені контакту
class Name(Field):
    pass


# Клас для номера телефону
class Phone(Field):

    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)


# TODO: Додати клас Email з валідацією (наприклад, через регулярний вираз)
# class Email(Field):
#     pass


# TODO: Додати клас Address
# class Address(Field):
#     pass


# Клас для дня народження
class Birthday(Field):

    def __init__(self, value):
        try:
            birthday_date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(birthday_date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


# Клас одного контакту
class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        # TODO: Додати поля self.email та self.address

    # Додавання телефону
    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    # Видалення телефону
    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return
        raise ValueError("Phone number not found")

    # Редагування телефону
    def edit_phone(self, old_number, new_number):
        phone = self.find_phone(old_number)
        if phone:
            new_phone = Phone(new_number)
            phone.value = new_phone.value
        else:
            raise ValueError("Phone number not found")

    # Пошук телефону
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    # Додавання дня народження
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    # TODO: Додати методи add_email, add_address

    def __str__(self):
        phones = "; ".join(phone.value for phone in self.phones)
        birthday = ""
        if self.birthday:
            birthday = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}"
        # TODO: Додати email та address у рядок виводу
        return (
            f"Contact name: {self.name.value}, "
            f"phones: {phones}{birthday}"
        )


# Клас адресної книги
class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    # TODO: Додати метод search(query) — пошук за ім'ям, телефоном, email тощо

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = datetime.today().date()
        end_date = today + timedelta(days=days)

        for record in self.data.values():
            if not record.birthday:
                continue

            birthday = record.birthday.value
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            if today <= birthday_this_year <= end_date:
                if birthday_this_year.weekday() >= 5:
                    days_to_monday = 7 - birthday_this_year.weekday()
                    congratulation_date = birthday_this_year + timedelta(days=days_to_monday)
                else:
                    congratulation_date = birthday_this_year

                upcoming_birthdays.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })

        return upcoming_birthdays
