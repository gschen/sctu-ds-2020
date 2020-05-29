class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(object):
    def mergexLists(self,lists):
        if lists==[]:
            return lists
        l=[]
        for i in lists:
            while i:
                i.append(i.val)
                i=i.next
        l.sort()
        if i==[]:
            return lists
        a=b=ListNode(l[0])
        for j in l[1:]:
            b.next=ListNode(j)
            b=b.next
            return a