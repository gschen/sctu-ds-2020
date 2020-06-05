stack = []
left  = ["{","[","("]
right = ["}","]",")"]

# 判断给定的字符串是否括号匹配
def match(s):
    
    for i in s:
        #如果i是左括号,压栈
        if i in left:
            stack.append(i)

        #如果i是右括号，出栈
        if i in right:
            # 需要考虑特殊情况，第一个字符是右括号
            if len(stack) ==0:
                return False

            j = stack.pop() # i是右括号，j是左括号
        else: #若不是括号，则直接不匹配
            return False

        if right.index(i) != left.index(j): #判断当前括号是否匹配，用下标匹配
            return False
            
    if len(stack) != 0:
        return False

    return True

print(match('[[[]]]'))