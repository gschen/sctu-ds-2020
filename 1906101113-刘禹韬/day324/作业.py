class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None


def search(head):
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


def node_print(head):
    list1=[]
    cur=head
    while cur!=None:
        list1.append(cur.elem)
        cur=cur.next
    return list1

a=Node(1)
b=Node(2)
c=Node(3)
a.next=b
b.next=c
print(node_print(a))
print(node_print(search(a)))