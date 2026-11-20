"""
🟡 Trie (Prefix Tree)
Implement a trie with insert, search, and startsWith operations.

Time:  O(m) for each operation, where m is the word length
Space: O(n * m) where n is number of words
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0  # Number of words with this prefix


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def count_prefix(self, prefix: str) -> int:
        node = self._find_node(prefix)
        return node.count if node else 0

    def _find_node(self, prefix: str) -> TrieNode:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def get_all_words(self) -> list[str]:
        words = []
        def dfs(node, path):
            if node.is_end:
                words.append("".join(path))
            for char, child in sorted(node.children.items()):
                path.append(char)
                dfs(child, path)
                path.pop()
        dfs(self.root, [])
        return words

    def delete(self, word: str) -> bool:
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                return False
            should_delete = _delete(node.children[char], word, depth + 1)
            if should_delete:
                del node.children[char]
                return not node.is_end and len(node.children) == 0
            return False
        return _delete(self.root, word, 0)


if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "apricot", "banana", "band", "bandana"]
    for w in words:
        trie.insert(w)

    print(trie.search("apple"))       # True
    print(trie.search("app"))         # True
    print(trie.search("ap"))          # False
    print(trie.starts_with("ap"))     # True
    print(trie.count_prefix("ban"))   # 3
    print(trie.get_all_words())
