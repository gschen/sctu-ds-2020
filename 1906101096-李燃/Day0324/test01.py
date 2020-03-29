
#创建节点的类
class Node:
    def __init__(self,value):
        self.value=value  #当前节点的值
        self.next=None    #下一个节点



class List:
    def __init__(self):
        #头节点
        self.head =Node(-1)
    #前插法创建单链表
    def insert_before(self,data):
        for i in data:
            node=Node(i)#创建节点

            #判断头节点的下一节点是否为空
            if self.head.next is None:  #如果为空，则将新节点加入到next
                self.head.head=node
            else:
                node.head=self.head.next  #将头节点的下一个节点加入到当前节点的next
                self.head.next=node



# 尾插法创建列表
def insert_tail(self,data):
    tail=self.head.next
    
    for i in data:
        node= Node(i)

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
    prinit('')

#删除链表中重复的元素
 def clear_reperition(self):
        cur=self.head
        while cur:#循环遍历
            while cur.next and cur.value==cur.next.value:#判断头节点的值与下一节点的值是否相同
                cur.next=cur.next.next#删除元素
                cur=cur.next#帮助遍历后面的

    
    
    # 第i个节点前插入值为value的节点
    def list_element_add(self, i, value):
        node_new = Node(value)#创建新节点
        index = 0
        node=self.head.next
        while node:#找位置
            index = index + i
            if index == i - 1:
                break
            node = node.next
        if node is None:
            return False
        node_new.next + node.next#插入新节点
        node.next = node_new





