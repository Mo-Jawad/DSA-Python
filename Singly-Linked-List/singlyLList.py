# singly linked list - Jawad codes (DSA in Python)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return 
        else:
            newNode.next = self.head 
            self.head = newNode
            return 
        


    def insertInMiddle(self, data, num):
        newNode = Node(data)

        if self.head is None:
            print("List is empty")
            return 

        current = self.head 

        while current is not None:
            if current.data == num:
                newNode.next = current.next 
                current.next = newNode
                return

            current = current.next

        print("enterred false number")

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

LList.insertInMiddle(80, 60)
LList.insertInMiddle(820, 20)

LList.insertAtBegin(700)

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