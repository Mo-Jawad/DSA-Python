class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None 
        self.next = None 

class DoublyLL:
    def __init__(self):
        self.head = None 

    def insertAtEnd(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return 

        current = self.head

        while current.next:
            current = current.next

        current.next = newNode
        newNode.prev = current 


    def insertAtBegin(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return 

        newNode.next = self.head 
        self.head.prev = newNode 
        self.head = newNode

    def removeFromBegin(self):
        if self.head is None:
            return

        self.head = self.head.next 

    def removeFromEnd(self):
        if self.head is None:
            return

        current = self.head 

        while current.next:
            current = current.next 

        current.prev.next = None   

    def printList(self):
        current = self.head 

        while current:
            print(current.data)
            current = current.next

List1 = DoublyLL()

List1.insertAtEnd(10)
List1.insertAtEnd(100)
List1.insertAtEnd(70)
List1.insertAtEnd(80)

List1.removeFromBegin()
List1.removeFromEnd()

List1.printList()