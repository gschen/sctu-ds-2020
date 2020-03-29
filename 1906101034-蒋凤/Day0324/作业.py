class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkNode():
    def __init__(self):
        self.head = Node(-1)
    def insert_tail(self,date):#尾插法
        tail = self.head.next
        for i in date:
            node = Node(i)
            if tail is None:#判断头节点的下一个结点是否为空
                self.head.next = node
                tail = node
            else:
                tail.next = node#头节点的下一个结点不为空，在最后一个结点的下一个结点加入node
                tail = node
#创建一个链表
a = LinkNode()
l = list(map(int,input().split()))
a.insert_tail(l)
p = a.head
res = []
count = 0
while p.next != None:#当p.next=None时，res中已经追加了最后一个结点，因为每一次都是追加的p.next
    p = p.next
    res.append(p.value)
    count += 1
print(res[count//2:])
