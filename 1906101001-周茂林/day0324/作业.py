class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkNode():
    def __init__(self):
        self.head = Node(-1)

    def insert_tail(self, date):
        tail = self.head.next
        for i in date:
            node = Node(i)
            #判断头节点的下一个结点是否为空
            if tail is None:
                self.head.next = node
                tail = node
            else:
                #头节点的下一个结点不为空，在最后一个结点的下一个结点加入node
                tail.next = node
                tail = node

#创建一个链表
a = LinkNode()
l = list(map(int, input().split()))
a.insert_tail(l)
p = a.head
res = []
count = 0

while p.next != None:
    p = p.next
    res.append(p.value)
    count += 1
print(res[count//2:])