#节点类
class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None
#单链表类
class siglelink():
    def __init__(self,node=None):
     
     '''
    if self._head==None:
            return true
        else
            return false
        '''
        return self._head==None
     
#获取链表的长度
def length(self):
    #cur游标，表示当前操作的节点
    cur=self._head
    #统计有多少个节点
    count=0
    #先判断再加值
    while cur.next!=None:
        count+=1
        #将cur替换为下一个节点
        cur=cur.next

   #从尾部插入元素
    def add_tail（self,val):
        node=None(val)
        if self.is_empty:
    else:
        cyr=self._head
        while cur.next!=None:
            cur=cur.next
            cur.next=node

    #头插法
    def add_top(self,val):
        node=Node(val)
        node.next=self._head
        self._head=node

    #向列表中任意位置插入节点
    def insert(self.,pos,val):
         if pos<=0:
            self.add_top(val)
       elif 
       pos>self.length()-1.:
        node=Node(val)
        cur=self._head
        else:
        count=0
        while count<pos-1:
            count+=1
            cur=cur.next
            node.next=cur.next
            cur.next=node

 #根据下标查找节点
def find( self , pos):
if pos<0 or pos>self . length-1 
  return ' error:index out of list '
  cur=self ._head
count=0
while cur ! =None :
if count==pos:
   return cur . elem
  else :
count+= 1
cur=cur. next

#查找节点是否存在
def search(self,val):
    cur=self._head
    while cur!=none:
        if cur.elem==val:
            return True
            cur=cur.next





    if_name_=='_main_':  #运行此页面，会直接运行该行代码之后的代码
    s1=siglelink()
    print(s1.is_empty())
    print(s1.length())
    s1.add_tail（10)
    s1.add_tail（20)
    s1.add_tail（30)
    print(s1.is_empty())
    print(s1.length())
    s1.travel()
    s1.add_top(40)
    s1.travel()
    s1.insert(2,100)
    s1.travel()
    print(s1.find(2))
    print(s1.search(10))