#类

class Node:
    #属性，方法/函数

    #构造函数
    def __init__(self):
        print('zhis is init')

        #定义属性：
        self.data = data
        self.next = next

    def sayhello(self):
        print('hello')

#如何使用类？
n = Node()#默认构造执行函数
n.sayhello()

n1 = Node(1)
print('n1的数据域：', n1.data)
print('n1的next域：',n1.next)

n2 = Node(2)
n3 = Node(3)


# n1 -> n2 -> n3
n1.next = n2
n2.next = n3

#单链表
#增加一个节点，删除一个节点，查找登操作/函数
class LinkList:

    # 1. 单链表构造函数
    def __init__(self):

        #属性
        self.head = Node(-1)
    # 2.头插法操作
    def headInsert(self):
        #将证书1-100插入单链表
        #head ->100 -> 99 -> ...-> 1
        for i in range(1, 101):
            q = Node(i)  #构造一个新节点，数据域为i
            q.next = head.next
            head.next = q

        head = self.head
        #head -> q
        q = Node(1)
        head.next = q
        #head -> 2 -> 1
        q = Node(2)
        q.next = head.next
        head.next = q

        #head ->3 -> 2 -> 1
        q = Node(3)
        q.next = head.next
        head.next = q
    # 3.打印使用节点
    def printList(self):
        p = self.head

        while p != Node:
            p = p.next
            print(p.data)
            p = p.next
    # 4.尾插法
    def tailInsert(self):
        #始终使用p来表示单链表的尾结点
        p = self.head

        q = Node(1)
        p.next = q
        p = q#当前链表的尾结点变成了q

        q = Node(2)
        p.next = q
        p = q

        #使用循环结构油画生疏代码

    #4.2尾插法
    def tailInsertV2(self):
        #使用尾插法插入1-100整数。

        p = self.head

        for i in range(1, 100):
            q = Node(i)
            p.next = q
            p = q



l1 = LinkList()
l1.headInsertV2()
l1.printList()

#类中两种写法的区别
self.daa # 这是一个类的属性/成员变量
self.data()#这是一个函数/方法，要使用这个函数 动词开头，不适用名词作为方法名字


class Person:
    def __init__(self):
        self.name
        self.age
        self.ID