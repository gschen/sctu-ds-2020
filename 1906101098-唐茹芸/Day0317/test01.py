class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None


class SigleLink():
    def __init__(self,node=None):
        self.__head=node
    
    def is_empty(self):
        if self._head==None:
            return True
        else:
            return False

        return self._head==None

    def length(self):
        cur=self.__head
        count=0
        while cur.next!=None:
            count+=1
            cur=cur.next
        return count

    def add_tail(self,val)：
        node=Node(val)
        if self.is_empty:
            self._head=Node
        else:
            cur=self._head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

    def travel(self):
        cur=self._head
        while cur!=None:
            print(cur.elem,end='') 
            cur=cur.next
        print('')  

    def add_top(self,val):
        node=Node(val)  
        node,next=self.__head
        self._head=node

    def insert(self,pos,val):
        if pos<=0:
            self.add_top(val)
        elif pos>self.length()-1:
            self.add_tail(val) 
        else:

            node=Node(val)
            cur=self.__head
            count=0
            while count<pos-1:
                count+=1
                cur=cur.next
            node.next=cur.next
            cur.next=node

    def find(self,pos):
        if pos<0 or pos>self.length-1:
            return'error:index out of list'
        cur=self._head
        count=0
        while cur!=None:
            if count==pos:
                return cur.elem
            else:
            count+=1
            cur=cur.next       

if __name__=='__main__':
    sl=SigleLink()
    print(sl.is_empty())
    print(sl.length())
    s1.add_tail(10)
    s1.add_tail(20)
    s1.add_tail(30)
    print(sl.is_empty())
    print(sl.length())
    s1.travel()
    s1.add_top(40)
    s1.travel()
    s1.insert(2,100)
    s1.travel()






