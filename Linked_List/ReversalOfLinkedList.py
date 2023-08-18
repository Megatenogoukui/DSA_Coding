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
    
    # Reversing a linkedList
    def reversal(self ):
        current = self.head
        next = None
        prev = None

        while current:
            next = current.nextPtr
            current.nextPtr = prev
            prev = current
            current = next
        self.head = prev

    #Printing the linked list
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " " ,end = " ")
            temp = temp.nextPtr
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
ll1.reversal()
print("Reversal of a linkedlist")
ll1.printLinkedList()