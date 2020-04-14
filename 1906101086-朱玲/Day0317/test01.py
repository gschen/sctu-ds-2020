#节点类
class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None
#单链表类
class Siglelink():
    def __int__(self,node=None):
        self.__head=node

    def is_empty(self):                    #判断链表是否为空
        
        # if self.__head==None:
        #     return True
        # else:
        #     return False
        return self.__head==None

#获取链表的长度
    def length(self):
        cur=self.__head         #cur游标，表示当前操作的节点
   
       #统计有多少个节点

        count=0
        while cur!=None:
            count+=1
            cur=cur.next      #将cur替换为下一个节点
        return count

    #从尾部插入元素
    def add_tail(self,val):
        node=Node(val)
        #分别处理链表为空和不为空的情况
        if self.is_empty():

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
            print(cur.elem,end=' ')
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


if __name__=='__main__':    #运行此页面，会直接运行该代码之后的代码
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