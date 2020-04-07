class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class List:
    def __init__(self):
        #头节点
        self.head = Node(-1)
    # 头插法创建单链表
    def insert_before(self,data):
        for i in data:
            node = Node(i) #创建新节点
            #判头节点的下一个节点是否为空
            if self.head.next == None:
                self.head.next = node
            else:
                node.next = self.head.next
                self.head.next = node
    # 尾插法创建单链表
    def insert_tail(self,data):
        tail = self.head.next
        for i in data:
            node = Node(i)
            if tail is None:
                self.head.next = node
                tail = node
            else:
                tail.next = node
                tail = node

    # 删除链表重复项
    def del_item(self):
        cur = self.head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur.next == cur.next.next
            cur = cur.next #遍历所有节点

    # 第i个节点后面插入一个新节点的值value
    def list_add(self,i,val):
        node_new = Node(val)
        index = 0
        node = self.head.next
        while node:
            index += 1
            if index == i-1:
                break
            node = node.next
        if node is None:
            return False
        node_new.next = node.next
        node.next = node_new

