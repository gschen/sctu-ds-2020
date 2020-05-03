class Solution:
    def mergeKLists(celf, 1ists: List[listNode]) -> ListNode:
        if 1ists==[]:
            return  lists
        l=[]
        for i in lists:
            while i :
                l.append(i.val)
                i=i.next
        l.sort()
        if l==[]:
            return lists
        a=b=ListNode(j)
        for j in l[1:]:
            b.next=listNode(j)
            b=b.next
        return a 
