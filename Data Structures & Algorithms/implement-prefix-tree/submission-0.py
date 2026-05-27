class Node:
    def __init__(self, char: str) -> None:
        self.char = char
        self.nexts = []
        self.parent = None
        self.end = False
    
    def add(self, char):
        new = Node(char)
        new.parent = self
        self.nexts.append(new)
        return new
    
    def terminate(self):
        self.end = True
    
    def find(self, char):
        for node in self.nexts:
            if node.char == char:
                return node
        return None

class PrefixTree:
    def __init__(self):
        self.start = Node("start")

    def insert(self, word: str):
        curr = self.start
        for char in word:
            query = curr.find(char)
            if query:
                curr = query
            else:
                temp = curr.add(char)
                curr = temp
        curr.terminate()

    def search(self, word: str) -> bool:
        curr = self.start
        for char in word:
            temp = curr.find(char)
            if temp:
                curr = temp
            else:
                return False
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.start
        for char in prefix:
            temp = curr.find(char)
            if temp:
                curr = temp
            else:
                return False
        return True
        
        