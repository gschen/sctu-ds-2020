class Node():
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Siglelink():
    def seek(self,head):
        if head is None:
            return None
        needle1=needle2=head
        while needle2 and needle2.next:
            needle1=needle1.next
            needle2=needle2.next.next
        while needle2==None and needle2==None:
            needle1=needle1.next
            print(needle1.data,end='')
        return ''