import re
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
        # Нормалізація: прибираємо пробіли, дефіси, дужки та префікс +380/380
        normalized = value.strip().replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        if normalized.startswith("+380"):
            normalized = "0" + normalized[4:]
        elif normalized.startswith("380"):
            normalized = "0" + normalized[3:]

        if not normalized.isdigit() or len(normalized) != 10:
            raise ValueError(
                "Invalid phone number. Use 10 digits (e.g. 0991234567) "
                "or formats like +380991234567 / 380991234567."
            )
        super().__init__(normalized)


class Email(Field):

    def __init__(self, value):
        # Перевірка стандартного формату email: local@domain.tld
        if not re.fullmatch(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", value
        ):
            raise ValueError(
                "Invalid email format (expected user@example.com)"
            )
        super().__init__(value)


class Address(Field):
    pass


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
        self.email = None
        self.address = None

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

    def add_email(self, email_address):
        self.email = Email(email_address)

    def add_address(self, physical_address):
        self.address = Address(physical_address)

    def __str__(self):
        phones = "; ".join(phone.value for phone in self.phones)
        birthday = ""
        if self.birthday:
            birthday = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}"
        email = f", email: {self.email.value}" if self.email else ""
        address = f", address: {self.address.value}" if self.address else ""

        return (
            f"Contact name: {self.name.value}, "
            f"phones: {phones}{email}{address}{birthday}"
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
        else:
            raise KeyError(f"Contact '{name}' not found")

    def search(self, query):
        query = query.lower()
        results = []

        for record in self.data.values():
            # Перевіряємо збіг в імені
            in_name = query in record.name.value.lower()
            # Перевіряємо збіг у телефонах
            in_phones = any(query in phone.value for phone in record.phones)
            # Перевіряємо збіг в email
            in_email = (
                record.email and query in record.email.value.lower()
            ) or False
            # Перевіряємо збіг в адресі
            in_address = (
                record.address and query in record.address.value.lower()
            ) or False

            if in_name or in_phones or in_email or in_address:
                results.append(record)

        return results

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
