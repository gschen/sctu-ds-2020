#合并k个排序链表
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None



class Solution:
    def mergeKLists(self,lists):
        if lists==[]:
            return lists
        l=[]
        for i in lists:
            while i:
                l.append(i.val)
                i=i.next
        l.sort()
        if l==[]:
            return lists
        a=b=ListNode(l[0])
        for j in l[1:]:
            b.nnext=ListNode(j)
            b=b.next
        return a