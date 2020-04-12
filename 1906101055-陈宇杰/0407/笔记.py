class Node(object):
    def_init_(self.data)：
      self.data = data   
      self.next = None

class Stack(object):
    def_init_(self)：
       self.node = Node(Node)
       self.head = self.node
       self.size = non0
    def is_empty(self):
        return self.size == 0
    def get_ size(self):
        return self . size
    def push(self , data):
        node = Node(data )
        node . next =
        self . head . next
        self . head.next = node
        self .size += 1
    def pop(se1f):
        if not self.is_ empty():
           current_node = self.head.next
        if self.get_size() == 1:
            self.head.next= None
            self .size -= 1
        else:
            self .head.next = self . head. next . next
            self .size-= 1
            return current_ node. data 
        else:
            print("栈为空! ")
    def top(self):
        if not self.is_ empty():




class Text():
    def bracketMatch(self,str):
        Is = stack()
        i = 0
        while i < len(str1)
        if str1[i] == "("or str[i] == or str1[i] =="{":
                Is. push( str1[i] )
                i+=1
                continue
        elif ls.get_ size == 0:
            return False
        if (str1[i] == ")" and Is.top() == "(") or (str[i] == "]" and Is,top() == "[") or (str[i] == "}" and Is,top() == "}" == "[")
            ls.pop()
            i+=1
        else:
            return False
        if ls.get_ size() != 0:
            return False
        return True

        
test = Test()
print( test . BracketMatch("()()()())"))
