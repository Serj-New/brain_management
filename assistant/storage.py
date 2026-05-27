import pickle
from pathlib import Path

from .contacts import AddressBook
# TODO: Імпортувати Notebook з notes.py після його реалізації
# from .notes import Notebook


# Шлях до файлу збереження
DEFAULT_PATH = Path.home() / ".personal_assistant" / "data.pkl"


# Збереження даних на диск
def save_data(book, path=DEFAULT_PATH):
    # TODO: Розширити для збереження notebook разом з book
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as file:
        pickle.dump(book, file)


# Завантаження даних з диску
def load_data(path=DEFAULT_PATH):
    # TODO: Розширити для завантаження notebook разом з book
    try:
        with open(path, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()
