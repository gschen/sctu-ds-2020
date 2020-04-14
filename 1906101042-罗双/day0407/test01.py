class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack(object):
    def __init__(self):
        # self.stack=[]
        self.node=Node(None)
        self.head=self.node
        self.size=0
    def is_empty(self):
        return self.size==0
    def get_size(self):
        return self.size
    # def top(self):#查看栈顶元素
    #     if self.stack:
    #         return self.stack[-1]
    def push(self,data):
        node=Node(data)
        node.next=self.head.next
        self.head.next=node
        self.size+=1
    def pop(self):
        if not self.is_empty():
            current_node=self.head.next #保存栈顶元素
            if self.get_size()==1:
                self.head.next=None
                self.size-=1
            else:
                self.head.next=self.head.next.next #将头节点指向栈顶的下一个节点
                self.size-=1
                return current_node.data
        else:
            print('栈为空')
    def top(self):
        if not self.is_empty():
            return self.head.next.data
        else:
            print("栈为空")

#括号匹配
class Test():
    def BracketMatch(self,str1):
        ls=Stack()
        i=0
        while i < len(str1):
            if str1[i] == "(" or str1[i] == "[" or str1[i] == "{":
                ls.push(str1[i])
                i+=1
                continue
            elif ls.get_size == 0:
                return False
            if (str1[i]==")" and ls.top()=="(") or (str1[i]=="]" and ls.top()=="[") or (str1[i]=="}" and ls.top()=="{"):
                ls.pop()
                i+=1
            else:
                return False
        if ls.get_size()!=0:
            return False
        return True

test=Test()
print(test.BracketMatch("()()()()){{{{"))
