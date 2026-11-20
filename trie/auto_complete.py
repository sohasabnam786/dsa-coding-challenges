"""
🟡 Autocomplete System
Design a search autocomplete system with ranking.

Time:  O(m) for each character input
Space: O(n * m) for all stored sentences
"""
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)


class AutocompleteSystem:
    def __init__(self, sentences: list[str], times: list[int]):
        self.root = TrieNode()
        self.current_input = ""
        self.current_node = self.root
        self.dead = TrieNode()  # Dead-end node

        for sentence, count in zip(sentences, times):
            self._insert(sentence, count)

    def _insert(self, sentence: str, count: int):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sentences[sentence] += count

    def input(self, c: str) -> list[str]:
        if c == "#":
            self._insert(self.current_input, 1)
            self.current_input = ""
            self.current_node = self.root
            return []

        self.current_input += c

        if c not in self.current_node.children:
            self.current_node = self.dead
            return []

        self.current_node = self.current_node.children[c]
        sentences = self.current_node.sentences

        # Sort by frequency (desc), then alphabetically
        ranked = sorted(sentences.items(), key=lambda x: (-x[1], x[0]))
        return [s for s, _ in ranked[:3]]


if __name__ == "__main__":
    system = AutocompleteSystem(
        ["i love you", "island", "iroman", "i love leetcode"],
        [5, 3, 2, 2]
    )
    print(system.input("i"))   # ["i love you", "island", "i love leetcode"]
    print(system.input(" "))   # ["i love you", "i love leetcode"]
    print(system.input("a"))   # []
    print(system.input("#"))   # []
