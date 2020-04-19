#树节点的构建
class Node():
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None
#构建树
class Tree():
    def __init__(self):
        self.root = None
    def add_left(self,val):
        node = Node(val)
        if self.root==None:
            self.root = node
        else:
            node.left = self.root.left
            self.root.left = node

    def add_right(self,val):
        node = Node(val)
        if self.root==None:
            self.root = node
        else:
            node.right = self.root.right
            self.root.right = node
#遍历树

    def travel(self):
        def tra(node):
            print(node.val)
            tra(node.left)
            tra(node.right)
