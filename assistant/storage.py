import pickle
from pathlib import Path

from .contacts import AddressBook
from .notes import Notebook


# Шлях до файлу збереження у домашній папці користувача
DEFAULT_PATH = Path.home() / ".personal_assistant" / "data.pkl"


def save_data(book: AddressBook, notebook: Notebook, path: Path = DEFAULT_PATH) -> None:
    """Серіалізує книгу контактів і нотатки у файл через pickle."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as file:
        pickle.dump({"book": book, "notebook": notebook}, file)


def load_data(path: Path = DEFAULT_PATH) -> tuple[AddressBook, Notebook]:
    try:
        with open(path, "rb") as file:
            data = pickle.load(file)
            # Підтримка старого формату (лише AddressBook без нотаток)
            if isinstance(data, AddressBook):
                return data, Notebook()
            return data["book"], data["notebook"]
    except FileNotFoundError:
        return AddressBook(), Notebook()
    except Exception:
        # Якщо файл пошкоджений — починаємо з чистого листа
        return AddressBook(), Notebook()
