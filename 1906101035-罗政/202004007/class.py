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


               
