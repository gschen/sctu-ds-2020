"""
n=eval(input())
def fib(a=1,b=1,k=2):
    if k==n:
        return b
    return fib(b,a+b,k+1)

print(fib())


def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))

"""


class Node():
    def __init__(self,val=Node):
        self.val=val
        self.next=Node

class SingleLink():
    def __init__(self):
        self._head=Node
    def add_tail(self,val):
        node=Node(val)

        if self._head==Node:
            self._head=node
        else:
            cur=self._head
            while cur.next!=Node:
                cur=cur.next
            cur.next=node


def travel(self):
    cur=self._head
    while cur!=Node:
        print(cur.val)
        cur=cur

def f_tra(self):
    def tra(node):
        if node==Node:
            return
            tra(node.next)
            print(node.val)
        tra(self._head)

a=SingleLink()
a.add_tail(10)
a.add_tail(20)


1