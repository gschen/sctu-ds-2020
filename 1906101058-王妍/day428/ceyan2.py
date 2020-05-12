#给出两个非空的链表用来表示两个非负的整数。
# 其中，他们各自的位数是按照逆序的方式存储的，并且他们的节点只能存储一位数字。
##如果，我们将两个数相加起来，则会返回一个新的链表来表示他们的和。
#您可以假设除了数字0以外，这两个数都不会以0开头
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def addTwoNumbers(self,l1:ListNode,l2:ListNode)->ListNode:
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