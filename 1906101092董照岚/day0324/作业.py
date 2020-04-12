# 给定一个不为空的链表，要求找到该链表的中间节点（若有两个中间值取第二个），然后输出中间值往后的链表
# 例如：[1，2，3，4，5]
# 输出：[3，4，5]

class Node:
    def __init__(self,value,*next):
        self.value=value
        self.next=None
class List:
    def __init__(self):
        self.head=Node(-1)

    def insert_before(self,date):
        for i in date:
            node=Node(i)
            if self.head.next is None:
                self.head.next=node
            else:
                node.next=self.head.next
                self.head.next=node

    def found_middle(self):
        h1=self.head
        n=0
        while h1.next!=None:#记录长度
            h1=h1.next
            n+=1
        n=n//2+1#中间节点位置

        h2=self.head
        for ii in range(n-1):#所找中间节点的前一个节点
            h2=h2.next
        self.head.next=h2.next#所找链表
        m=0
        h3=self.head
        while h3.next!=None:#记录结果长度
            h3=h3.next
            m+=1
        print(m)
x=List()
x.insert_before([1,2,3,4,5])
x.found_middle()