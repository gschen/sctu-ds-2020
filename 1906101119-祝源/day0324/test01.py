class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None

class List:
    def __init__(self):
        #头节点
        self.head = Node(-1)
    #前插法创建单链表
    def insert_before(self,data):
        for i in data:
            node =Node(i)#创建新节点
            if self.head.next is None:
                self.head.next = node
            else:
                node.next = self.head.next
                self.head.next = node 

def insert_tail(self,data):

    tail = self.head.next

    for i in data:
        node =Node(i)

        if tail is None:
            self.head.next = node
            tail = node
        else:
            tail.next = node 
            tail = node

#尾插法创建单链表 
    def insert_tail(self,data): 
        tail = self.head.next 
        for i in data: 
            node = Node(i)#创建新节点 
 #判断下一节点是否为空 
            if tail is None:#如果为空 
                self.head.next = node 
                tail = node 
            else: 
                tail.next = node 
                tail = node 
#删除链表中的重复元素
def clear_repetition(self):
    cur=self.head
    while cur:#遍历元素
        while cur.next and cur.value==cur.next.value:#（判断节点的值与下一个节点的值是否相同）
            cur.next=cur.next.next#将指针指向下下个节点（删除元素）
        cur=cur.next


#在第i个节点前插入value的节点
def list_element_add(self,i,value):
    node_new=Node(value)#创建新节点
    index = 0
    node=self.head.next
    while node:#找位置
        index=index + 1
        if index == i-1:
            break
        node=node.next
        if node is None:
            return False
        node_new.next=node.next#插入节点
        node.next=node_new

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
