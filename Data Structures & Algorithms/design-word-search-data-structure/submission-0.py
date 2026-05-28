class Node:
    def __init__(self, char=""):
        self.char = char
        self.children = {}  # Use dict instead of list for O(1) lookup
        self.is_word = False
    
    def find(self, char):
        return self.children.get(char)

    def add(self, char):
        if char not in self.children:
            self.children[char] = Node(char)
        return self.children[char]

class WordDictionary:
    def __init__(self):
        self.root = Node("")

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.add(char)
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            # Base case: reached end of word
            if index == len(word):
                return node.is_word
            
            char = word[index]
            
            if char == ".":
                # Wildcard: try all children
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                # Regular character: find specific child
                child = node.find(char)
                if not child:
                    return False
                return dfs(child, index + 1)
        
        return dfs(self.root, 0)