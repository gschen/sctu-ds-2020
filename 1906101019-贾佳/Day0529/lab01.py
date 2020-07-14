class Node():
    #构造函数 
    def __init__(self,data):
        #定义属性
        self.data = data
        self.next = None


# n1 n2 n3
n = Node(-1)
n1 = Node(1)
print(n1.data)
print(n1.next)

n2 = Node(2)
n3 = Node(3)

#n1 -> n2 -> n3
n1.next = n2
n2.next = n3
print(n1.next.next.data)

   #单链表
    #增加一个结点，删除一个结点，查找等操作/函数 
class LinkList():

    #1、单链表的构造函数
    def __init__(self):
        #属性
        self.head = Node(-1)

    # 2.1.头插法操作
    def headInsert(self):
        head = self.head
        
        #head -> q
        q = Node(1)
        head.next = q

        #head ->2 -> 1
        q = Node(2)
        q.next = head.next
        head.next = q

        #head -> 3 -> 2 -> 1
        q = Node(3)
        q.next = head.next
        head.next = q
    
    
    #2.2、头插法的改进
    def headInsertV2(self):
        head = self.head
        for i in range(1,101):
            q = Node(i)#构造一个新节点，数据域为i


            q.next = head.next
            head.next = q
        
    # 3.打印所有节点
    def printList(self):
        p = self.head
        #若不打印头节点 p = self.head.next


        while p != None:
            print(p.data)
            p = p.next
            
    # 4.1 尾插法
    def tailInsert(self):
        #始终使用p来表示单链表的尾结点
        p = self.head

        q = Node(1)
        p.next = q
        p = q # 当前链表的尾节点变为了q

        q = Node(2)
        p.next = q
        p = q

        q = Node(3)
        p.next = q
        p = q
    
    # 4.2 尾插法改进版
    def tailInsertV2(self):
        p = self.head
        for i in range(1,101):
            q = Node(i)
            p.next = q
            p = q

List = LinkList()
List.tailInsert()
List.printList()





