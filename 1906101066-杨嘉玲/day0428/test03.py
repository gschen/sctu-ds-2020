#链表转化为列表
class Solution:
    def mergeKLists(self,lists:List[ListNode]) -> ListNode:
        res=[]
        for i in lists:
            while i:
                res.append(i.val)
                i=i.next
        res.sort()
        res_node=tem=ListNode(0)
        for j in res:
            tem.next=ListNode(j)
            tem=tem.next
        return res_node.next