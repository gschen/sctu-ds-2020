class Node:
    def __init__(self,value):
        self.value = value
        self.next = Node
class List:
    def__init__(self):
        self.head = Node(-1)
    def insert_before(self,data):
        for i in data:
            node = Node(i)
            if self.head.next = node 
        else:
            node.next = self.head.next
            self.head.next = node

def insert_tail(self.data):
    tail = self.head.next
    for i in data:
        node = Node(i)
        if tail is Node:
            self.head.next = node
            tail = node
        else:
            tail.next = node
            tail = node

def clear_repetition(self):
    cur=self.head
    while cur:
        while cur.next and cur.value==cur.next.value:  #判断是否重复
            cur.next=cur.next.next
        cur=cur.next

def list_element_add(self,i,value):
    node_new = Node(value)
    index = 0
    node = self.head.next
    while node:
        index = =index + 1
        if index == i - 1:
            break
        node = node.next

        if node is None:
            return False

        node_new.next = node.next
        node.next = node_new

