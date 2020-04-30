class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self,lists):
        if list==[]:
            return lists
        l=[]
        for i in lists:
            while i:
                l.append(i.val)
                i=i.next
        l.sort()
        l_node=tem=ListNode(0)
        for j in l:
            tem.next=ListNode(j)
            tem=tem.next
        return l_node.next
