class Solution:
    def mergeKLists(self,lists:List[ListNode]) -> LisetNode
    L=[]
    for i in lists:
        while i:
            L.append(i.val)
            i=i.next
    L_sort()
    L_node=tem=ListNode(0)
    for j in L:
        tem.next=ListNode(j)
        tem=tem.next
    return L_node.nexte 