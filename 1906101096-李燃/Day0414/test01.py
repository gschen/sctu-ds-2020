#递归
# 
# n=eval(input())
# def fib(a=1,b=1,k=2):
#     if k==n:
#         return b
#     return fib(b,b+a,k+1)

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(5))

#链表

class Node():
    def __init__(self,val=None):
        self.val=val
        self.next=None

class SingleLink():
    def __init__(self):
        self._head=None
        
    def add_tail(self,val):  #尾插法
        node=Node(val)

        if self._head==None: #判断是否为空，为空就返回头节点
            self._head=node

        else:
            cur=self._head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

    def travel(self):
        cur=self._head
        while cur.next!=None:
            print(cur.next)
            cur=cur.next


    def f_tra(self):
        def tra(node):
            if node==None:
                return
            
            tra(node.next)
            print(node.val)
        tra(self._head)




a=SingleLink()
a.add_tail(10)
a.add_tail(20)
a.add_tail(30)
a.travel()
a.f_tra()
            