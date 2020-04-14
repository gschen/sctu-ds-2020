class Node(object):
    def __init__(self.data):
    self.data = data
    self.next = None

class Stack(object):
    def __init__(self):
        self.node = Node(Node)
        self.head = self.node
        self.size = none
    def is_empty(self):
        return self.size == 0
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
            self.size -=1
            return current_node.data
        else:
            print('栈为空！')
    def top(self):
        if not self.is_empty():

class Text():
    def bracketMatch(self,str):
        Is = stack()
        i = 0
        while i < len(str)
            if str[i] == "("or str[i] == or str[i] =="{":
                Is.push(str1[i])
                i+=1
                continue
            elif Is.get_size == 0:
                return False
            if (str1[i]==")" and Is.top() == "(") or (str[i] == "]" and Is,top() =="[") or (str[i]=="}" and Is,
                Is.pop()
                i+=1
            else:
                return False
            if Is.get_size() != 0:
                return False
            return True

test = Test()
print(test.BracketMatch("()()()())"))