#节点类
class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None
#单链表类
class SigleLink():
    def __init__(self,node=None):
        self.__head=node
        
 #判断链表是否为空
    def is_empty(self):
        if self.__head==None:
            return True
        else:
            return False

        return self.__head==None

    #获取链表的长度
        def Length(self):
            #cur游标，表示当前操作的节点
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
        if self.is_empty:
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node