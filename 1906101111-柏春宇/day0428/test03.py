class Solution:
    def mergeKLists(self,lists: List[ListNode]) -> ListNode:
        if list==[]:
            return lists
        l=[]
        for i in lists:
            while i:
                l.append(i.val)
                i=i.next
        l.sort()
        if l==[]:
            return lists
        a=b=ListNode(1[0])

        for j in l[1:]:
            b.next=ListNode(j)
            b=b.next
        return a
    