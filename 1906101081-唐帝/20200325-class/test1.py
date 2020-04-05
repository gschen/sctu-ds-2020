class Node:
    def __init__(self,value):
        self.value=value# 当前节点的值
        self.next=None #下一个节点
class List:
    def __init__(self):
        #头节点
        self.head=Node(-1)
        # 前插法创建单链表
    def insert_before(self,data):
        for i in data:
            node=Node(i)# 创建新节点
            # 判断头节点的下一个节点是否为空
        if self.head.next is None:# 如果为空，则讲新节点加入next
            self.head.next=node
        else:
            node.next=self.head.next#将头节点的下一个节点添加到当前节点
            self.head.next=node

     # 尾插法创造单链表
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

#。.