#测试括号
class Test():
    def Brack(self,str):
        ls = Stack()
        i = 0
        while i < len(str1):
            if str[i] == "(" or str[i] == "[" or str[i] == "{":
                ls.push(str[i])
                i += 1
                continue
            elif ls.get_size == 0:
                return False
            if (str[i] == ")" and ls.top() == "(" ) or (str[i] == "]" and ls.top() == "[" ) or ( str[i] == "}" and ls.top() == "{" )
                ls.pop()
                i += 1
            else:
                return False
        if ls.get_size() != 0:
            return False
        return True