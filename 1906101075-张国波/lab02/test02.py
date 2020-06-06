
'''
编程实现括号匹配
输入:{[()]}
输出:True
'''
stack=[]
left = ['{','[','(']
right = ['}',']',')']

def match(s):

    for i in s:
        if i in left:
            stack.append(i)

        if i in right:
            j=stack.pop()

            if right.index(i)!=left.index(j):
                return False

    if len(stack)!=0:
        return False
    return True

print(match('[[[()]]]'))