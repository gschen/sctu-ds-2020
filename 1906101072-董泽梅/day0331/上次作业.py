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
