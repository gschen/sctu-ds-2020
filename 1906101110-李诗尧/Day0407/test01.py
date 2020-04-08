class Node(object):          #创建一个节点
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack(object):
    def __init__(self):
        self.node = Node(None)   #初始化栈
        self.head = self.node    #创建头节点
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def get_size(self):          #得到栈长度
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
        while i < len(str1):
            if str1[i] == "(" or str1[i] == "[" or str1[i] == "{":
                ls.push(str1[i])
                i+=1
                continue
            elif ls.get_size == 0:
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
print(test.BracketMatch("()()()()"))