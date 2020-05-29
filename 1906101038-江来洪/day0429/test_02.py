class Node(object):#定义一个节点类
    def __init__(self,data):
        self.val = data
        self.next = None
class ListNode():#定义一个链表类
    def __init__(self,node = None):
        self.head = Node(node)
    def insert(self,list):#尾插法创建链表
        tail = self.head
        for i in list:
            node = Node(i)
            if self.head == None:
                self.head.next = node
                tail = node
            else:
                tail.next = node
                tail = node
link = ListNode()
link.insert([1,2,3,4])#创建链表
#将链表转化为列表
res = []
p = link.head
while p.next:#遍历链表每一个节点
    p = p.next
    res.append(p.val)#将值添加进res
print(res)

