n=eval(input())
def fib(a=1,b=1,k=2):
    if k==n:
        return b
    return fib(b,a+b,k+1)

def fib(n):
    if n==1 or n==2:
        retrun 1
    retrun fib(n-1)+fib(n-2)
print(fib(5))

class Node():
    def __init__(self,val=None):
        self.val=val
        self.next=None
class SingleLink():
    def __init__(self):
        self._head=None
    def add_tail(self,val):
        node=None(val)
        if self._head==Node:
            self._gead=node
        else:
            cur=self._head
            while  cur.next!=None:
                cur=cur.next
            cur.next=node
    def travel(self):
        cur=self._head
        while cur!=None:
            print(cur.val)
            cur=cur.next
    def f_tar(self):
        def tra(node):
            if node==None:
                return 
            tra(node.next)
            print(node.val)
        tra(self._head)
a=SingleLink()
a.add_tail(10)

