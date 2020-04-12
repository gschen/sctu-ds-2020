class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class Link():
    def __init__(self):
        self.head = Node(-1)
    def insert_tail(self,date):#尾插法
        tail = self.head.next
        for i in date:
            node = Node(i)
            if tail is None:
                self.head.next = node
                tail = node
            else:
                tail.next = node#头节点的下一个结点不为空，在最后一个结点的下一个结点加入node
                tail = node
#创建一个链表
a = Link()
l = list(map(int,input().split()))
a.insert_tail(l)

p = a.head
res = []
count = 0
while p.next != None:
    p = p.next
    res.append(p.value)
    count += 1
print(res[count//2:])