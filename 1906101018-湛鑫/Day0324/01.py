class List:
    def __init__(self):
        # 头结点
        self.value = value
        self.next = None


class List:
    def __init__(self):
        # 头结点
        self.head = None(-1)
        # 前插法创建单链表
    def insert_before(self,data):
        for i in data:
            node = Node(i)#创建新节点
            #判断头节点的下一个节点是否为空
            if self.head.next is None:#如果为空，则将新节点加入到next
                self.head.next = node
            else:
                node.next = self.head.next#将头节点的下一个节点加入当前节点的next
                self.head.next = node