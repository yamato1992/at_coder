class Node:
    def __init__(self, char: str):
        self.before = None
        self.char = char
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.before = node
            self.head = node

    def add_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.before = self.tail
            self.tail.next = node
            self.tail = node
