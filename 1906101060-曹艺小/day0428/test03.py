class Solution:
    def mergeKlists(self,lists:list[listNode]) ->listNode:
        if lists=[]:
            return lists
        l=[]
        for i in lists:
            while i:
                l.append(i.val)
                i=i.next

        l.sort()
        if l=[]:
            return lists
        a=b=listNode(l[0])
        for j in l[1:]:
            b.next=listNode(j)
            b=b.next
        return a