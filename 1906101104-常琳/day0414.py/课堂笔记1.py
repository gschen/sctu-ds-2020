#用递归实现斐波拉契数列：
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(5))

#用单链表实现：
class Node():
    def __init__(self,val=None):
        self.val=val
        self.next=None
class singlelink():
    def __init__(self):
        self._head=None
    def add_tail(self,val):
        node=Node(val)
        if self._head==None:
            self._head=node
        else:
            cur=self._head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
    def travel(self):
        cur=self._head
        while cur!=None:
            print(cur.val)
            cur=cur.next
    def f_tra(self):
        def tra(node):
            print(node.val)
            tra(node.next)
        tra(self._head)
a=singlelink()
a.add_tail(10)
a.add_tail(20)
a.add_tail(30)
a.travel()


#树：
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
            if node == None:
                return
            print(node.val)
            tra(node.left)
            tra(node.right)
        tra(self.root)

s=tree()
s.add_left(3)
s.add_left(2)
s.add_right(4)
s.add_right(1)
s.travel()