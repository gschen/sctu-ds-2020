class Node:
    def _init_(self,value):
        self.value=value
        self.next=None
class List:
#创建头节点
    def _init_(self):
        self.head=Node(-1)


#使用前插法创建单链列表
    def insert_before(self,data):
        for i in data:
            node=Node(i)#创建新节点
            #判断头节点的下一个节点是否为空·
            if self.head.next is None:#如果为空，则将新节点加入next
                self.head.next=node
            else:
                node.next=self.head.next#将头节点的下一个节点加入当前节点的next
                self.head.next=node



#尾插法
def insert_tail(self,data):
    tail=self.head.next
    for i in data:
        node=Node(i)
        if tail is None:
            self.head.next=node
            tail=node
        else:
            tail.next=node
            tail=node

