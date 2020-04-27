# 给定一个不为空的链表，要求找到该链表的中间节点（若有两个中间值取第二个），然后输出中间值往后的链表
# 例如：[1，2，3，4，5]
# 输出：[3，4，5]


# 思路1：先找到链表的长度，然后找到中间位置，最后将链表的头节点指向中间位置的节点
# 还可以使用其他思路，可跟据自己的需求编写代码
class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None
def search_middle(head):
    cur=head
    count=0
    while cur!=None:
        count+=1
        cur=cur.next
        
    p=head
    n=count//2
    while n>0:
        p=p.next
        n-=1
    return p
