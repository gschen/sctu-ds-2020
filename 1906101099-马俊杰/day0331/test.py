'''
class Stack(object):
    def __init__(self,limit = 10):
        self.stack = []
        self.limit = limit
    def is_empty(self):
        return len(self.stack) == 0
    def push(self,data):
        if len(self.stack)>=self.limit:
            print('栈溢出')
        else:
            self.stack.append(data)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print('空栈不能被弹出')
    def top(self):
        if self.stack:
            return self.stack[-1]
    def size(self):
        return len(self.stack)                                       
'''
'''
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
        return self.size == 0
    def get_size(self):
        return self.size
    def push(self,data):
        node =  Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1  
    def pop(self):
        if not self.is_empty():     #判断是否为空
            current_node = self.head.next   #保留栈顶元素 
            if self.get_size() == 1:
                self.head.next = None
                self.size-=1
            else:
                self.head.next = self.head.next.next    #将头节点指向栈的下一个节点
                self.size -=1
                return current_node.data 
        else:
            print('栈为空')
    def top(self):
        if not self.is_empty():
            return self.head.next.data
        else:
            print('栈为空')

class Test():
    def BracketMatch(self,str1):
        ls = Stack()
        i = 0
        while i < len(str1)
            if str[i] == "(" or str1[i] == "[" or str1[i] == "{":
                ls.push(str1[i])
                i+=1
                continue
            elif ls.get_size == 0
                return False
            if (str1[i] == ")" and ls.top() == "(") or (str1[i] == "]" and ls.top =="[") or(str1[i] == "}" and ls.top() == "["):
                ls.pop()
                i+=1
            else:
                return False
        if ls.get_size() != 0:
            return False
        return True

test = Test()
print(test.BracketMatch("()()()()){{{{"))


s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.is_empty())
print(s.top())
s.pop()
s.pop()
s.pop()
print(s.is_empty())
print(s.get_size())
print(s.top())
'''
