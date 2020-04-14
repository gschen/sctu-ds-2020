class Stack(object):
    def __init__(self, limit=10):
        self.stack = [] #存放元素
        self.limit = limit #栈容量极限
    def push(self, data): #判断栈是否溢出
        if len(self.stack) >= self.limit:
            print('StackOverflowError')
            pass
        else:
            self.stack.append(data)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack') #空栈不能被弹出
    def peek(self): #查看堆栈的最上面的元素
        if self.stack:
            return self.stack[-1]
    def is_empty(self): #判断栈是否为空
        return not bool(self.stack)
    def size(self): #返回栈的大小
        return len(self.stack)


class Test():
    def kh(self,str1):
        stack = Stack(len(str1))
        i = 0
        while i < len(str1):
            a = str1[i]
            if a == "(" or a == "{" or a == "[":
                stack.push(a)
                i+=1
                continue
            elif stack.is_empty():
                return False
            if (a == ")" and stack.peek()=="(") or (a == "]" and stack.peek()=="[") or (a == "}" and stack.peek()=="{"):
                stack.pop()
                i+=1
                continue
            else:
                return False
        if not stack.is_empty():
            return False
        return True

test = Test()
print(test.kh("(({{}}))"))

