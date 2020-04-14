class Node():
    def __init__(self,val):
        self.elem = val
        self.next = None

class SigleLink():
    def __init__(self,node=None):
        self.__head = node
    def add_tail(self,val):
        node = Node(val)
        cur = self.__head
        while cur.next!= None:
            cur = cur.next
        cur.next = node
    def Length(self):
        cur = self.__head
        count = 0
        while cur!=None:
            count += 1
            cur = cur.next 
        return count
    def print_middle(self):
        cur = cur.next 
        if len(Length()) % 2 ==0:




if __name__ =='__main__':
    a=SigleLink()
    a.add_tail(1)
    print(a.print_middle())
