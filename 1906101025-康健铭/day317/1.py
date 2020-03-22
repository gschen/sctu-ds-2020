# 节点类
class node():
    def __init__(self,val):
        self.elem=elem
        self.next=none
# 单链表
class siglelink():
    def __init__(self,node=none):
        self.__head=node
    # 判断链表是否为空
    def is_empty(self):
        if self.__head==None:
            return True 
        else:
            return False
        
        return self.__head==None 
        # 获取链表的长度
        def length(self):
            # cur游标，表示当前操作的节点
            cur=self.__head
            # 统计有多少节点
            count=0
            # 先判读再加值
            while cur!=None:
                count+=1
                 # 蒋cur替换为下一个节点
                cur=cur.next
            return count
        # 从尾部插入元素
        def add_tail(self,val):
             node=Node(val)
            if self.is_empty():
                self.__head=node
            else:
                 cur.self.__head
                while cur.next!=none:
                    cur=cur.next
                cur.next=node
        #    链表节点遍历
        def travel(self):
            cur=cur.__head
            while cur!=none:
                print(cur.elem,end=" ")
                cur=cur.next
        # 头插法
        def add_top(self,val):
            node=node(val)
            node.next=self.__head
            self.__head=node
        # 向链表中任意位置插入
        def insert(self,pos,val):
            if pos<=0:
                self.add_top(val)
            elif:
                pos>self.length()-1
                self.add_tail(val)
            else:
                node=node(val)
                cur=self.__head
                count=0
                while count<pos-1:
                    count+=1
                    cur=cur.next
                node.next=cur.next
                cur.next=node
            
    # 根据下标查找节点
    def find(self,pos):
        if pos<0 or pos>self.length()-1:
            return "error:index out of link"
        cur=self.__head
        count=0
        while cur!=none :
            if count==pos:
                return cur.elem
            else:
                count+=1
                cur=cur.next
    # 判断节点是否存在
    def search(self,val):
        cur=self.__head
        while cur!=none :
            if cur.elem==val:
                return True
            cur=cur.next
        return False

        





            
        


