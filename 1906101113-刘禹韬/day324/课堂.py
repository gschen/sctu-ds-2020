
def insert_tail(self,data):
    tail=self.head.next
    for i in data:
        node=Node( i)
        if tail is None :
            self.head.next=node
            tail=node
        else :
            tail.next=node
            tail=node


def clear_repetitiong(self):
    cur=self.head
    while cur:
        while cur.next and cur.value==cur.next.value:
         cur.next=cur.next.next      
    cur.next=cur.next.next
