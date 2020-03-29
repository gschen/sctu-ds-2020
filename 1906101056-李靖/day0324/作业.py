class Node():
    def __init__(self,value):
        self.elem=value
        self.next=None
class List():
    def __init__(self,node=None):
        self.head=node
    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False
        return self.head==None   
    def add_tail(self,value):
        node=Node(value)
        if self.is_empty():
            self.head=node
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
    def Length(self):
        cur=self.head
        count=0
        while cur.next!=None:
            count+=1
            cur=cur.next
        return count
    def find(self,pos):
        if pos<0 or pos>self.Length()-1:
            return "error:index out of list"
        cur=self.head
        count=0
        while cur!=None:
            if count==pos:
                return count
            else:
                count+=1
                cur=cur.next   
    def mu(self):
        cur=self.head
        list=[]
        while cur!=None:
            list.append(cur.elem)
            cur=cur.next
        N=a.find(2)
        print(list[N:])
if __name__=="__main__":
    a=List()
    a.add_tail(1)
    a.add_tail(2)
    a.add_tail(3)
    a.add_tail(4)
    a.add_tail(5)
    a.mu()