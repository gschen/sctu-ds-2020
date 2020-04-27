class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None
#单链表类
class Siglelink():
    def __init__(self,node=None):
        self.__head=node
        


    #判断列链表为空
    def is_empty(self):
        '''
        if self.__head=None:
            return True
        else:
            return False
        '''
        return self.__head==None
    def length(self):
        #cur游标 表示当前操作的节点
        cur=self.__head
        #统计多少个节点
        count=0
        while cur!=None:
            count+=1
            #将cur替换为下一个节点
            cur=cur.next
        return count
    #重尾巴插入参数
    def add_tail(self,val):
        node=Node(val)
        if self.is_empty():
            self.__head=node
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
        print('')#换行
    def add_top(self,val):
        node=Node(val)
        node.next=self.__head
        self.__head=node
    #向列表中任意位子插入节点
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
    #根据下标查找节点
    def find(self,pos):
        if pos<0 or pos>self.length()-1:
            return 'error:index out of list'
        cur=self.__head
        count=0
        while cur!=None:
            if count==pos:
                return cur.elem
            else:
                count+=1
                cur=cur.next
    #查找结点是否存在
    def search(self,val):
        cur=self.__head
        while cur != None:
            if cur.elem==val:
                return True
            cur=cur.next
        return  False
#行此页面，会直接该行代码之后的代码
if __name__=='__main__': 
    s1=Siglelink()
    print(s1.is_empty())
    print(s1.length())
    s1.add_tail(10)
    s1.add_tail(20)
    s1.add_tail(30)
    print(s1.is_empty)
    s1.travel()
    s1.add_top(40)
    s1.travel()
    s1.insert(2,100)
    s1.travel()
    print(s1.find(2))
    print(s1.search(10))