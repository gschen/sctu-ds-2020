#节点类
class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None
#单链表类
class SigleLink():
    def __init__(self,node):
        self.__head=node
        print(self.__head)

#判断链表是否为空
    def is_empty(self):
        if self.__head==None:
            return True
        else:
            return False

#判断链表长度
    def length(self):
        #cur游标，表示当前操作的节点
        cur=self.__head
        #统计有多少节点
        count=0
        #先判断再加值
        while cur.next!=None:
            count+=1
            #将cur替换为下一个节点
            cur=cur.next
        return count
#尾插法
    def add_tail(self,val):
        node=Node(val)
        if self.is_empty():
            self.__head
        else:
            cur=self.__head
        while cur.next!=None:
            cur=cur.next
        cur.next=node

    def travel(self):
        cur=self.__head
        while cur!=None:
            print(cur)
            cur=cur.next

    def add_top(self,val):
        node=None(val)
        node.next=self.__head
        self.__head=node


    def insert(self,pop,val):
        if pos<=0:
            self.add_top(val)
        elif pos>self.length()-1:
            self.add_tail(val)
        else:
            node=None(val)
            node.next=self.__head
            count=0
            while count<pos-1:
                count+=1
                cur=cur.next
            node.next=cur.next
            cur.next=node


    def find(self,pos,):
        if pos<0 or pos>self.length-1:
            return 'error:index out of list'
        cur=self.__head
        count=0
        while cur!=None:
            if count==pos:
                return cur.elem
            else:
                count+=1
                cur=cur.next


    def search(self,val):
        cur=self.__head
        while cur!=None:
            if cur.elem==val:
                return True
            else:
                return False
        return False























if __name__=='__main__':
    sl=SigleLink()
    print(sl.is_empty())
    print(sl.length())
    sl.add_tail(10)
    sl.add_tail(20)
    sl.add_tail(30)
    print(sl.is_empty())
    print(sl.length())
    sl.travel()
    sl.insert(2,200)
    sl.find