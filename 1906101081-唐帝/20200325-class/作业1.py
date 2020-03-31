class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
n1 = Node('n1',None)
n2 = Node('n2',n1)
n3 = Node('n3',n2)
n4 = Node('n4',n3)
n5 = Node('n5',n4)

p1 = n5
p2 = n5
while p2.next is not None and p2.next.next is not None:
    p1 = p1.next
    p2 = p2.next.next
print(p1.data)
#。.
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cur=head
        num=0
        while cur :
            num=num+1
            cur=cur.next
        mid=num//2
        new_head=head
        for i in range(mid):
            new_head=new_head.next
        return new_head
