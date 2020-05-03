#作业1
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ''
        s2 = ''
        while l1:
            s1 = str(l1.val)+s1
            l1 = l1.next
        while l2:
            s2 = str(l2.val)+s2
            l2 = l2.next
        s3 = str(int(s1)+int(s2))
        l = len(s3)
        li = ListNode(int(s3[0]))
        for i in range(1,l):
            f = ListNode(int(s3[i]))
            f.next = li
            li = f 
        return li
'''