class Node():
    def __init__(self,val=None):
        self.val=val
        self.next=None

class SingleLink():
    def __init__(self):
        self.head=None
    def add_tail(self,val):
        node=Node(val)

        if self.head==None:
            self.head=node
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

    def travel(self):
        cur=self.head
        while cur!=None:
            print(cur.val)
            cur=cur.next


    def f_tra(self):
        def  tra(node):
            if node==None:
                return
            print(node.val)
            tra(node.next)
        tra(self.head)
    



a=SingleLink()
a.add_tail(1)
a.add_tail(2)
a.add_tail(3)
a.travel()
a.f_tra