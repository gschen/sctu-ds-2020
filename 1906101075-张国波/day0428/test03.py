class Solution:
    def mereKLists(self,lists:List[ListNode]) -> ListNode:
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
                b.next=ListNode(j)
                b=b.next
            return a  