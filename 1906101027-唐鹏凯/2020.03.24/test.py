class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class List():
    def __init__(self):
        #头节点
        self.head = Node(-1)
    #前插法创建单链表
    def insert_before(self,data):
        for i in data:
            node = Node(i)#创建新节点
            #判断头节点的下一个节点是否为空
            if self.head.next is None:#如果为空，则将新节点加入到next
                self.head.next = node
            else:
                node.next = self.head.next#将头节点的下一个节点加入到当前的node
                self.head.next = node
        
    def insert_tail(self,data):
        tail = self.head.next #相当于指针，从头节点开始

        for i in data:#遍历data中的数据
            node = Node(i)#将data里面的数据给赋值给node

            if tail is None:#如果下一个节点为空则直接将node的值放进节点
                self.head.next = node
            else:
                tail.next = node#如果不为空则将值赋给节点尾巴上
                tail = node#将tail节点后移至最后的一个节点
    
    #打印单链表
    def list_print(self):
        node = self.head.next

        while node:
            print(node.value,' ',end='')
            node = node.next
        print('')
    #删除链表中重复元素
    def cur_repetition(self):
        cur = self.head
        while cur:#循环遍历
            while cur.next and cur.value == cur.next.value:
                cur.next = cur.next
            cur = cur.next#帮助以上遍历后面的
#插入元素
    def list_element_add(self,i,value):
        node_new = Node(value)#创建新节点
        index = 0
        node = self.head.next

        while node:#找位置
            index=index+1
            if index == i - 1:
                break
            node = node.next

        if node is None:
            return False
        
        node_new.next = node.next#插入节点
        node.next = node_new
  