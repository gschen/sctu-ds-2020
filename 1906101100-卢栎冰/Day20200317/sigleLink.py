# 节点类
class Node():
    def _init_(self,val):
        self.elem=val
        self.next=None

# 单链表类
class SigleLink():
    def _init_(self,node=None):
        self._head=node
        # print(self.__head)

# a=SigleLink(node=10)

  #判断链表是否为空 
    def is_empty(self):
        # if is_empty(self):
        #     return True
        # else:
        #     return False
        return self.__head == None

    #获取链表长度
    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    #尾插法
    def add_tail(self,val):
        node = Node(val)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    #链表节点遍历
    def travel(self):
        cur = self.__head
        while cur!= None:
            print(cur.elem,end='')
            cur = cur.next
        print('') 
# 头插法
def add_top(self,val):
    node=Node(val)
    node.next=self._head
    self.__head=node

# 向列表中任意位置插入节点
    def insert(self,pos,val):
        if pos<=0:
            self.add_top(val)
        elif pos>self.length()-1:
            pass
        else:
            node=Node(val)
            cur=self.__head
            count=0
            while count<pos:
                count+=1
                cur=cur.next
                node.next=cur.next
                cur.next=node
    # 根据下标查找节点
        def find(self,pos):
            if pos<0 or pos>self.length-1:
                return 'error:index out of li'
            cur=self.__head
            count=0
            while cur!=None:
                if count==pos:
                    return cur.elem
                else:
                    count+=1
                    cur=cur.next

# 查找节点是否存在
def search(self,val):
    cur=self._head
    while cur!=None:
        if cur.elem==val:
            return True
        return False

if __name__ == '__main__': #运行此页面，会直接运行以下代码
    sl=SigleLink()
    print(sl.is_empty())
    print(sl.length())
    sl.add_tail(10)
    sl.add_tail(20)
    sl.add_tail(30)
    print(sl.is_empty())
    print(sl.length())
    sl.travel()
    # sl.add_top(40)
    # sl.travel()
    # sl.insert(2,100)
    # sl.travel()
    # print(sl.find(2))
    # print(sl.search(10))