from collections import UserDict


class Tag:
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other) -> bool:
        if isinstance(other, Tag):
            return self.value == other.value
        return self.value == str(other)


class Note:
    def __init__(self, title: str, content: str, tags: list[str] | None = None):
        self.title = title
        self.content = content
        self.tags: list[Tag] = [Tag(t) for t in (tags or [])]

    def edit_content(self, new_content: str) -> None:
        self.content = new_content

    def add_tag(self, tag: str) -> None:
        if Tag(tag) in self.tags:
            raise ValueError(f"Tag '{tag}' already exists on this note.")
        self.tags.append(Tag(tag))

    def remove_tag(self, tag: str) -> None:
        for existing in self.tags:
            if existing == tag:
                self.tags.remove(existing)
                return
        raise KeyError(f"Tag '{tag}' not found on this note.")

    def __str__(self) -> str:
        tag_str = "  ".join(str(t) for t in self.tags) if self.tags else "no tags"
        return (
            f"Title   : {self.title}\n"
            f"Content : {self.content}\n"
            f"Tags    : {tag_str}"
        )


class Notebook(UserDict):
    def add_note(self, note: Note) -> None:
        if note.title in self.data:
            raise ValueError(f"Note '{note.title}' already exists.")
        self.data[note.title] = note

    def find(self, title: str) -> Note | None:
        return self.data.get(title)

    def delete(self, title: str) -> None:
        if title not in self.data:
            raise KeyError(f"Note '{title}' not found.")
        del self.data[title]

    def search(self, query: str) -> list[Note]:
        q = query.lower()
        return [
            note for note in self.data.values()
            if q in note.title.lower() or q in note.content.lower()
        ]

    def search_by_tag(self, tag: str) -> list[Note]:
        return [
            note for note in self.data.values()
            if tag in note.tags
        ]

    def sort_by_tag(self) -> list[Note]:
        def sort_key(note: Note) -> tuple:
            if note.tags:
                return (0, note.tags[0].value.lower())
            return (1, "")

        return sorted(self.data.values(), key=sort_key)

    def __str__(self) -> str:
        if not self.data:
            return "No notes found."
        return "\n\n".join(str(note) for note in self.data.values())