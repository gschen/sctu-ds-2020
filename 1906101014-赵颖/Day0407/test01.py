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
            if (str1[i] == ")" and ls.top() == "(") or (str1[i] == "]" and ls.top() == "[") or (str1[i] == "}" and ls.top() == "{") 
                ls.top()
                i+=1
            else:
                return False
        if ls.get_size() != 0:
            return False
        return True
test = Test()
print(test.BracketMacth("()()()()){{{{"))
