from .handlers import (
    add_contact,
    change_contact,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
    # TODO: Імпортувати нові хендлери після реалізації
)
from .storage import load_data, save_data


# Розбір введеної команди
def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.lower(), args


def run():
    book = load_data()
    # TODO: Також завантажувати notebook після реалізації storage та notes

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        if not user_input.strip():
            print("Invalid command.")
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            # TODO: Також зберігати notebook
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        # TODO: Додати нові команди:
        # add-email, add-address, search-contacts, delete-contact
        # add-note, edit-note, delete-note, show-note, all-notes,
        # search-notes, add-tag, remove-tag, search-tag, sort-notes

        else:
            print("Invalid command.")
