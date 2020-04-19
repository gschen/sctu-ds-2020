n = eval(input())
def fib(a=1,b=1,k=2):
    if k==n:
        return b
    return fib(a=b,b=a+b,k=k+1)


def fib1(n):
    if n==1 or n==2:
        return 1
    return fib1(n-1)+fib1(n-2)

class Node():
    def __init__(self,val):
        self.data=val
        self.next=None

class SingleLink():
    def __init__(self):
        self._head=None
    def add_tail(self ,val):
        node=Node(val)
        if self._head==None:
            self._head=node
        else:
            cur=self._head
            while cur.next!=None:
                cur=cur. next
            cur.next=node
    def travel(self):
        cur=self.head
        while cur!=None:
            print( cur. val )
            cur=cur . next
    def f_tra(se1f):
        def tra( node) :
            if node==None:
                return
            tra(node.next)
            print(node.val)
        tra(se1f._head)
