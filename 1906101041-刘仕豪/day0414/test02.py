class Node():
    def __int__(self,val=None):
        self.val = val
        self.next = None

class Singlelink():
    def __init__(self):
        self._head = None
    def add_tail(self,val):
        node = Node(val)

        if self._head==None:
            self._head = node
        else:
            cur = self._head
            while cur.next!=None:
                cur = cur.next
            cur.next = node

    def travel(self):
        cur = self._head
        while cur!=None:
            print(cur.val)
            cur = cur.next


    def f_tra(self):
        def tra(node):
            if node==None:
                return
            print(node.val)
            tra(node.next)
        tra(self._head)


a = Singlelink()
a.add_tail(10)
a.add_tail(20)
a.add_tail(30)
