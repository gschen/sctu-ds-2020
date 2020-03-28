class Node:
    sef __init__(self,)
    self.value=value
    self.next=None
class List:
    def __init__(self):
        self.head=Node(-1)





    #头插
    def insert_before(self,date):
        for i in date:
            node=Node(i)
            if self.head.next is None:
                self.head.next=node
            else:
                node.next=self.head.next
                self.head.next=node





    #尾插
    def insert__tail(self,date):
        tail=self.heaad.next
        for i in date:
            node=Node(i)
            if tail is Node:
                self.head.next=node
                tail=node#记录每一次最后元素，方便下一次链接
            else:
                tail.next=node
                tail=node




    #删除重复元素
    def clear_repetition(self):
        cur=self.head
        while cur:
            while cur.next and cur.value==cur.next.value:#重复进下一个节点
                cur.next=cur.next.next
            cur=cur.next



            

    #在i前插入新节点
    def list_element_add(self,i,value):
        node_new=Node(value)#新建新节点
        index=0
        node=self.head.next
        while node:
            index+=1
            if index==i-1:#找到i-1节点
                break
            node=node.next
        if node is Node:
            return False
        
        node_new.next=node.next#新建链接
        node.next=node_new