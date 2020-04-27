#链表
class Node():
    def __init__(self, val):
        self.elem = val
        self.next = None

#单链表
class SigleLink():
    def __init__(self, node=None):
        self.__head = node

    #判断链表是否为空
    def is_empty(self):
        '''
        if self.__head == None:
            return True
        else:
            return False
        '''
        return self.__head == None

    #获取链表的长度
    def Length(self):
        #cur游标--当前操作的节点
        cur = self.__head
        
        #统计节点数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    #尾插
    def add_tail(self, val):
        node = Node(val)
        #链表为空和不为空
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    #遍历链表节点
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print('\n')
    
    #头插
    def add_top(self, val):
        node = Node(val)
        node.next = self.__head
        self.__head == node

    #任意位置插入
    def insert(self, pos, val):
        if pos <= 0:
            self.add_top(val)
        elif pos > self.Length()-1:
            self.add_tail(val)       
        else:
            node = Node(val)
            cur = self.__head
            count = 0
            while count < pos-1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    #根据下标查找节点
    def find(self, pos):
        if pos<0 or pos>self.Length()-1:
            return "error:index out of list"
        cur = self.__head
        count = 0
        while cur != None:
            if count == pos:
                return cur.elem
            else:
                count += 1
                cur = cur.next

    #判断节点是否存在
    def search(self, val):
        cur = self.__head
        while cur != None:
            if cur.elem == val:
                return True
            cur = cur.next
        return False


#运行此页面，会直接该行代码之后的代码
if __name__ == "__main__":  
    sl = SigleLink()
    print(sl.is_empty())
    print(sl.Length())
    sl.add_tail(10)
    sl.add_tail(20)
    sl.add_tail(30)
    print(sl.is_empty())
    print(sl.Length())
    sl.travel()
    sl.add_top(40)
    sl.travel()
    sl.insert(2,100)
    sl.travel()
    print(sl.find(2))
    print(sl.search(10))
    print(sl.search(100))

