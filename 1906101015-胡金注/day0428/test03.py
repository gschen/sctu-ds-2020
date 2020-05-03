s1=''
s2=''
while l1:
    s1=s1+str(l1.val)
    l1=l1.next
while l2:
    s2=s2+str(l2.val)
    l2=l2.next
s1=s1[::-1]
s2=s2[::-1]
s3=str(eval(s1)+eval(s2)):
s3=s3[::-1]
for i in s3:
    tem.next=ListNode(eval(i))

#2
class Solution:
    def mergrkLists(self,lists:List[ListNode]) -> ListNode:
        res=[]
        for i in list:
            while i:
                res.append(i.val)
                i=i.next
            res.sort()
            res_node=tem=ListNode(0)
            for j in res:
                tem.next=ListNode(j)
                tem=tem.next
            return res_node.next