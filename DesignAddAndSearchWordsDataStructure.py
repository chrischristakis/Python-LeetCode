class WordDictionary(object):
    class Node:
        def __init__(self, char=None):
            self.char = char
            self.children = {}
            self.completed = False

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = self.Node(c)
            curr = curr.children[c]
        curr.completed = True

    def search(self, word):
        def search_char(node, target_index):
            if target_index >= len(word):
                return node.completed
            target = word[target_index]
            if target == '.':
                for child in node.children:
                    if search_char(node.children[child], target_index + 1):
                        return True
            if target not in node.children:
                return False
            return search_char(node.children[target], target_index + 1)

        return search_char(self.root, 0)


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))  # False
print(wordDictionary.search("bad"))  # True
print(wordDictionary.search(".ad"))  # True
print(wordDictionary.search("b.."))  # True
