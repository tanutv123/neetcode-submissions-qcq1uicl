class Node:
    def __init__(self, key: int, val: int, prev: Node = None, next: Node = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def add(self, node: Node):
        prev = self.right.prev
        prev.next = self.right.prev = node
        node.prev, node.next = prev, self.right


    def remove(self, node: Node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        node.prev = node.next = None

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
            self.remove(node)
        
        node.val = value
        self.add(node)
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
