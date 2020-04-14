#链表的方式实现队列
class Node:
    def __init__(self,value):
        self.value=value
        self.next=next

class Queue_:
    #初始化队列
    def __init__(self):
        self.head=Node#头节点
        self.end=Node#尾节点初始化
        #判断是否为空
         def is_empty(self):
            if self.size==0:
                return True
            return False
             def que_size(self):
            return self.size


        #添加列表元素
        def enqueue(self,value):
            self.size+=1
           que=Node(value)#创建节点
           if self.head is Node:#判断是否存在头节点
               self.head=self.end=que
            else:
                self.end.next=que#尾节点后面的节点
                self.end=que
            

                                                   
      
        def dequeue(self):
            if self.head is Node:
                print("000")
            else:
                self.size-=1
                self.head=self.head.next
                if self.head is Node:
                    self.end=Node
                    






                    class Node(object):
    def __init__(self,date):
        self.date=date
        self.next=Node
class Stack(object):
    def __init__(self):
        self.node=Node(Node)
        self.head=self.node
        self.size=0
    def is_empty(self):
        return self.size==0
    def get_size(self):
        return self.size
    def push(self,date):
        node=Node(date)
        node.next=self.head.next
        self.head.next=node
        self.size+=1
    def pop(self):
        if not self.is_empty():
            current_node=self.head.next
            if self.get_size()==1:
                self.head.next=Node
                self.size-=1
            else:
                self.head.next=self.head.next.next
                self.size=-1
                return current_node.date
        else:
            print("栈为空")
    def top(self):
         if not self.is_empty():
             return self.head.next.date
         else:
             print("栈为空")











class Test():
    def BracktMatch(self,str):
        ls=Stack()
        i=0
        while i<len(strl):
            if str[i]=="("or str[i] == "[" or str [i]== "{":
                ls.push(str[i])
                i+=1
                continue
            elif ls.get_size==0:
                return False
            if (str[i]==")" and ls.top() == "(") or (strl[i]== "]" and(str[i]==")" and ls.top() == "(") or (strl[i]== "]"(str[i]==")" and ls.top() == "(") or (strl[i]== "]":
                ls.pop()
                i+=1
            else:
                return False
            if ls.get_size()!=0:
                return False
            return True
test=Test()
print(test.BracktMatch("()()()(){{{"))









class Queue:
    #初始化队列
    def __init__(self):
        self.que=[]
        self.size=0#列表的长度
        #判断队列是否为空
        def is_empty(self):
            if self.size==0:
                return True
            return False



        #返回队列的长度
        def que_size(self):
            return self.size


        #添加列表元素
        def enqueue(self,value):
            self.size+=1
            self.que.append(value)
  


         #删除队列元素
         def dequeue(self):
             if self.size==0:
                 print("没有东西，不可以删除")
                 return
            else:
                self.size-=1
                self.que.pop(0)
queue=Queue()
queue.enqueue("b")
queue.enqueue("c")
queue.enqueue("d")
print(queue.que_size())

