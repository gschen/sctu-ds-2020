class Node():
    def __init__(self,value)
        self.value=Value
        self.next=Node

class List:
    def __init__(self):
        self.head=Node(-1)
    #前插法创建单链表
    def insert_before(self,date):
        for i in date:
            node=Node(i)
            if self.head.next is None:
                self.head.next=node
            else:
                node.next=self.head.next
                self.head.next=node


#尾插法

def insert_tail(self,date):
    tail=self.head.next
    for i in date:
        node=Node(i)
        if tail is None:
          self.head.next=node
          tail=node
        else:
            tail.next=node
            tail=node


#删除相同的元素

def clear_repetition(self):
    cur=self.head
    while cur:
        while cur.next and cur.value==cur.next.value:
            cur.next=cur.next.next
        cur=cur.next




#第i个节点前插入值为value的节点
def list_element_add(self,i,value):
    node_new=Node(value)创建节点
    index=0
    node=self.head.next
    while node:#找位置
        index==i+1
        if index==i-1
        break
        node=node.next
    if node is Node:
        return False
    node_new.next=node.next#插入节点
    node.next=node_new
1