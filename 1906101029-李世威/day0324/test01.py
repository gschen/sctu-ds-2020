class Node:
    def __init__(self):
        self.value=value
        self.next=None

class List:
    def __init__(self):
        self.head = Node(-1)
#头插法
    def insert_before(self,data):
        for i in data:
            node = Node(i)
            if self.head.next is None:
                self.head.next = node
            else:
                node.next = self.head.next
                self.head.next = node
#尾插法
    def insert_tail(self,data):
        tail=self.head.next
        for i in data:
            node = Node(i)
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
            node = node.next
        print('')
#删除链表中的重复元素
    def clear_repetition(self):
        cur=self.head
        while cur:
            while cur.next and cur.value==cur.next.value:
                cur.next=cur.next.next
                cur=cur.next

#在第i个节点插入值为value的节点
    def list_element_add(self,i,value):
        node_new = Node(value)
        index = 0
        node self.head.next
        while node:
            index = index +1
            if index == i-1:
                break
            node = node.next
        if node is None:
            return False
        node_new.next=node.next
        node.next=node_new