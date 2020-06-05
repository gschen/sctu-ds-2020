

#回文问题
'''
输入是什么
输出是什么
算法是什么
'''
stack = []
def huiwen(s):
    l = list(s)
    n = ''
    n += l.pop()
    if n == s:
        return True
    else:
        return False
s = 'abba'
print(huiwen(s))