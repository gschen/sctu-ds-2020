#斐波拉契数列
n=eval(input())
'''
def fib(a=1,b=1,k=2):
    if k==n:
        return b
    return fib(b,a+b,k+1)
print(fib())
'''

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))
class SingleLink():
    def __init__(self):
        self._head=None
    def add_tail(self,val):
        node=Node(val)
        if self._head==None:
            self._head=node
        else:
            cur=self._head
            while cur.next != None:
                cur=cur.next
            cur.next=node

    def travel(self):
        cur=self._head
        while cur != None:
            print(cur.val)
            cur=cur.next
    def f_tra(node):
        if node==None:
            return
        print(node,val)
        tra(node.next)


a=SingleLink()
a.add_tail(10)
a.add_tail(20)
a.add_tail(30)
a.travel()