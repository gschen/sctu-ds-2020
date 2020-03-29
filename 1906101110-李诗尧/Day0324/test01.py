class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class List:
    def __init__(self):
        #头节点
        self.head=Node(-1)
    #前插法创建单链表
    def insert_before(self,date):
        for i in date:
            node=Node(i)#创建新节点
            #判断头节点的下一个节点是否为空
            if self.head.next is None:  #如果为空，则将新节点加入到next
                self.head.next=node
            else:
                node.next=self.head.next #将头节点的下一个节点加入到当前节点的next
                self.head.next=node
    #尾插法创建单链表
    def insert_tail(self,date):
        tail=self.head.next   #将头结点存储在tail里
         
        for i in date:
            node=Node(i)
            #判断头节点的下一个节点是否为空
            if tail is None:
                self.head.next=node
                tail=node      #tail就变了
            else:
                tail.next=node   #没有为空，就将头节点的下个节点加入到当前节点的next
                tail=node

    #删除链表中重复元素
    def clear_repetitiong(self):
        cur=self.head
        while cur: #循环遍历
            while cur.next and cur.value==cur.next.value:   #当head后面有下一个节点，判断头节点与下一个节点的值
                cur.next=cur.next.next  #相同的进行删除，直到不再相同
            cur=cur.next
    #在第i个节点前插入值为value的节点
    def list_element_add(self,i,value):
        node_new=Node(value)#创建新的节点
        index=0
        node=self.head.next  #head本身不存在节点里，
        while node:#找位置
            index=index+1
            if index==i-1:
                break
            node=node.next
        if node is None:
            return False
        node_new.next=node.next#插入节点
        node.next=node_new
        