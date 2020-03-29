class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkNode():
    def __init__(self):
        self.head = Node(-1)
    def insert_tail(self,date):
        tail = self.head.next
        for i in date:
            node = Node(i)
            if tail is None:
                self.head.next = node
                tail = node
            else:
                tail.next = node
                tail = node
a = LinkNode()
l = list(map(int,input().split()))
a.insert_tail(l)
p = a.head
res = []
count = 0
while p.next != None:
    p = p.next
    res.append(p)#.value)
    count += 1
print(res[count//2:])
