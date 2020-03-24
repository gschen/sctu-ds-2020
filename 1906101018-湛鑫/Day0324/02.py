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