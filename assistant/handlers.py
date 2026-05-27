from .contacts import AddressBook, Record
# TODO: Імпортувати Note, Notebook після реалізації notes.py
# from .notes import Note, Notebook


# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return str(error)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
    return inner


# --- Команди для контактів ---

@input_error
def add_contact(args, book):
    name, phone = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    return "; ".join(phone.value for phone in record.phones)


@input_error
def show_all(book):
    if not book.data:
        return "No contacts saved."
    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    if record.birthday is None:
        return "Birthday not found."
    return record.birthday.value.strftime("%d.%m.%Y")


@input_error
def birthdays(args, book):
    # Отримуємо кількість днів з аргументів, або 7 за замовчуванням
    days = int(args[0]) if args else 7
    upcoming = book.get_upcoming_birthdays(days)
    if not upcoming:
        return "No upcoming birthdays."
    return "\n".join(
        f"{item['name']} -> {item['congratulation_date']}"
        for item in upcoming
    )


# TODO: Додати команди для email та address:
# add_email, add_address, edit_email

# TODO: Додати команди для пошуку контактів:
# search_contacts(args, book)

# TODO: Додати команди для видалення контакту:
# delete_contact(args, book)


# --- Команди для нотаток ---
# TODO: Реалізувати після notes.py

# def add_note(args, book, notebook): ...
# def edit_note(args, book, notebook): ...
# def delete_note(args, book, notebook): ...
# def show_note(args, book, notebook): ...
# def show_all_notes(args, book, notebook): ...
# def search_notes(args, book, notebook): ...
# def add_tag(args, book, notebook): ...
# def remove_tag(args, book, notebook): ...
# def search_notes_by_tag(args, book, notebook): ...
# def sort_notes(args, book, notebook): ...
