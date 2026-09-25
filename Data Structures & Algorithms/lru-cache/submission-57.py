class Node:
    def __init__(self, key, val, prev: Node = None, next: Node = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def add(self, node):
        prev, next = self.right.prev, self.right
        node.prev, node.next = prev, next
        prev.next = next.prev = node
    
    def remove(self, node):
        prev, next = node.prev, node.next
        node.prev = node.next = None
        prev.next, next.prev = next, prev
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node
        else:
            node = self.cache[key]
            node.val = value
            self.remove(node)
        self.add(node)
        if self.cap < len(self.cache):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
