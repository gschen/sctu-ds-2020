#节点类型
class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None
#单链表类
class Siglelink():
    def __init__(self,node=None):
        self.__head=node
#判断链表是否为空
    def is_empty(self):
        ...
        if self.__head==None:
            return True
        else:
            return False
        ...
        return self.__head==None
#获取链表的长度
    def length(self):
        #cur游标表示当前操作的节点
        cur=self.__head
        #统计有多少节点
        count=0
        #先判断再加值
        while cur!=None:

            count+=1
            #将cur替换为下一个节点
            cur=cur.next
        return count
#从尾部插入元素
    def add_tail(self,val):
        node=Node(val)
        #分别处理链表为空和不为空的情况
        if self.is_empty:
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
    #链表节点遍历
    def travel(self):
        cur=self.__head
        while cur!=None:
            print(cur.elem,end='')
            cur = cur.next
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
            cur=self._head
            count=0
            while count<pos-1:
                count+=1
                cur.next
            node.next=cur.next
            cur.next=node
    #根据下标查找结点
    def find(self,pos):
        if pos<0 or pos>self.length()-1:
            return 'error:index out of list'
        cur=self._head
        count=0
        while cur!=None:
            if count==pos:
                return  cur.elem
            else:
                count+=1
                cur=cur.next
    #查找节点是否存在
    def search(self,val):
        cur=self._head
        while cur!=None:
            if cur.elem==val:
                return True
            cur=cur.next
        return False


if __name__=='__main__':#运行此页面，会直接该行代码之后的代码
    s1=Siglelink()
    print(s1.is_empty())
    print(s1.length())
    s1.add_tail(10)
    s1.add_tail(20)
    s1.add_tail(30)
    print(s1.is_empty())
    print(s1.length())
    s1.travel()
    s1.add_top(40)
    s1.travel()
    s1.insert(2,100)
    s1.travel()
    print(s1.find(2))
    print(s1.search(10))
    print(s1.search(100))


