class Node:
    def __init__(self,value):
        self.value = value
        self.next = None 
class List:
    def __init__(self):
        #头节点
        self.head = Node(-1)
    def insert_before(self,date):#通过头插法创建一个单列表
        for i in date:
            node = Node(i)#创建新节点
        if self.head.next is None:
            self.head.next = node
        else:
            node.next = self.head.next
            self.head.next = node
    def insert_tail(self,date):
        tail = self.head.next
        for i in date:
            node = Node(i)

            if tail is None:
                self.head.next = node
                tail = node
            else:
                tail.next = node
                tail = node
    def clnear(self):#删除重复节点
        cur = self.head
        while cur:
            while cur.next and cur.value == cur.next.value:#判断头节点的下一个节点的值是否与下下一个节点的值相同
                cur.next = cur.next.next#删除下下给节点
            cur = cur.next
    def list_element_add(self,i,value):
        node_new = Node(value)#创建一个新节点
        index = 0
        node = self.head.next
        while node:#找要插入的位置
            index += 1
            if index == i-1:
                break
            node = node.next
        if node is Node:
            return False
        node_new.next = node.next#插入新节点
        node.next = node_new
        