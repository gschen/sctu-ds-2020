class Node():
    def __init__(self,val=None):
        self.val=val
        self.left=None 
        self.right=None

class Tree():
    def __init__(self):
        self.root=None
    def add_left(self,val):
        node=Node(val)
        if self.root==None:
            self.root=node
        else:
            node.left=self.root.left
            self.root.left=node

    def add_right(self,val):
        node=Node(val)
        if self.root==None:
            self.root=node
        else:
            node.right=self.root.right
            self.root.right=node


    def travel(self):
        def tra(node):
            if node==None:
                return
            print(node.val)
            tra(node.left)
            tra(node.right)
        tra(self.root)


tree=Tree()
tree.add_right(10)
tree.add_left(20)
tree.travel()