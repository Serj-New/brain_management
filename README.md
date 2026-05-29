# Команда "Brain Management (Менеджмент головного мозку)" — Персональний помічник

## Опис

Консольний персональний помічник для керування контактами та нотатками.
Дані зберігаються на диску і не втрачаються між сесіями.

## Встановлення

```bash
# Клонувати або розпакувати проєкт, перейти у папку
cd brain_management

# Python 3.10+ (стандартна бібліотека, без залежностей)
python main.py
```

## Запуск

```bash
python main.py
```

Для виходу введіть `exit` або `close`.

---

## Команди

### Контакти

| Команда          | Аргументи                        | Опис                                            |
| ---------------- | -------------------------------- | ----------------------------------------------- |
| `add`            | `<name> <phone>`                 | Додати контакт або телефон                      |
| `change`         | `<name> <old_phone> <new_phone>` | Замінити номер телефону                         |
| `delete-contact` | `<name>`                         | Видалити контакт                                |
| `phone`          | `<name>`                         | Показати телефони контакту                      |
| `all`            | —                                | Усі контакти                                    |
| `search`         | `<query>`                        | Пошук за ім'ям, телефоном, email, адресою       |
| `add-email`      | `<name> <email>`                 | Додати або оновити email                        |
| `add-address`    | `<name> <address>`               | Додати або оновити адресу                       |
| `add-birthday`   | `<name> <DD.MM.YYYY>`            | Додати день народження                          |
| `show-birthday`  | `<name>`                         | Показати день народження                        |
| `birthdays`      | `[days]`                         | Дні народження в наступні N днів (за замовч. 7) |

### Нотатки

| Команда        | Аргументи                  | Опис                                  |
| -------------- | -------------------------- | ------------------------------------- |
| `add-note`     | `<title> <content...>`     | Нова нотатка                          |
| `edit-note`    | `<title> <new_content...>` | Редагувати вміст                      |
| `delete-note`  | `<title>`                  | Видалити нотатку                      |
| `show-note`    | `<title>`                  | Показати нотатку                      |
| `all-notes`    | —                          | Усі нотатки                           |
| `search-notes` | `<query>`                  | Пошук у заголовку або вмісті          |
| `add-tag`      | `<title> <tag>`            | Додати тег до нотатки                 |
| `remove-tag`   | `<title> <tag>`            | Видалити тег                          |
| `search-tag`   | `<tag>`                    | Пошук нотаток за тегом                |
| `sort-notes`   | —                          | Нотатки, відсортовані за першим тегом |

### Службові

| Команда          | Опис                   |
| ---------------- | ---------------------- |
| `hello`          | Привітання             |
| `help`           | Список усіх команд     |
| `exit` / `close` | Зберегти дані та вийти |

---

## Приклади використання

```
>>> add Mykola 0991234567
Contact added.

>>> add-email Mykola mykola@example.com
Email added.

>>> add-address Mykola Kyiv, Khreshchatyk 1
Address added.

>>> add-birthday Mykola 06.06.1913
Birthday added.

>>> all
Contact name: Mykola, phones: 0991234567, email: mykola@example.com, address: Kyiv, Khreshchatyk 1, birthday: 06.06.1913

>>> birthdays 30
Mykola -> 08.06.2026

>>> add-note Shopping Buy milk and bread
Note 'Shopping' added.

>>> add-tag Shopping personal
Tag 'personal' added to note 'Shopping'.

>>> search-tag personal
Title   : Shopping
Content : Buy milk and bread
Tags    : personal
```

---

## Валідація

- **Телефон**: рівно 10 цифр, лише цифри. Приклад: `0991234567`
- **Email**: формат `user@domain.tld`. Приклад: `john@example.com`
- **Дата**: формат `DD.MM.YYYY`. Приклад: `06.06.1913`

При некоректному введенні програма повідомляє про помилку і **не завершується**.

---

## Збереження даних

Дані зберігаються у файлі:

- **Linux/macOS**: `~/.personal_assistant/data.pkl`
- **Windows**: `C:\Users\<YourName>\.personal_assistant\data.pkl`

Файл створюється автоматично при першому виході командою `exit`.

---

## Структура проєкту

```
brain_management/
├── main.py                  # Точка входу
├── README.md
└── assistant/
    ├── __init__.py
    ├── contacts.py          # Field, Name, Phone, Email, Address, Birthday, Record, AddressBook (Авторка - Тетяна Баталова)
    ├── notes.py             # Tag, Note, Notebook (Автор - Євгеній Грішаєв)
    ├── handlers.py          # Обробники команд (Автор - Сергій Новіков)
    ├── cli.py               # REPL-цикл, диспетчер (Автор - Сергій Новіков)
    ├── storage.py           # Збереження/завантаження pickle (Автор - Сергій Новіков)
    └── matcher.py           # Підказки при невідомих командах (Автор - Сергій Новіков)
```
