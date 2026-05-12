class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
node1=Node(10)
node2=Node(20)
node3=Node(30)

# Linking nodes
node1.next=node2
node2.next=node3

# Traversing the linked list *why cant we use a for loop?*
head = node1
while head:
    print(head.data, end=" ->  ")
    head=head.next

print("None")

# Insert a new note at the beginning of the linked list
new_node = Node(5)
new_node.next = node1
node1=new_node

# Traversing the linked list after insertion
head = node1
while head:
    print(head.data, end=" ->  ")
    head=head.next

print("None")

# Insert a new node at the end of the linked list
new_node = Node(40)
node3.next = new_node

# Traversing the linked list after insertion
head = node1
while head:
    print(head.data, end=" ->  ")
    head=head.next
print("None")