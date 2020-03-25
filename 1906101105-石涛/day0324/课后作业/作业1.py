# coding=utf-8

'''
给定一个不为空的链表，要求找到该链表的中间节点（若有两个中间值取第二个），然后输出中间值往后的链表
例如：[1，2，3，4，5]
输出：[3，4，5]
'''
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        def length(x): # 计算长度
            cur=head
            count=0
            while cur!=None:
                count+=1
                cur=cur.next
            return count

        m=length(head)
        p=head
        n=m//2
        while n>0:
            p=p.next
            n-=1
        return p

