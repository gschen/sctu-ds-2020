#节点类
class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None
#单链表类
class SigleLink():
    def __init__(self,node=Node):
        self.__head=node

    #判断列表是否为空
    def is_empty(self):
        '''
        if self.__head==None:
            return True
        else:
            return False
        '''
        return self.__head==None

    #获取链表的长度
    def length(self):
        #cur游标，表示当前操作的节点
        cur=self.__head
        #统计有多少节点
        count=0
        while cur!=None:
            print('测试',cur.elem)
            count+=1
            #将cur替换为下一个节点
            cur=cur.next
        return count
    #从尾部插入元素
    def add_tail(self,val):
        node=Node(val)
        if self.is_empty:
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
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

if __name__=='__main__':#运行次页面，会直接该行代码之后的代码
    sl=SigleLink()
    print(sl.is_empty())
    print(sl.length())
    sl.add_tail(10)
    sl.add_tail(30)
    print(sl.is_empty())
    print(sl.length())
