
#回文问题
'''
输入是什么
输出是什么
算法是什么
'''
def huiwen(s):

    stack=list(s)
    res=''
    while len(stack)>0:
        res+=stack.pop()
    if res==s:
        return True
    return False

s='abcba'
print(huiwen(s))



