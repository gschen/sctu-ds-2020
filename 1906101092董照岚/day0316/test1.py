#节点类
class Node():
    def __init__(self,val):
        self.elaem=val
        self.next=None
#单链表类
class SigleLink():
    def __init__(self,node=None):
        self.__head=node

#判断列表是否为空 
    def is_empty(self):


        # if self.__head==None:
        #     return True
        # else:
        #     return False
        return self.__head==None


    #获取链表长度
    def length(self):
        cur=self.__head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count

    #尾插法
    def add_tail(self,val):
        node=Node(val)
        if self.is_empty:
            self._head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
    def travel(self):
        cur=self.__head
        while cur!=None:
            print(cur.elem,end=' ')
            cur=cur.next
        print(' ')
    #头插法
    def add_top(self,val):
        node=Node(val)
        node.next=self.__head
        self.__haed=node
    

    #插入节点
    def insert(self,pos,val):
        if pos<=0:
            self.add_top
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
    #根据下标查找节点
    def find(self,pos,val):
        if pos<0 or pos>length()-1:
            return 'error'
        cur=self.__head
        count=0
        while cur!=None:
            if count==pos:
                return cur.elem
            else:
                count+=1
                cur=cur.next
    #判断节点是否存在
    def search(self,val):
        cur=self.__head
        while cur!=None:
            if cur.elem==val:
                return True
            cur=cur.next
        else:
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
        sl.add_top(40)
        sl.travel()
        sl.insert(2,100)
        sl.travel()
        print(sl.find(2))
        print(sl.search(10))