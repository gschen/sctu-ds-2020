class Node():
    def __init__(self,val=Node):
        self.val=val
        self.left=None
        self.right=None
class Tree():
    def __init__(self):
        self.root=None
    def add_left(self):
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

tree=Tree()
tree.add_left(10)
tree.add_right(20)
tree.add_left(30)
tree.add_right(40)
tree.add_left(50)
tree.travel()
