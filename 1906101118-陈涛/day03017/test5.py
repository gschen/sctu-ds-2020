#节点
class Node():
    def __init__(self,val):
        self.elem = val
        self.next = None
#单链表
class SigleLink():
    def __init__(self,node=None):
        self.__head = node
        
#判断链表是否为空
    def is_empty(self):
        # if self.__head == None:
        #     return True
        # else:
        #     return False
        return self.__head == None
#链表长度
    def Length(self):
        cur = self.__head
        count = 0
        while cur!=None:
            count += 1
            #将cur替换为下一节点
            cur = cur.next 
        return count
#尾插法
    def add_tail(self,val):
        node = Node(val)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next!=None:
                cur = cur.next
            cur.next = node
#链表节点遍历
    def travel(self):
        cur = self._head
        while cur!=None:
            print(cur.elem,end='')
            cur=cur.next

#头插法
    def add_top(self,val):
        node = Node(val)
        node.next=self.__head
        self._head = node
        
#任意位置插入
    def insert(self,pos,val):
        if pos <= 0:
            self.add_top(val)
        elif pos >self.Length()-1:
            self.add_tail(val)
        else:
            node=Node(val)
            cur = self._head
            count = 0
            while count < pos-1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

#根据下标找节点
    def find(self,pos):
        if pos < 0 or pos > self.Length-1:
            return 'error:index out of list'
        cur = self._head
        count = 0
        while cur!=None:
            if count == pos:
                return cur.elem
            else:
                count += 1
                cur = cur.next
#查找节点是否存在
    def search(self,val):
        cur = self._head
        while cur!=None:
            if cur.elem == val:
                return True
            cur = cur.next
        return False
            


#运行此页面，会直接运行下行代码之后的代码
if __name__=='__main__':
    sss = SigleLink()
    
    
    print(sss.is_empty())
    print(sss.Length())
    
    
    
    
        