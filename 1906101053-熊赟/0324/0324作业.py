class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        cur=head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        if count % 2==0:
            a=count/2+1
        else:
            a=(count+1)/2
        cur=head
        a=a-1
        while a:
            cur=cur.next
            a=a-1
        return cur