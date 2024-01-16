# stack implementation using linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    # Initializing
    # use a dummy node for edge cases
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    
    # string representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        
        return out[:-2]

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return (self.size == 0)

    def peek(self):
        if self.isEmpty():
            raise Exception("the stack is empty currently")
        return self.head.next.value
    
    def pop(self):
        if self.isEmpty():
            raise Exception("the stack is empty currently")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
    
    def push(self, data):
        new_node = Node(data)
        
        new_node.next = self.head.next
        self.head.next = new_node

        self.size += 1
        return