...
2.编程实现括号匹配
输入：{[()]}
输出：True
...

stack = []
left = ['{','[','(']
right = ['}',']',')']

#判定给定的字符串是否括号匹配
def match(s):

    for i in s:
        # 如果i是左括号,压栈
        if i in left:
            stack.append(i)

        # 如果i是右括号，出栈
        if i in right:
            # 需要考虑特殊情况，第一个字符就是右括号
            if len(stack) == 0:
                return False
                
            j = stack.pop() # i是右括号，j是左括号

            # 判断当前的右括号与出栈的左括号是否匹配
            if right.index(i) == left.index(j):
                return False

    # ((()))
    if len(stack) != 0:
        return False

    return True

print(match('(({'))