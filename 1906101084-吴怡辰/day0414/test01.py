'''
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(5))
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SingleLink:
    def __init__(self):
        self.head = None
    
    def add_tail(self,val):
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    def travel(self):
        cur = self.head
        while cur != None:
            print(cur.val)
            cur = cur.next

    def f_tra(self,val):
        def tra(node):
            if node == None:
                return
            tra(node.next)
            print(node.val)
        tra(self.head)

a=SingleLink()
a.add_tail(10)
a.add_tail(20)
a.add_tail(30)
a.add_tail(40)
a.add_tail(50)
a.travel()

