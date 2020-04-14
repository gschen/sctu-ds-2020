class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None
class Solution():
    def length(self,head):
        cur = head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        if count % 2 == 0:
            a = count/2 + 1
        else:
            a = (count+1)/2
        cur = head
        a = a-1
        while a<0:
            cur = cur.next
            a = a - 1
            return cur