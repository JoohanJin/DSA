# Basic implementation using oop
class Node:
    def __init__(self, data: int): # data can be any type
        self.data = data
        self.next = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        # Make the new node and insert at the head
        if (self.head == None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return
    
    def insert_at_index(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if (index == 0):
            self.insert_at_begin(data)
        else:
            while (current_node != None and position+1 != index):
                position = position + 1
                current_node = current_node.next
            
            if current_node == Node:
                return -1
            else:
                new_node.next = current_node.next
                current_node.next = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    def delete_at_index(self, data, index):
        if (not self.head):
            return -1

        current_node = self.head
        position = 0
        if index == 0:
            self.head = self.head.next
        else:
            while (current_node and position+1 != index):
                position = position + 1
                current_node = current_node.next
            if not current_node:
                return -1
            else:
                current_node.next = current_node.next.next

