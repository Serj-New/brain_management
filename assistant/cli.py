from .handlers import (
    add_contact, change_contact, delete_contact,
    show_phone, show_all, search_contacts,
    add_email, add_address,
    add_birthday, show_birthday, birthdays,
    add_note, edit_note, delete_note,
    show_note, show_all_notes, search_notes,
    add_tag, remove_tag, search_by_tag, sort_notes_by_tag,
)
from .storage import load_data, save_data
from .matcher import suggest_command


COMMANDS = {
    # Контакти
    "add":              add_contact,
    "change":           change_contact,
    "delete-contact":   delete_contact,
    "phone":            show_phone,
    "all":              show_all,
    "search":           search_contacts,
    "add-email":        add_email,
    "add-address":      add_address,
    "add-birthday":     add_birthday,
    "show-birthday":    show_birthday,
    "birthdays":        birthdays,
    # Нотатки
    "add-note":         add_note,
    "edit-note":        edit_note,
    "delete-note":      delete_note,
    "show-note":        show_note,
    "all-notes":        show_all_notes,
    "search-notes":     search_notes,
    "add-tag":          add_tag,
    "remove-tag":       remove_tag,
    "search-tag":       search_by_tag,
    "sort-notes":       sort_notes_by_tag,
}

# Команди без аргументів (args ігноруються)
NO_ARGS_COMMANDS = {"all", "all-notes", "sort-notes"}

HELP_TEXT = """
┌─────────────────────────────────────────────────────────────────┐
│                     ПЕРСОНАЛЬНИЙ ПОМІЧНИК                       │
├──────────────────────┬──────────────────────────────────────────┤
│ КОМАНДА              │ ОПИС                                     │
├──────────────────────┼──────────────────────────────────────────┤
│ Контакти                                                        │
│  add <n> <phone>     │ Додати контакт / телефон                 │
│  change <n> <o> <new>│ Замінити телефон                         │
│  delete-contact <n>  │ Видалити контакт                         │
│  phone <name>        │ Показати телефони                        │
│  all                 │ Усі контакти                             │
│  search <query>      │ Пошук контактів                          │
│  add-email <n> <e>   │ Додати email                             │
│  add-address <n> <a> │ Додати адресу                            │
│  add-birthday <n> <d>│ Додати д/н (DD.MM.YYYY)                  │
│  show-birthday <n>   │ Показати д/н                             │
│  birthdays [days]    │ Д/н у наступні N днів (за замовч. 7)     │
├──────────────────────┼──────────────────────────────────────────┤
│ Нотатки                                                         │
│  add-note <t> <text> │ Нова нотатка                             │
│  edit-note <t> <text>│ Редагувати вміст                         │
│  delete-note <t>     │ Видалити нотатку                         │
│  show-note <t>       │ Показати нотатку                         │
│  all-notes           │ Усі нотатки                              │
│  search-notes <q>    │ Пошук у нотатках                         │
│  add-tag <t> <tag>   │ Додати тег                               │
│  remove-tag <t> <tag>│ Видалити тег                             │
│  search-tag <tag>    │ Пошук за тегом                           │
│  sort-notes          │ Нотатки за тегами                        │
├──────────────────────┼──────────────────────────────────────────┤
│  hello               │ Привітання                               │
│  help                │ Це меню                                  │
│  exit / close        │ Зберегти і вийти                         │
└──────────────────────┴──────────────────────────────────────────┘"""


def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.strip().split()
    if not parts:
        return "", []
    return parts[0].lower(), parts[1:]


def run() -> None:
    book, notebook = load_data()

    print("Ласкаво просимо до Персонального помічника!")
    print('Введіть "help" для перегляду списку команд або "exit" для виходу.')

    while True:
        try:
            user_input = input("\n>>> ").strip()
        except (EOFError, KeyboardInterrupt):
            # Коректне завершення при Ctrl+C або кінці потоку
            save_data(book, notebook)
            print("\nGood bye!")
            break

        if not user_input:
            continue

        command, args = parse_input(user_input)

        # --- Службові команди ---
        if command in ("exit", "close"):
            save_data(book, notebook)
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
            continue

        if command == "help":
            print(HELP_TEXT)
            continue

        # --- Диспетчер бізнес-команд ---
        if command in COMMANDS:
            handler = COMMANDS[command]
            if command in NO_ARGS_COMMANDS:
                # Ці обробники не потребують args
                print(handler(args, book, notebook))
            else:
                print(handler(args, book, notebook))
            continue

        # --- Невідома команда: підказки через matcher ---
        suggestions = suggest_command(command, list(COMMANDS.keys()))
        if suggestions:
            print(f"Unknown command '{command}'.")
            print("Did you mean: " + ", ".join(suggestions) + "?")
        else:
            print(f"Unknown command '{command}'. Type 'help' to see all commands.")
