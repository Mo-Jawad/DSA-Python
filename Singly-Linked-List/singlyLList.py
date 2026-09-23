# singly linked list - Jawad codes (DSA in Python)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next: ## loops till thee last item
            current_node = current_node.next

        current_node.next = new_node

        new_node.next = None

LList = SinglyLL()

LList.append(30)
LList.append(20)
LList.append(60)

current = LList.head

while current:
    print(current.data) ## prints every element in the List
    current = current.next

'''
output:

30
20
60
'''