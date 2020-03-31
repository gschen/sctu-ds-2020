class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkNode():
    def __init__(self):
        self.head = Node(-1)
    def insert_tail(self,date):
        for i in date:
            node = Node(i)
            if tail is None:
                self.head.next = node
                tail = node
            else:
                tail.next = node
                tail = node