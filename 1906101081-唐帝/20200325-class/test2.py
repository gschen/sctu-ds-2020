def list_print(self):
    node=self.head.next

    while node:
        print(node.value,'',end='')
        node=node.next
    print('')
# 删除链表中重复元素
def clear_repetition(self):
    cur=self.head
    while cur:
        while cur.next and cur.value==cur.next.value:
            cur.next=cur.next.next
        cur=cur.next
    # 找到链表中间节点

def list_element_add(self,i,value):
    
    #node_new_Node(value)#创建新节点

    index=0

    node = self.head.next

    while node:#找位置
        index =index+1

        if index==i-1:
            break

        node=node.next

    if node is None:
        return False

    node_new.next=node.next#插入节点
    #。
    