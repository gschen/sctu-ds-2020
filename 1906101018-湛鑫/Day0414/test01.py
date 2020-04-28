#n=eval(input())
#def fib(a=1,b=1,k=2):
#   if k==n:
#        return b
#    return fib(b,a+b,k+1)

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(5))

class Node():
    def __init__(self,val=None):
        self.val=val
        self.next=None

class SingleLink():
    def __init__(self):
        self._head=None
    def add_tail(self,val):
        node=Node(val)

        if self._head==None:
            self._head=node
        else:
            cur=self._head
            while cur.next !=None:
                cur=cur.next
            cur.next=node

    def travel(self):
        cur=self._head
        while cur !=None:
            print(cur.val)
            cur=cur

    def f_tra(self):

        def tra(node):
            if node==None:
                return 
            tra(node.next)
            print(node.val)