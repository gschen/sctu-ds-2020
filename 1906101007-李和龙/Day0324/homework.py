"""
给定一个不为空的链表，要求找到该链表的中间节点（若有两个中间值取第二个）
，然后输出中间值往后的链表
例如：[1，2，3，4，5]
输出：[3，4，5]

"""
class Node():
    def __init__(self,val):
        self.elem = val
        self.next = None

class mid():
    def __init__(self,node=None):
        self.head=node
    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False
        return self.head==None
    def length(self):
        cur=self.head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count
    def add_tail(self,val):
        node=Node(val)
        if self.is_empty():
            self.head=node
        else:
            cur=self.head
            while cur.next!=None:
                cur.next=node
    def find(self,pos):
        if pos < 0 or pos > self.length()-1:
            return "error:index out of list"
        cur=self.head
        count=0
        while cur!=None:
            if count==pos:
                return count
            else:
                count+=1
                cur=cur.next
    def aa(self):
        cur=self.head
        list=[]
        while cur!=None:
            list.append(cur.elem)
            cur=cur.next
        N=n.find(2)
        print(list[N:])

if __name__=="__main__":
    n=mid()
    n.add_tail(1)
    n.add_tail(2)
    n.add_tail(3)
    n.add_tail(4)
    n.add_tail(5)
    n.aa()


