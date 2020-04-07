
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class Dll(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        if self.head == None:
            node.right = None
            node.lelf = None
            self.head = node
            self.tail = node
        else:
            node.right = self.head
            self.head.left = node
            node.left = None
            self.head = node
    
    def remove(self, node):
        if self.head == None or node == None:
            return
        elif node == self.head:
            self.head = node.right
            if self.head:
                self.head.left = None
        elif node == self.tail:
            self.tail = self.tail.left
            if self.tail:
                self.tail.right = None
        else:
            node_prev = node.left
            node_next = node.right
            if node_prev:
                node_prev.right = node_next
            if node_next:
                node_next.left = node_prev

    def remove_tail_node(self):
        node = self.tail
        if node != None:
            self.tail = node.left
            if self.tail:
                self.tail.right = None
        return node           

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.size = 0
        self.dll = Dll()
        self.hashmap = {}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.hashmap.keys():
            node = self.hashmap[key]
            self.dll.remove(node)
            self.dll.add(node)
            return node.value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        node = Node(key, value)
        if self.size == self.capacity:
            tail_node = self.dll.remove_tail_node()
            del self.hashmap[tail_node.key]
            self.size -= 1
        self.dll.add(node)
        self.hashmap[key] = node
        self.size += 1

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

def print_dll():
    print("print DLL -- forwards")
    head = our_cache.dll.head
    while head:
        print(head.value)
        head = head.right
    print("print DLL -- backwards")
    tail = our_cache.dll.tail
    while tail:
        print(tail.value)
        tail = tail.left


ret = our_cache.get(1)       # returns 1
print(f"get(1) = {ret}")

# print_dll()

ret = our_cache.get(2)       # returns 2
print(f"get(2) = {ret}")
ret = our_cache.get(9)      # returns -1 because 9 is not present in the cache
print(f"get(9) = {ret}")

our_cache.set(5, 5) 

our_cache.set(6, 6)
print_dll()
ret = our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(f"get(3) = {ret}")
