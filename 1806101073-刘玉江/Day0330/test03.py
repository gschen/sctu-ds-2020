class Node(object):
    def __init__(self, data):
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

    def push(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if not self.is_empty():
            current_node = self.head.next
            if self.get_size() == 1:
                self.head.next = None
            else:
                self.head.next = self.head.next.next
            self.size -= 1
            return current_node.data
        else:
            raise IndexError("pop from empty stack")

    def top(self):
        if not self.is_empty():
            return self.head.next.data
        else:
            raise IndexError("stack is empty")

class Test():
    def BracketMatch(self,str1):
        ls = Stack()
        i = 0
        while i < len(str1):
            if str1[i] == "(" or str1[i] == "{" or str1[i]=="[":
                ls.push(str1[i])
                i+=1
                print("push",i)
                continue
            elif ls.get_size() == 0:
                return False
            if (str1[i] == ")" and ls.top()=="(") or (str1[i] == "}" and ls.top()=="{") or (str1[i] == "]" and ls.top()=="["):
                ls.pop()
                print("pop",i)
                i+=1
            else:
                i+=1
        if ls.get_size() != 0 :
            return False
        print(ls.get_size())
        return True





# s = Stack()
# s.push(1)
# s.push(2)
# print(s.get_size())
# s.pop()
# print(s.get_size())
# print(s.get_size())
test = Test()
print(test.BracketMatch("{{(}})"))
