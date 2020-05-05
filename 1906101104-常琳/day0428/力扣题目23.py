#力扣23题
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l=[]
        for i in lists:
            while i:
                l.append(i.val)
                i=i.next
        l.sort()
        a=b=ListNode(0)
        for j in l:
            b.next=ListNode(j)
            b=b.next
        return a.next


#力扣101题：
