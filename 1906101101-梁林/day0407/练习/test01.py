class Node(object):
    def __init__(self,date):
        self.date = date
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
    def push(self,date):
        node = Node(date)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    def pop(self):
        if not self.is_empty():
            current_node = self.head.next
            if self.get_size() == 1:
                self.head.next = None
                self.size-=1
            else:
                self.head.next = self.head.next
                self.size -= 1
                return current_node.date
        else:
            print('栈为空')
    def top(self):
        if not self.is_empty():
            return self.head.next.date
        else:
            print('栈为空')

class Test():
    def BKM(self,str1):
        Is=Stack()
        i=0
        while i<len(str1):
            if str1[i]=='(' or str1[i]=='[' or str1[i]=='{':
                Is.push(str1[i])
                i+=1
                continue
            elif Is.get_size==0:
                return False
            if (str1[i]==')' and Is.top()=='(') or (str1[i]==']' and Is.top()=='[') or (str1[i]=='}' and Is.top()=='{'):
                
                Is.pop()
                i+=1
            else:
                return False
        if Is.get_size!=0:
            return False
        return True
test=Test()
print(test.BKM("()()()()"))