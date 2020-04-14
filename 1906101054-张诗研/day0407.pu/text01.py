class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack(object):
    def __init__(self):
        self.node=Node(None)
        self.head=self.node
        self.size=0
    def is_empty(self):
        return self.size==0
    def get_size(self):
        return self.size
    def push(self,data):
        node=Node(data)
        node.next=self.head.next
        self.head.next=node
        self.size+=1
    def pop(self):
        if not self.is_empty():
            current_node=self.head.next
            if self.get_size()==1:
                self.head.next=None
                self.size-=1
            else:
                self.head.next=self.node.next.next
                self.size-=1
                return current_node.data
        else:
            print("empty")
    def top(self):
        if not self.is_empty():
            return self.head.next.data
        else:
            print("empty")



class Text():
    def BracketMatch(self,str1):
        Is=Stack()
        i=0
        while i<len(str1):
            if str1[i]=="(" or str1[i]=="[" or str1[i]=="{":
                Is.push(str1[i])
                i+=1
                continue
            elif Is.get_size==0:
                return False
            if (str1[i]==")" and Is.top()=="(" or str1[i]=="]" and Is.top()=="[" or str1[i]=="}"  and Is.top()=="{"):
                Is.pop()
                i+=1
            else:
                return False
        if Is.get_size()!=0:
            return False
        else:
            return True

test=Text()
print(test.BracketMatch("()()()()({{{{"))
<<<<<<< HEAD
=======

>>>>>>> 42f7e6696cd46b332b07cf06f9f1dddc2e18ce48
        

            