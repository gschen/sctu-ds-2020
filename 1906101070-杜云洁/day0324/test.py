class Node():
    def __init__(self,value):
        self.value=value#当前节点的值
        self.next=next#下一个节点

class List:
    def __init__(self):
        #头节点
        self.head=Node(-1)
    #前插法创建单链表：用当前节点的next去连接上一个节点。
    def insert_before(self,data):
        for i in data:
            node=Node(i)#创建新节点
            #判断头节点的下一个节点是否为空
            if self.head.next is None:#如果为空，则将新节点加入到next
                self.head.next=node
            else:
                node.next=self.head.next#将头节点的下一个加入到当前节点的next
                self.head.next=node
    #尾插法创建单链表：用当前节点的next去连接下一个节点。          
    def insert_tail(self,data):
        #尾节点
        tail=self.head.next
        for i in data:
            node=Node(i)#创建新节点
            #判断尾节点是否为空
            if tail is None:#如果为空，则将新节点加入到尾部
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
        node=node.next
    print('')
    #删除链表中的重复元素
    def clear_repetition(self):
        cur=self.head
        while cur:
            while cur.next and cur.value==cur.next.value:
                cur.next=cur.next.next
            cur=cur.next
            
    def list_element_add(self,i,value):
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
        
        
                