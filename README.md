# Brain Management — Персональний помічник

## Структура проєкту

```
brain_management/
├── main.py                  # Точка входу
└── assistant/
    ├── __init__.py
    ├── contacts.py          # Класи Field, Name, Phone, Birthday, Record, AddressBook
    ├── notes.py             # TODO: Класи Tag, Note, Notebook
    ├── handlers.py          # Обробники команд
    ├── cli.py               # Головний цикл CLI
    └── storage.py           # Збереження/завантаження даних
```

## Запуск

```bash
python main.py
```

## Що вже зроблено (основа з попереднього коду)

- Класи `Field`, `Name`, `Phone`, `Birthday`, `Record`, `AddressBook` — у `contacts.py`
- Команди: `add`, `change`, `phone`, `all`, `add-birthday`, `show-birthday`, `birthdays`
- Збереження/завантаження адресної книги через `pickle` — у `storage.py`
- Головний цикл CLI — у `cli.py`

## TODO — що потрібно зробити команді

### contacts.py
- [ ] Клас `Email` з валідацією формату
- [ ] Клас `Address`
- [ ] Методи `add_email`, `add_address` у класі `Record`
- [ ] Метод `search(query)` у класі `AddressBook`
- [ ] Метод `delete(name)` у класі `AddressBook`

### notes.py
- [ ] Клас `Tag`
- [ ] Клас `Note` (title, content, tags)
- [ ] Клас `Notebook` з методами: `add_note`, `find`, `delete`, `search`, `search_by_tag`, `sort_by_tag`

### storage.py
- [ ] Розширити `save_data` / `load_data` для збереження `Notebook` разом з `AddressBook`

### handlers.py
- [ ] Додати обробники: `add_email`, `add_address`, `edit_email`, `search_contacts`, `delete_contact`
- [ ] Додати обробники для нотаток: `add_note`, `edit_note`, `delete_note`, `show_note`, `all_notes`, `search_notes`
- [ ] Додати обробники для тегів: `add_tag`, `remove_tag`, `search_notes_by_tag`, `sort_notes`

### cli.py
- [ ] Підключити `Notebook` до циклу
- [ ] Додати нові команди у `if/elif` блоки
