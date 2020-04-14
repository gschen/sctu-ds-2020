class Node(object):

    def __init__(self,data):

        self.data = data

        self.next = None

class Stack(object):

    def __init__(self):

        self.node = Node(None)

        self.head = self.node

        self.size = 0

    def is_empty(self):

        return self.size

    def get_size(self):

        return self.size

    def push(self,data):

        node = Node(data)

        node.next = self.head.next

        self.head.next = node

        self.size += 1

    def pop(self):

        if not self.is_empty():

            current_node = self.head.next

            if self.get_size() == 1:

                self.head.next = None

                self.size -= 1

            else:

                self.head.next = self.head.next.next

                self.size -= 1

                return current_node.data

        else:

            print('栈为空')

    def top(self):

        if not self.is_empty():

            return self.head.data

        else:

            print('栈为空')





class Test():

    def BracketMatch(self,str):

        ls = Stack()

        i = 0

        while i < len(str):

            if str[i] == '(' or str[i] == '[' or str[i] == '{':

                ls.push(str[i])

                i += 1

                continue

            elif ls.get_size() == 0:

                return False

            if (str[i] == ')' and ls.top() == '(') or (str[i] == ']' and ls.top() == '[') or (str[i] == ']' and ls.top() == '{'):

                ls.pop()

                i += 1

            else:

                return False

        if ls.get_size() != 0:

            return False

        return True



test = Test()

print(test.BracketMatch("()()()"))




# 队列

class Queue:

    # 初始化队列

    def __init__(self):

        self.que = []

        self.size = 0

    # 判断队列是否为空

    def is_empty(self):

        if self.size == 0:

            return True

        return False

    # 返回队列长度

    def que_size(self):

        return self.size

    # 添加元素

    def enqueue(self,val):

        self.size += 1

        self.que.append(val)

    # 删除元素

    def dequeue(self):

        if self.size == 0:

            print('队列为空，不可删')

            return

        else:

            self.size -= 1

            self.que.pop(0)



queue = Queue()

queue.que_size()

queue.enqueue(1)

queue.enqueue(3)

queue.enqueue(5)

queue.enqueue(7)

queue.is_empty()






# 用链表方式实现队列

class Node:

    def __init__(self,val):

        self.val = val

        self.next = next

class Queue_:

    def __init__(self):

        self.head = None

        self.end = None

        self.size = 0

    def is_empty(self):

        if self.size == 0:

            return True

        return False

    def que_size(self):

        return self.size

    # 添加

    def enqueue(self,val):

        self.size += 1

        que = Node(val)  #创建节点

        if self.head is None:

            self.head = self.end = que

        else:

            self.end.next = que   #将新节点放在尾节点后

            self.end = que   #将尾节点指向新节点

    def dequeue(self,val):

        if self.head is None:

            print('队列为空')

        else:

            self.size -= 1

            self.head = self.head.next

            if self.head is None:

                self.end = None

queue =Queue_()

print(queue.is_empty())
