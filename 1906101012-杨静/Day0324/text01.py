class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None


class List():
    def __init__(self):
        #头结点
        self.head=Node(-1)
    #头插法创建单链表
    def insert_before(self,data):
        for i in data:
            node=Node(i)#创建新结点
            #判断头结点的下一个结点是否为空
            if self.head.next is None:#如果为空，则将新结点加入到next
                self.head.next=node
            else:
                node.next=self.head.next#将头结点的下一个结点加入到当前结点的next
                self.head.next=node


    #从尾部插入元素    
    def insert_tail(self,data):
        #尾结点
        tail=self.head.next

        for i in data:
            node=Node(i)#创建新结点
            #判断尾结点是否为空
            if tail is None:#如果为空，则将新结点加入到next
                self.head.next=node
                tail=node
            else:
                tail.next=node#将新结点加入到尾结点的next
                tail=node


    #删除链表中重复元素
    def clear_repetition(self):
        #头结点
        cur=self.head
        while cur:
            while cur.next and cur.value==cur.next.value:#当前结点下一个结点不为空并且头结点的值与next的值是否相等
                cur.next=cur.next.next#将当前结点链接到当前结点的next.next
            cur=cur.next


    #第i个结点前插入值为value的结点
    def list_element_add(self,i,value):

        node_new=Node(value)#创建新结点

        index=0

        node=self.head.next

        while node:#找位置
            index=index+1

            if index==i-1:
                break

            node=node.next   

        if node is Node:
            return False

        node_new.next=node.next#插入结点
        node.next=node_new