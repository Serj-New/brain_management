from .contacts import AddressBook, Record
from .notes import Note, Notebook

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return str(error)
        except KeyError as error:
            return str(error) if str(error) != "" else "Not found."
        except IndexError:
            return "Enter the argument for the command."
    return inner

# Контакти

@input_error
def add_contact(args, book: AddressBook, _notebook=None):
    if len(args) < 2:
        raise IndexError
    name, phone = args[0], args[1]
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
def change_contact(args, book: AddressBook, _notebook=None):
    if len(args) < 3:
        raise IndexError
    name, old_phone, new_phone = args[0], args[1], args[2]
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def delete_contact(args, book: AddressBook, _notebook=None):
    if not args:
        raise IndexError
    name = args[0]
    book.delete(name)
    return f"Contact '{name}' deleted."


@input_error
def show_phone(args, book: AddressBook, _notebook=None):
    if not args:
        raise IndexError
    record = book.find(args[0])
    if record is None:
        raise KeyError("Contact not found.")
    if not record.phones:
        return "No phones saved for this contact."
    return "; ".join(phone.value for phone in record.phones)


@input_error
def show_all(args, book: AddressBook, _notebook=None):
    if not book.data:
        return "No contacts saved."
    return "\n".join(str(record) for record in book.data.values())


@input_error
def search_contacts(args, book: AddressBook, _notebook=None):
    if not args:
        raise IndexError
    query = " ".join(args)
    results = book.search(query)
    if not results:
        return "No contacts found."
    return "\n".join(str(r) for r in results)


@input_error
def add_email(args, book: AddressBook, _notebook=None):
    if len(args) < 2:
        raise IndexError
    name, email = args[0], args[1]
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    record.add_email(email)
    return "Email added."


@input_error
def add_address(args, book: AddressBook, _notebook=None):
    if len(args) < 2:
        raise IndexError
    name = args[0]
    address = " ".join(args[1:])
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    record.add_address(address)
    return "Address added."


@input_error
def add_birthday(args, book: AddressBook, _notebook=None):
    if len(args) < 2:
        raise IndexError
    name, birthday = args[0], args[1]
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args, book: AddressBook, _notebook=None):
    if not args:
        raise IndexError
    record = book.find(args[0])
    if record is None:
        raise KeyError("Contact not found.")
    if record.birthday is None:
        return "Birthday not set for this contact."
    return record.birthday.value.strftime("%d.%m.%Y")


@input_error
def birthdays(args, book: AddressBook, _notebook=None):
    try:
        days = int(args[0]) if args else 7
    except ValueError:
        return "Invalid number of days. Use: birthdays [number]"
    upcoming = book.get_upcoming_birthdays(days)
    if not upcoming:
        return f"No birthdays in the next {days} days."
    return "\n".join(
        f"{item['name']} -> {item['congratulation_date']}"
        for item in upcoming
    )

# Нотатки

@input_error
def add_note(args, _book, notebook: Notebook):
    if len(args) < 2:
        raise IndexError
    title = args[0]
    content = " ".join(args[1:])
    note = Note(title, content)
    notebook.add_note(note)
    return f"Note '{title}' added."


@input_error
def edit_note(args, _book, notebook: Notebook):
    if len(args) < 2:
        raise IndexError
    title = args[0]
    new_content = " ".join(args[1:])
    note = notebook.find(title)
    if note is None:
        raise KeyError(f"Note '{title}' not found.")
    note.edit_content(new_content)
    return f"Note '{title}' updated."


@input_error
def delete_note(args, _book, notebook: Notebook):
    if not args:
        raise IndexError
    title = args[0]
    notebook.delete(title)
    return f"Note '{title}' deleted."


@input_error
def show_note(args, _book, notebook: Notebook):
    if not args:
        raise IndexError
    title = args[0]
    note = notebook.find(title)
    if note is None:
        raise KeyError(f"Note '{title}' not found.")
    return str(note)


@input_error
def show_all_notes(args, _book, notebook: Notebook):
    if not notebook.data:
        return "No notes saved."
    return "\n\n".join(str(n) for n in notebook.data.values())


@input_error
def search_notes(args, _book, notebook: Notebook):
    if not args:
        raise IndexError
    query = " ".join(args)
    results = notebook.search(query)
    if not results:
        return "No notes found."
    return "\n\n".join(str(n) for n in results)


@input_error
def add_tag(args, _book, notebook: Notebook):
    if len(args) < 2:
        raise IndexError
    title, tag = args[0], args[1]
    note = notebook.find(title)
    if note is None:
        raise KeyError(f"Note '{title}' not found.")
    note.add_tag(tag)
    return f"Tag '{tag}' added to note '{title}'."


@input_error
def remove_tag(args, _book, notebook: Notebook):
    if len(args) < 2:
        raise IndexError
    title, tag = args[0], args[1]
    note = notebook.find(title)
    if note is None:
        raise KeyError(f"Note '{title}' not found.")
    note.remove_tag(tag)
    return f"Tag '{tag}' removed from note '{title}'."


@input_error
def search_by_tag(args, _book, notebook: Notebook):
    if not args:
        raise IndexError
    tag = args[0]
    results = notebook.search_by_tag(tag)
    if not results:
        return f"No notes with tag '{tag}'."
    return "\n\n".join(str(n) for n in results)


@input_error
def sort_notes_by_tag(args, _book, notebook: Notebook):
    """sort-notes — виводить нотатки, відсортовані за першим тегом."""
    if not notebook.data:
        return "No notes saved."
    sorted_notes = notebook.sort_by_tag()
    return "\n\n".join(str(n) for n in sorted_notes)
