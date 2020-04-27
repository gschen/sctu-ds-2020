# coding=utf-8

'''链表二（续上周）'''

'''
    这是之后的代码
'''
class Node(): # 这是一个结点类
    def __init__(self,value):
        self.value=value
        self.next=None

class List:
    def __init__(self):
        # 结点头
        self.head=Node(-1)

    # 头插法
    def insert_before(self,data):
        for i in data:
            node=Node(i) #创建新结点
            if self.head.next is None: # 判断头结点的下一个结点是否为空，如果为空，则将新结点加入到next
                self.head.next=node
            else:
                node.next=self.head.next # 将头结点的下一个结点加入到当前结点的next
                self.head.next=node

    # 尾插法
    def insert_tail(self,data):
        tail=self.head.next
        for i in data:
            node=Node(i)
            if tail is None: # 判断头结点之后是否为None
                self.head.next=node # 直接后面连上链表吧
                tail=node
            else: # 不为None时就找到最后，连上这个
                tail.next=node
                tail=node

    # 打印单链表
    def list_print(self):
        node=self.head.next
        while node:
            print(node.value,end=' ')
            node=node.next # 配合while循环进行遍历
        print()

    # 删除链表中重复元素
    def clear_repetition(self):
        cur=self.head
        while cur: # 循环遍历
            while cur.next and cur.value==cur.next.value:
                cur.next=cur.next.next # 重复便进行删除，while不断循环删除
            cur=cur.next # 帮助以上遍历后面的

    # 在i个结点插入元素
    def list_element_add(self,i,value):
        node_new=Node(value) # 创建新结点
        index=0
        node=self.head.next
        while node: # 找位置
            index+=1
            if index==i-1: # 找到需要插入的位置
                break
            node=node.next
        if node is None: # 位置是否存在
            return False
        node_new.next=node.next # 插入结点
        node.next=node_new