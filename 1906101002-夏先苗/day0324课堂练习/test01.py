class Node:
    def __init__(self,value):
        self.value=value#当前节点的值
        self.next=None#下一个节点

class List():
    def __init__(self):
        #头节点
        self.head=Node(-1)
    #前插法创建单链表
    def insert_before(self,data):
        for i in data:
            node=Node(i)#创建新节点
            #判断头节点的下一个节点是否为空
            if self.head.next is None:#如果为空，则将新节点加入next
                self.head.next=node
            else:
                node.next=self.head.next#将头节点的下一个节点添加到当前节点
                self.head.next=node

    #用尾插法创造单链表
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
    #打印单链表
    def list_print(self):
        node=self.head.next
        while node:
            print(node.value,' ',end='')
            node=node.next
        print('')

    #删除链表中重复元素
    def clear_repetition(self):
        cur=self.head
        while cur:
            while cur.next and cur.value==cur.next.value:
                cur.next=cur.next.next#重复便进行删除，while不断循环删除
            cur=cur.next#处于第一个循环内，已经循环了全部
    
    def list_element_add(self,i,value):
        node_new = Node(value)#创建新节点
        index=0
        node=self.head.next
        while node:#找位置
            index=index+1
            if index==i-1:
                break
            node=node.next
        if node is None:
            return False
        node_new.next=node.next
        node.next=node_new
