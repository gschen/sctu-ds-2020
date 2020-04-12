lxh 2020/4/12 18:37:30
class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack(object):
    def __init__(self):
        self.node=Node(None)
        self.head=self.node
        self.size=0
    def is_empty(self):
        return self.size==0
    def get_size(self):
        return self.size
    def push(self,data):
        node=Node(data)
        node.next=self.head.next
        self.head.next=node
        self.size+=1
    def pop(self):
        if not self.is_empty():
            current_node=self.head.next
            if self.get_size()==1:
                self.head.next=None
                self.size-=1
            else:
                self.head.next=self.head.next.next
                self.size-=1
                return current_node.data
        else:
            print("栈为空")
    def top(self):
        if not self.is_empty():
            return self.head.next.data
        else:
            print("栈为空")
class Test():
    def BracktMatch(self,strl):
        ls=Stack()
        i=0
        while i<len(strl):
            if strl[i]=="(" or strl[i] == "[" or strl[i] == "{":
                ls.push(strl[i])
                i+=1
                continue
            elif ls.get_size == 0:
                return False
            if (strl[i] == ")" and ls.top() == "(") or (strl[i] =="]" and ls.top() =="[") or (strl[i] == "}" and ls.top() == "{"):
                ls.pop()
                i+=1
            else:
                return False
        if ls.get_size() !=0:
            return False
        return True
test = Test()
print(test.BracktMatch("()()()()"))

lxh 2020/4/12 18:40:19
#链表的方式实现队列
class Node:
    #初始化,value为当前节点的值
    def __init__(self,value):
        self.value=value
        self.next=next

class Queue_:
    #初始化队列
    def __init__(self):
        self.head=None#头节点初始化
        self.end=None#尾节点初始化
        self.size=0

    #判断是否为空
    def  is_empty(self):
        if self.size==0:
            return True
        return False
     #返回队列长度
    def que_size(self):
        return self.size
    #列表添加元素
    def enqueue(self,value):
        self.size+=1
        que=Node(value)#创建节点
        if self.head is None:#判断是否存在头结点
            self.head=self.end=que
        else:#如果存在头结点
            self.end.next=que#将新节点放在尾节点后面（第一步）
            self.end=que#将尾节点指针指向新节点（第二步）

    #删除队列元素
    def dequeue(self):
        #判断队列是否为空
        if self.head is None:
            print("1111")
        else:
            self.size-=1
            self.head=self.head.next#删除元素，使头指针指向下一个元素
            if self.head is None:  
                self.end=None  #如果删除元素后队列没有元素，head此时为None,end此时也应该为end

queue=Queue_()
print(queue.is_empty())
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.que_size())

lxh 2020/4/12 18:40:19
class Queue:
    #初始化队列
    def __init__(self):
        self.que=[]
        self.size=0  #列表的长度
    #判断队列是否为空
    def is_empty(self):
        if self.size==0:
            return True
        return False

    #返回队列长度
    def que_size(self):
        return self.size

    #列表添加元素
    def enqueue(self,value):
        self.size+=1
        self.que.append(value)

    #删除队列元素
    def dequeue(self):
        if self.size==0:
            print("没东西不能删")
            return
        else:
            self.size-=1
            self.que.pop(0)
queue=Queue()
queue.enqueue("1")
queue.enqueue("5")
queue.enqueue("10")
print(queue.que_size())
