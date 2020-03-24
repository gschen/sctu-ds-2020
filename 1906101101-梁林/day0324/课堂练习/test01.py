class Node:
    sef __init__(self,)
    self.value=value
    self.next=None
class List:
    def __init__(self):
        self.head=Node(-1)
    def insert_before(self,date):
        for i in date:
            node=Node(i)
            if self.head.next is None:
                self.head.next=node
            else:
                node.next=self.head.next
                self.head.next=node


    def insert__tail(self,date):
        tail=self.heaad.next
        for i in date:
            node=Node(i)
            if tail is Node:
                self.head.next=node
                tail=node
            else:
                tail.next=node
                tail=node