class Node:
    def __init__(self, key: int, value: int, left: Optional[Node], right: Optional[Node]):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.left = Node(0, 0, None, None) # most recently used
        self.right = Node(0, 0, None, None) # least recently used
        self.left.right = self.right
        self.right.left = self.left
        self.h = dict()

    def get(self, key: int) -> int:
        if key in self.h.keys():
            n = self.h[key]
            self.remove(n)
            self.add(n, self.left)
            return n.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # If key already exists, update it and move to MRU
        if key in self.h:
            n = self.h[key]
            n.value = value
            self.remove(n)
            self.add(n, self.left)
            return
        
        # Key doesn't exist
        if self.count < self.capacity:
            # Capacity not full, just add
            n = Node(key, value, None, None)
            self.add(n, self.left)
            self.count += 1
            self.h[key] = n
        else:
            # Capacity full, evict LRU
            lru = self.right.left
            self.remove(lru)
            del self.h[lru.key]
            
            # Add new node
            n = Node(key, value, None, None)
            self.add(n, self.left)
            self.h[key] = n

    def remove(self, node: Node) -> None:
        left = node.left
        right = node.right
        left.right = right
        right.left = left
    
    def add(self, middle: Node, left: Node) -> None:
        right = left.right
        left.right = middle
        middle.right = right
        middle.left = left
        right.left = middle