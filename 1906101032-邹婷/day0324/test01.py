class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class List:
    def __init__(self):
        #头节点
        self.head=Node(-1)
        #前插法创建单链表
    def insert_before(self,data):
        for i in data:
            node=Node(i)#创建新节点
            if self.head.next is None:#如果为空，则将新节点加入到next
                self.head.next=node
            else:
                node.next=self.head.next#将头节点的下一个节点加入到当前节点的next
                self.head.next=node
#尾插法
def insert_before(self,data):
    tail=self.head.next#相当于指针
    for i in data:
        node=Node(i)
        if tail is None:
            self.head.next=node
            tail=node#指向新的节点
        else:
            tail.next=node
            tail=node
#删除链表中重复元素
def clear_repetition(self):
    cur=self.head
    while cur:
        while cur.next and cur.value == cur.next.next.value:
            cur.next=cur.next.next#每个节点都与后面所有的节点做对比
        cur=cur.next#处于第一个循环内，已经循环了全部
#在第i给节点前插入值为value的节点
def list_element(self,i,value):
    node_new=Node(value)
    index=0#插入点
    node=self.head.next#将头节点避开
    while node:
        index=index+1
        if index == i-1:
            break
        node=node.next
    if node is None:
        return False
    node_new.next=node.next#插入节点
    node.next=node_new

    
 