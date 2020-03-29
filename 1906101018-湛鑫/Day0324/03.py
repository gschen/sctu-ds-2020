# 打印单链表
def list_print(self):
    node = self.head.next

    while node:
        print(node.value,' ',end='')
        node = node.next
    print('')

# 删除链表中重复元素 
def clear_repetition(self):
    cur=self.head
    while cur.next and cur.value==cur.next.value:
        cur.next=cur.next.next
    cur=cur.next


