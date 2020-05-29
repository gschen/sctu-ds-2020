#作业2
'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
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
        a=b=ListNode(1[0])  
        for j in l[1:]:
            b.next=ListNode(j)          
            b=b.next
        return a  
'''        