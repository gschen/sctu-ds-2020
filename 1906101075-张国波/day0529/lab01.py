#类
class Node:
#属性，方法/函数

#构造函数
    def __init__(self,data):
        print('this is init')

        #定义属性
        self.data=data
        self.next=None

    def sayHello(self):
        print('hello')

#如何使用类？
n=Node(-1)#默认自动执行构造函数
n.sayHello()
#n1 n2 n3
n1=Node(1)
print('n1的数据：',n1.data)
print('n1的next域：',n1.next)

n2=Node(2)

n3=Node(3)
#n1 -> n2 -> n3
n1.next=n2
n2.next=n3


#单链表
#增加一个结点，删除一个结点，查找等操作/函数
class LinkList:
#1.单链表构造函数
    def __init__(self):
        #属性
        self.head=Node(-1)
    #2.头插法操作
    def headInsert(self):

        head = self.head
        #head -> q
        q = Node(1)
        head.next = q

        #head -> 2 -> 1
        q=Node(2)
        q.next=head.next
        head.next=q

        #head -> 3 -> 2 -> 1
        q=Node(3)
        q.next=head.next
        head.next=q

    #2.2头插法的改进
    def headInsertV2(self):
        #将1到100插入到单链表
        
        head=self.head
        for i in range(1,101):
        
            node = Node(i)
            node.next=head.next
            head.next=node

 



#4.1尾插法
    def tailInsert(self):
        #始终使用p来表示单链表的尾节点
        p =self.head

        q=Node(1)
        p.next=q
        p=q

        q=Node(2)
        p.next=q
        p=q

        q=Node(3)
        p.next=q
        p=q

        #使用循环结构优化上述代码

    def tailInsertV2(self):
        #使用尾插法插入1-100整数
        p=self.head

        for i in range(1,101):
            q=Node(i)
            p.next=q
            p=q


 #3.打印所有结点
    def printList(self):
        p=self.head

        while p != None:
            
            print(p.data)
            p=p.next





l1=LinkList()
l1.headInsert()
l1.printList()
l1.headInsertV2()
l1.printList()
l1.tailInsertV2()
l1.printList()
