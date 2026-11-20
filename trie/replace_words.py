"""
🟡 Replace Words
Replace words in a sentence with their shortest root from a dictionary.

Time:  O(n * m) where n = words, m = max word length
Space: O(total characters in dictionary)
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_root = False


def replace_words(dictionary: list[str], sentence: str) -> str:
    root = TrieNode()
    for word in dictionary:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_root = True

    def find_root(word):
        node = root
        for i, char in enumerate(word):
            if char not in node.children:
                return word
            node = node.children[char]
            if node.is_root:
                return word[:i + 1]
        return word

    words = sentence.split()
    return " ".join(find_root(w) for w in words)


if __name__ == "__main__":
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(replace_words(dictionary, sentence))
    # "the cat was rat by the bat"
