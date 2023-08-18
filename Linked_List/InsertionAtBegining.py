# Creating  a new node

class Node:

    def __init__(self , data) :
        self.data = data
        self.nextPtr = None

class LinkedList :

    def __init__(self):
        self.head = None

    # Inserting a new value to a linked list
    def insertAtBegining(self , new_data):
        #creating a new node
        newNode = Node(new_data)

        #insertion at the begining
        newNode.nextPtr = self.head
        self.head = newNode

    #Printing the linked list
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " " ,end = " ")
            temp = temp.nextPtr
#driver code

ll1 = LinkedList()
ll1.insertAtBegining(10)
ll1.insertAtBegining(20)
ll1.printLinkedList