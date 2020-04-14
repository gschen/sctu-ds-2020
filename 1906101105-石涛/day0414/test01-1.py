# coding=utf-8

# n=eval(input())
# def fib(a=1,b=1,k=2):
#     if k>=n:
#         return b
#     return fib(b,a+b,k+1)

# def fib(n):
#     if n==1 or n==2:
#         return 1
#     return fib(n-1)+fib(n-2)
# print(fib(7))


class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

class SingleLink():
    def __init__(self):
        self.__head=None
    def add_tail(self,val):
        node=Node(val)
        if self.__head==None:
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
    def travel(self):
        cur=self.__head
        while cur!=None:
            print(cur.val)
            cur=cur.next
    def f_tra(self):
        def tra(node):
            if node==None:
                return
            tra(node.next)
            print(node.val)
        tra(self.__head)

a=SingleLink()
a.add_tail(1)
a.add_tail(2)
a.add_tail(3)
a.travel()
a.f_tra()