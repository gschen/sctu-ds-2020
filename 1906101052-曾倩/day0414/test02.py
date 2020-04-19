class Node():
    def __init__(self,val=None):
        self.val=val
        self.left=None
        self.right=None

class tree():
    def __init__(self):
        self.root=None
    def add_left(self,val):
        node=Node(val)
        if self.root==None:
            self.root=node
        else:
            node.self=self.root.self
            vroot.left=node
    def add_right(self,val):
        node=Node(val)
        if self.root==None:
            self.root=node
        else:
            node.right=self.root.right
            self.root.right=node
        
    def travel(self):
        def tra(node):
            if node == Node:
                return
            print(node.val)
            tra(node.left)
            tra(node.right)
        tra(self.root)

tree=Tree()
tree.add_left(10)
tree.add_right(20)
tree.add_left(30)
tree.add_right(40)
tree.add_left(50)