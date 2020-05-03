class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNunbers(self,l1:ListNode,l2:ListNode)->ListNode:
        result1=""
        while l1:
            result1=str(l1.val)+result1
            l1=l1.next

        result2=""
        while l2:
            result2=str(l2.val)+result2
            l2=l2.next

        s=str(int(result1)+int(result2))
        return s