class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class Queue:
    def __init__(self):
        self.head: Node = Node("head")
        self.tail: Node = Node("tail")
        self.size = 0
        
    def isEmpty(self):
        return (self.size == 0)

    def add(self, value):
        new_node: Node = Node(value)
        if (not self.isEmpty()): # when queue is not empty, it is not none
            self.tail.next.next = new_node
            self.tail.next = new_node
        else: # queue is empty
            self.head.next = new_node
            self.tail.next = new_node
        self.size += 1
        return
    
    def remove(self):
        if (not self.isEmpty()):
            raise Exception("The queue is empty!")
        remove: Node = self.head.next
        self.head.next = remove.next
        self.size -= 1
        return remove.value
    
    def peek(self):
        if (not self.isEmpty()):
            raise Exception("The queue is empty!")
        return self.head.next.value