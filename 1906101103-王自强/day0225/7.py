# 7. 统计
def tj(x):
    z, s, k, q = 0, 0, 0, 0
    for i in x:
        if i in list(map(chr, list(range(97, 123)))) or i in list(map(chr, list(range(65, 91)))):
            z += 1
        elif i in list(map(str, list(range(10)))):
            s += 1
        elif i == ' ':
            k += 1
        else:
            q += 1
    return z, s, k, q


x = 'D,a, ,s,1,3,2, ,a,2,d,a, '.split(',')
print(x)
print(tj(x))
