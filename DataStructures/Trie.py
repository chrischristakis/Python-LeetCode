class Trie:
    class Node:
        def __init__(self, char=None):
            self.char = char
            self.children = {}
            self.completed = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = self.Node(char)
            curr = curr.children[char]
        curr.completed = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.completed

    def starts_with(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))    # True
print(trie.search("app"))      # False
print(trie.starts_with("app"))  # True
trie.insert("app")
print(trie.search("app"))      # True
