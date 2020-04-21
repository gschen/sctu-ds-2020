class Node():
    def __init__(self,val=None):
        self.val=val
        self.next=None
class SingleLink():
    def __init__(self):
        self._head=None
    def add_tail(self,val):
        node=Node(val)
        if self._head==None:
            self._head=node
        else:
            cur=self._head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
    def travel(self):
        cur=self._head
        while cur!=None:
            print(cur.val)
            cur=cur.next
            
    def f_tra(self):
        def tra(node):
            if node==None:
                return
            tra(node.next)
            print(node.val)
        tra(self._head)
class Node():
    def __init__(self,val=None):
        self.val=val
        self.left=None
        self.right=None
class Tree():
    def __init__(self):
        self.root=None
    def add_left(self,val):
        node=Node(val)
        if self.root==None:
            self.root=node
        else:
            node.left=self.root.left
            self.root.left=node
    def add_right(self,val):
        node=Node(val)
        if self.root==None:
            self.root=node
        else:
            node.right=self.root.right
            self.root.right=node
    def travel(self):
        def tra(node):
            if node ==None:
                return
            print(node.val)
            tra(node.left)
            tra(node.right)
        tra(self.root)

