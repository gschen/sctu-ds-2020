class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

class SingleLink():
    def __init__(self,node=None):
        self.head = node
    
    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False
        return self.head==None

    def add_tail(self,value):
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur=cur.next
            cur.next = node

    def find_mid(self):
        count = -1
        lis = []
        cur = self.head
        while cur.next != None:
            count += 1
            cur = cur.next
            lis.append(cur.val)
        return lis[(count//2):]

if __name__ == '__main__': 
    sl=SingleLink()
    sl.add_tail(1)
    sl.add_tail(2)
    sl.add_tail(3)
    sl.add_tail(4)
    sl.add_tail(5)
    print(sl.find_mid())

    