"""
Text Editor with Undo/Redo
Implement a simple text editor supporting undo and redo operations.

Pattern: Command Pattern + Stack
"""
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class InsertCommand(Command):
    def __init__(self, editor, position: int, text: str):
        self.editor = editor
        self.position = position
        self.text = text

    def execute(self):
        self.editor._content = (
            self.editor._content[:self.position] +
            self.text +
            self.editor._content[self.position:]
        )

    def undo(self):
        self.editor._content = (
            self.editor._content[:self.position] +
            self.editor._content[self.position + len(self.text):]
        )


class DeleteCommand(Command):
    def __init__(self, editor, position: int, length: int):
        self.editor = editor
        self.position = position
        self.length = length
        self.deleted_text = ""

    def execute(self):
        self.deleted_text = self.editor._content[self.position:self.position + self.length]
        self.editor._content = (
            self.editor._content[:self.position] +
            self.editor._content[self.position + self.length:]
        )

    def undo(self):
        self.editor._content = (
            self.editor._content[:self.position] +
            self.deleted_text +
            self.editor._content[self.position:]
        )


class TextEditor:
    def __init__(self):
        self._content = ""
        self._undo_stack = []
        self._redo_stack = []
        self.cursor = 0

    @property
    def content(self):
        return self._content

    def insert(self, text: str):
        cmd = InsertCommand(self, self.cursor, text)
        cmd.execute()
        self._undo_stack.append(cmd)
        self._redo_stack.clear()
        self.cursor += len(text)

    def delete(self, length: int = 1):
        if self.cursor < length:
            length = self.cursor
        cmd = DeleteCommand(self, self.cursor - length, length)
        cmd.execute()
        self._undo_stack.append(cmd)
        self._redo_stack.clear()
        self.cursor -= length

    def undo(self):
        if not self._undo_stack:
            return
        cmd = self._undo_stack.pop()
        cmd.undo()
        self._redo_stack.append(cmd)

    def redo(self):
        if not self._redo_stack:
            return
        cmd = self._redo_stack.pop()
        cmd.execute()
        self._undo_stack.append(cmd)

    def move_cursor(self, position: int):
        self.cursor = max(0, min(position, len(self._content)))


if __name__ == "__main__":
    editor = TextEditor()
    editor.insert("Hello")
    print(f"After insert: '{editor.content}'")
    editor.insert(" World")
    print(f"After insert: '{editor.content}'")
    editor.undo()
    print(f"After undo: '{editor.content}'")
    editor.redo()
    print(f"After redo: '{editor.content}'")
    editor.delete(5)
    print(f"After delete: '{editor.content}'")
    editor.undo()
    print(f"After undo: '{editor.content}'")
