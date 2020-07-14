"""回文数实现"""

k = "abca"

def huiwen(k):
    s = ""
    l = list(k)
    for i in range(len(l)):
         s += l.pop()
         
    if k == s:
        return True
    return False

print(huiwen(k))
