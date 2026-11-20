"""
In-Memory File System
Design a file system that provides basic operations.

Operations: mkdir, addContent, readContent, ls
"""


class FileNode:
    def __init__(self, name: str, is_file: bool = False):
        self.name = name
        self.is_file = is_file
        self.content = ""
        self.children = {}


class FileSystem:
    def __init__(self):
        self.root = FileNode("/")

    def ls(self, path: str) -> list[str]:
        node = self._navigate(path)
        if node.is_file:
            return [node.name]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._create_path(path)

    def add_content(self, file_path: str, content: str) -> None:
        parts = self._split_path(file_path)
        node = self.root

        for part in parts[:-1]:
            if part not in node.children:
                node.children[part] = FileNode(part)
            node = node.children[part]

        file_name = parts[-1]
        if file_name not in node.children:
            node.children[file_name] = FileNode(file_name, is_file=True)

        node.children[file_name].content += content

    def read_content(self, file_path: str) -> str:
        node = self._navigate(file_path)
        if not node.is_file:
            raise ValueError(f"{file_path} is not a file")
        return node.content

    def _navigate(self, path: str) -> FileNode:
        if path == "/":
            return self.root
        parts = self._split_path(path)
        node = self.root
        for part in parts:
            if part not in node.children:
                raise FileNotFoundError(f"Path not found: {path}")
            node = node.children[part]
        return node

    def _create_path(self, path: str) -> FileNode:
        parts = self._split_path(path)
        node = self.root
        for part in parts:
            if part not in node.children:
                node.children[part] = FileNode(part)
            node = node.children[part]
        return node

    def _split_path(self, path: str) -> list[str]:
        return [p for p in path.split("/") if p]

    def tree(self, path: str = "/", prefix: str = "") -> str:
        """Display directory tree."""
        node = self._navigate(path)
        lines = [f"{prefix}{node.name}/"]
        children = sorted(node.children.keys())
        for i, name in enumerate(children):
            child = node.children[name]
            is_last = i == len(children) - 1
            connector = "└── " if is_last else "├── "
            if child.is_file:
                lines.append(f"{prefix}{connector}{name}")
            else:
                lines.append(f"{prefix}{connector}{name}/")
        return "\n".join(lines)


if __name__ == "__main__":
    fs = FileSystem()
    fs.mkdir("/home/user/documents")
    fs.mkdir("/home/user/pictures")
    fs.add_content("/home/user/documents/notes.txt", "Hello World\n")
    fs.add_content("/home/user/documents/notes.txt", "Second line\n")
    fs.add_content("/home/user/readme.md", "# My Files")

    print(f"ls /home/user: {fs.ls('/home/user')}")
    print(f"Read notes: {fs.read_content('/home/user/documents/notes.txt')}")
    print(f"\nTree:")
    print(fs.tree("/home"))
