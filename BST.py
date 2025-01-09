
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        newNode=Node(data)
        if self.root is None:
            self.root=newNode
            return
        ptr=self.root
        curr=self.root
        while curr:
            ptr=curr
            if data<curr.data:
                curr=curr.left
            elif data>curr.data:
                curr=curr.right
            else:
                return
        if data<ptr.data:
            ptr.left=newNode
        else:
            ptr.right=newNode

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end="-> ")
            self.inorder(node.right)
    def inorder_helper(self):
        self.inorder(self.root)
        print("NULL")
b=BST()
b.insert(1)
b.insert(2)
b.insert(3)
b.insert(4)
b.inorder_helper()

        
