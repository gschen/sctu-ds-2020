class Node():
    def __init__(self,value):
        self.elem = value
        self.next = None

class List():
    def __init__(self,node=None):
        self.head = node
    def length(self):
        cur=self.head
        self.count=0
        while cur != None:
            self.count+=1
            cur = cur.next
        return self.count

    def add(self,value):
        node = Node(value)
        node.next=self.head
        self.head=node
    def tavel(self):
        l = []
        cur = self.head
        while cur != None:
            
            l.append(cur.elem)
            cur = cur.next
        print(l)
        if self.count%2 == 0:
            s = int(self.count/2)
            return (l[s:])
        if self.count%2 != 0:
            x = int((self.count-1)/2)
            return (l[x:])
            
if __name__ == "__main__":
    sl=List()
    sl.add(20)
    sl.add(10)
    sl.add(30)
    sl.add(50)
    sl.add(5)
    sl.length()
    print(sl.tavel())
