# 节点类
class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None

# 单链表类
class SigleLink():
    def __init__(self,node=None):
        self._head=node

    # 判断链表是否为空
    def is_empty(self):
        '''
        if self._head==None:
            return True
        else:
            return False
        '''
        return self._head==None

    # 获取链表的长度
    def length(self):
        # cur游标，表示当前操作的节点
        cur=self._head

        # 统计有多少节点
        count=0
        while cur!=None:
            count+=1

            # 将cur替换为下一个节点
            cur=cur.next
        return count
    
    # 从尾部插入元素
    def add_tail(self,val):
        node=Node(val)
        # 分别处理链表为空和不为空的情况
        if self.is_empty():
            self._head=node
        else:
            cur=self._head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
    
    # 链表节点遍历
    def travel(self):
        cur=self._head
        while cur!=None:
            print(cur.elem,end='')
            cur=cur.next

        print('')

    # 头插法
    def add_top(self,val):
        node=Node(val)
        node.next=self._head
        self._head=node
    
    # 向列表中任意位置插入节点
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
                cur=cur.next
            node.next=cur.next
            cur.next=node

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
    sl.travel