class Node:

    def __init__(self , data) :
        self.data = data
        self.nextPtr = None

class LinkedList :

    def __init__(self):
        self.head = None

# Inserting a new value to a linked list
    def insertionAtEnd(self,new_data):
        # creating new node 
        newNode = Node(new_data)
        
        #If the linked list is empty
        if self.head == None:
            self.head = newNode
            return
        
        #Inserting a new node at the 
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

    # Deletion Of a node
    def deletion(self,pos):
        temp = self.head
        for i in range(pos - 1):
            temp = temp.nextPtr
            if temp == None:
                return
        temPtr = temp.nextPtr.nextPtr
        # temp.nextPtr = None
        temp.nextPtr = temPtr

#driver code

ll1 = LinkedList()

ll1.insertionAtEnd(30)
ll1.insertionAtEnd(40)
ll1.insertionAtEnd(50)
ll1.insertionAtEnd(60)
ll1.insertionAtEnd(31)
print("Insertion at the end of linkedlist")
ll1.printLinkedList()
print()
ll1.deletion(4)
ll1.printLinkedList()