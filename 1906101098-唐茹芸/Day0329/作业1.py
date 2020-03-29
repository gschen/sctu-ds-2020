class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

    def length(self):
        cur=self.__head
        count=0
        while cur.next!=None:
            count+=1
            cur=cur.next
        return count
n1 = Node('n1',None)
n2 = Node('n2',n1)
n3 = Node('n3',n2)
n4 = Node('n4',n3)
n5 = Node('n5',n4)

p1 = n5
p2 = n5
while p2.next is not None and p2.next.next is not None:
    p1 = p1.next
    p2 = p2.next.next
print p1.data
    
    def clear(self):
        p1.next=p1.data
    return
    
    def PrintList(self):
        if self.length ==0:
            return None
        else:
            p = self.head
            while p.next:
                print(p.data,'-->',end = '')
                p = p.next
            print(p.data)


    
    
    
    
    
    