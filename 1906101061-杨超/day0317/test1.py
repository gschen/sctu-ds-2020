#单链表siglelink
#节点类
class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None
#单链表类
class SigleLink():
    def __init__(self,node=None):
        self.__head=node
        print(self.__head)
    #判断列表是否为空
    def is_empty(self):
        '''
        if self.__head==None:
            return True
        else:
            return False
    '''
        return self.__head==None
#获取列表长度
    def length(self):
        cur = self.__head
#统计有多少节点
        count=0
        while cur!=None:
            count+=1
    #将cur替换为下一个节点
            cur=cur.next
        return count
#从尾部插入元素
    def add_tail(self,val):
        node=Node(val)
    #分别处理链表为空和不为空的情况
        if self.is_empty():
            self.__head=Node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
            
            
#链表节点历遍
    def travel(self):
        cur=self.__head
        while cur!=None:
            print(cur.elem,end='')
            cur=cur.next
        print('')#换行
#头插法
    def add_top(self,val):
        node=Node(val)
        node.next=self.__head
        self.__head=node

#向列表中任意位置插入节点
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
if __name__=='__main__': #运行此页面，会直接运行代码之后的代码
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