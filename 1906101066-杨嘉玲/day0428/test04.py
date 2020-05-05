#链表-字符串
class Solution:
    def addTwoNumber(self,l1: ListNode, l2: ListNode) -> ListNode:
        f=ListNode(0)
        p=f
        carry=0
        while l1 or l2:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            res=x+y+carry
            carry=res // 10
        p.next=ListNode(res%10)
        p=p.next
        l1=l1.next if l1 else 0
        if carry > 0:
            p.next=ListNode(1)
            return f.next