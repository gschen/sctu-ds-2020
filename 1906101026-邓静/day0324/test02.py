#打印链表
def list_print(self):
    node=self.head.next
    while node:
    print(node.value,'',end='')
    print('')


#删除链表重复元素
def clear_repetition(self):
    cur=self.head
    while cur.next and cur.value==cur.next.value:
        cur.next=cur.next.next
    cur=cur.next
S


#找到链表中间节
#某i个节点前插入值为value的节点
def list_element_add(self,i,value):
    node_new=Node(value)#创建节点
    index=0
    node=self.head.next
    while node:#找位置
        index=index+1
        if index == i -1:
            break
        node=node.next
    if node is Node:
        return False
    node_new.next=node.next#插入节点
    node.next=node_new
    
