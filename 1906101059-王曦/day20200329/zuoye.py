class Node():
    def __init__(self,val):
        self.data=val
        self.next=None
class SingleLink():
    def __init__(self,node=None):
        self.__head=Node(node)

    def appendlink(self,val):
        node = Node(val)
        p = self.__head
        while p.next!=None:
            p=p.next
        p.next = node

    def travel(self):
        p = self.__head
        while p.next!=None:
            p=p.next
            print(p.data,end=' ')

    def length(self):
        s = 0
        p = self.__head
        while p.next!=None:
            p=p.next
            s+=1
        return s
    def find(self,x):
        p = self.__head
        while x>0:
            p = p.next
            x-=1
        self.__head.next = p
    def Print(self):
        if (self.length())%2==0:
            self.find((self.length()+2)/2)
            self.travel()
        else:
            self.find((self.length()+1)/2)
            self.travel()
l = SingleLink()
l.appendlink(1)
l.appendlink(2)
l.appendlink(3)
l.appendlink(4)
l.Print()
