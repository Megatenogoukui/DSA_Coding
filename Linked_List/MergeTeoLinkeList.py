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

def mergeLinkedList(head1 , head2):
        temp = None
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        
        if head1.data < head2.data:
            temp = head1
            temp.nextPtr = mergeLinkedList(head1.nextPtr , head2)
        else:
            temp = head2
            temp.nextPtr = mergeLinkedList(head1 , head2.nextPtr)

            

        return temp
#driver code

ll1 = LinkedList()

ll1.insertAtBegining(20)
ll1.insertAtBegining(10)
ll1.insertionAtEnd(30)
print("Linked List 1 : ")
ll1.printLinkedList()
print()
ll2 = LinkedList()
ll2.insertionAtEnd(11)
ll2.insertionAtEnd(22)
ll2.insertionAtEnd(33)
print("Linked List 2 : ")
ll2.printLinkedList()
print()
ll3 = LinkedList()
print("Merged Linked LIst 1 and linked List 2")
ll3.head = mergeLinkedList(ll1.head, ll2.head)
ll3.printLinkedList()