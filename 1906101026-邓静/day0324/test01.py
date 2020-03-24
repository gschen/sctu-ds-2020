class Node():
    def __init__(self,val):
        self.elem=val
        self.next=Node
class List:
    def __init__(self):
        #头结点
        self.head=Node(-1)
    #前段法创建单链表
    def insert_before(self,data):
        for i in data:
            node=Node(i)#创建新节点
            #判断头结点的下一个节点是否为空
            if self.head.next is Node:#如果为空，则将新节点
                self.head.next=node
            else:
                node.next=self.head.next#讲头结点的下一个节点加入到当前节点的
                self.head.next=node
    #尾插法
    def insert_tail(self,data):
        tail=self.head.next
        for i in data:
            node=Node(i)
            if tail is Node:
                self.head.next=node
                tail=node
            else:
                tail.next=node
                tail=node

                
                