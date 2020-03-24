#删除链表中的重复元素
def clear_repetition(self):
    cur=self.head
    while cur:#遍历元素
        while cur.next and cur.value==cur.next.value:#（判断节点的值与下一个节点的值是否相同）
            cur.next=cur.next.next#将指针指向下下个节点（删除元素）
        cur=cur.next


#在第i个节点前插入value的节点
def list_element_add(self,i,value):
    node_new=Node(value)#创建新节点
    index = 0
    node=self.head.next
    while node:#找位置
        index=index + 1
        if index == i-1:
            break
        node=node.next
        if node is None:
            return False
        node_new.next=node.next#插入节点
        node.next=node_new







