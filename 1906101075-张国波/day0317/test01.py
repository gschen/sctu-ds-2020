class Node():
    def __init__(self):
        self.elem=elem
        self.next=None

class SigleLink():
    def __init__(self,node=None):
        self.__head=node

    def is_empty(self):
        if self.__head==None:
            return True
        else:
            return False

        return self.__head==None

    def length(self):
        cur=self.__head
        counr=0
        while cur.next!=None:
            count += 1
            cur=cur.next
        return count

    def add_tail(self,val):
        node=Node(val)
        if self.is_empty():
            self.__head=node
        else:
            cur=self.__head
            while cur!=None:
                cur=cur.next
            cur.next=node

    def travl(self):
        cur=self.__head
        while cur!=None:
            print(cur.elem,end='')
            cur=cur.next

        print('')

    def add_top(self,val):
        node=Node(val)
        node.next=self.__head
        self.__head=node

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

    def find(self,pos,val):
        if pos<0 or pos>self.length()-1:
            return 'error:index out of list '
        cur=self.__head
        count=0
        while cur!=None:
            if count == pos:
                return cur.elem
            else:
                count+=1
                cur=cur.next

    def search(self,val):
        cur = self.__head
        while cur!=None:
            if cur.elem==val:
                return True
                cur=cur.next
        return False            

if __name__=='__main__':
    s1=sigleLink()
    print(s1.is_empty())
    print(s1.length())
    s1.add_tail(10)
    s1.add_tail(20)
    s1.add_tail(30)
    print(s1.is_empty())
    print(s1.length())
    s1.travl()
    s1.add_top(40)
    s1.travel()
    s1.insert(2,100)
    s1.travel()
    print(s1.find(2))
    print(s1.search(200))
    print(s1.search(10))