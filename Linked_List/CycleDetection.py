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

    # Checking if ther is a cycle
    def cycleDetection(self):
        # Initialising the check to first node
        check = self.head
        # Initialising the temp to first node
        temp = self.head
        count = 0
        # Will traverse till we find the check or None
        # Here we have used count because since we ar checking if the temp == check and for the first time they are same so letting them go for the first time
        while temp:
            if temp == check:
                count += 1
                if count == 2:
                    return "Cycle Detected"
            temp = temp.nextPtr
                
        return "Cycle not Detected"            



#driver code

ll1 = LinkedList()

ll1.insertionAtEnd(30)
ll1.insertionAtEnd(40)
ll1.insertionAtEnd(50)
ll1.insertionAtEnd(60)
ll1.insertionAtEnd(31)
ll1.head.nextPtr.nextPtr.nextPtr.nextPtr = ll1.head
print("Insertion at the end of linkedlist")
# ll1.printLinkedList()
print(ll1.cycleDetection())