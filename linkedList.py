class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insertAtBegin(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    
    def insertAtEnd(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newNode
    def deleteAtHead(self):
        if self.head is None:
            return
        self.head=self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            return
        temp=self.head
        while temp.next and temp.next.next:
            temp=temp.next
        temp.next=None

    def traverse(self):
        temp=self.head
        while temp.next:
            print(temp.data,end="->")
            temp=temp.next
        print(temp.data,"->NULL")

ll=LinkedList()
ll.insertAtBegin(1)
ll.insertAtBegin(2)
ll.insertAtBegin(3)

ll.traverse()
ll.insertAtEnd(7)
ll.insertAtEnd(8)
ll.insertAtEnd(9)
ll.traverse()
ll.deleteAtHead()
ll.traverse()
ll.deleteAtEnd()
ll.traverse()