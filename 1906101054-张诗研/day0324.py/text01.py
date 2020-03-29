class Node:
    def __init__(self,value):
        self.value=value#当前节点的值
        self.next=None#下一个节点的值 


class List:
    def __init__(self)：
    #头节点
    self.head=Node(-1)

    #前插创建单链表
    def insert_before(self,data):
        for i in data:
            node =Node(i)
            if self.head.next is None:
                self.head.next=node
            else:
                node.next=self.head.next
                self.head.next=node
    

    #尾插法
    def insert__tail(self,data):
        tail=self.head.next

        for i in data:
            node=Node(i)
            
            if tail is None:
                self.head.next=node
                tail=node
            else:
                tail.next=node
                tail=node



    #删除重复元素
    def clear_repetition(self):
        cur=self.head
        while cur:
            while cur.next and cur.value==cur.next.value:
                cur.next=cur.next.next
            cur=cur.next


    #第i个节点前插入值
    def list_add(self,i,value):
        node_new=Node(value)
        index=0
        node=self.head.next
        while node:
            index=index+1
            if index==i-1:
                break
            node=node.next
        
        if node is None:
            return False
        
        node_new.next=node.next
        node.next=node_new
        