#节点类
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
        '''
        if self.__head==None:
            return True
        else:
            return False
        '''
        return self.__head==None

    #获取链表的长度
    def length(self):
        cur=self.__head
        count=0
        while cur.next!=None:
            count+=1
            cur=cur.next

