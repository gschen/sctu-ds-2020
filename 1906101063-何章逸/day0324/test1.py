class Node:

    def __init__(self,value):
        self.value=value
        self.next=None

class List:
    def __init__(self):
        #头结点
        self.head=Node(-1)
    #头茶法创建单链表
    def insert_before(self,data):
        for i in data:
            node=Node(i)#创建新节点

            if self.haed.next is None:#如果为空，则将新节点加到next
                self.head.next = node
            else:
                node.next = self.head.next
                self.head.next = node

        #尾插发
    def insert_tail(self,data):

        tail=self.head.next

        for i in data:
            node = Node(i)

            if tail is None:
                self.head.next=node
                tail = node
            else:
                tail.next = node 
                tail = node

    #打印单链表
    def list_print(self):
        node=self.head.next

        while node:
            print(node.value,' ',end='')
            node = node.next
        print('')
        #删除重复元素
        def clear_repetition(self):
            cur=self.head
            while cur:
                while cur.next and cur.value == cur.next.value:
                    cur.next=cur.next.next
                cur=cur.next
        #找链表中间节点











        #第一个节点前插入值为value的节点

        def list_element_aad(self,i,value):

            node_new = Node(value)#创建节点
            index=0
            node=self.head.next

            while node:#找位置
                index=index+1

                if index  == i-1:
                    break

                node=node.next

            if node is None:
                return False

            node_new.next=node.next#插入节点
            node.next=node_new
            