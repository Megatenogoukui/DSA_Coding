# Creating  a new node

class Node:

    def __init__(self , data) :
        self.data = data
        self.nextPtr = None

class LinkedList :

    def __init__(self):
        self.head = None

    # Inserting a new value to a linked list at the begining
    def insertAtBegining(self , new_data):
        #creating a new node
        newNode = Node(new_data)

        #insertion at the begining
        newNode.nextPtr = self.head
        self.head = newNode


    # Inserting a new value to a linked list
    def insertionAtEnd(self,new_data):
        # creating new node 
        newNode = Node(new_data)
        
        #If the linked list is empty
        if self.head == None:
            self.head = newNode
            return
        
        #Inserting a new node at the  end
        temp = self.head
        while temp.nextPtr:
            temp = temp.nextPtr
        temp.nextPtr = newNode
        
        

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

ll1.insertionAtEnd(30)
ll1.insertionAtEnd(40)
ll1.insertionAtEnd(50)
ll1.insertionAtEnd(60)
ll1.insertionAtEnd(31)

ll1.printLinkedList()