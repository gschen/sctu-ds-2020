class node:
    def  __init__(self,value):
        self.value=value
        self.next=none 
class list:
    def __init__(self):
        self.head=node(-1)
    def insert_before(self,data):
        for i in data:
            node=node(i)
            if self.head.next is none:
                self.head.next=node
            else:
                node.next=self.head.next
                self.head.next=node
    def insert_tail(self,data):
        tail=self.head.next
        for i in data:
            node=node(i)
            if tail is none :
                self.head.next=node
                tail=node
            else:
                tail.next=node
                tail=node
    # 删除重复元素
    def clear_repetition(self):
        cur=self.head
        while cur:
            while cur.next and cue.value==cur.next.value:
                cur.next=cur.next.next
            cur=cur.next
    # 在i个节点前插入
    def list_element_add(self,i,value):
        node_new=node(value)    #新建节点
        index=0
        node=self.head.next
        while node : #找位置
            index=index+1
            if index==i-1:
                break
            node = node.next
            if node is None:
                return
            node_new.next=node.next #插入新节点
            node.next = node_new