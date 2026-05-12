class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:

    # Constructor to initialize the linked list
    # The head of the linked list is initialized to None, indicating that the list is empty.
    def __init__(self):
        self.head = None

    # Inset at the beginning of the linked list 
    def insert_beginning(self, data):
        new_node=Node(data)

    # Insert a new node at the end of the linked list
    def insert_at_end(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node