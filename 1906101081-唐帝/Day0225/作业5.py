a,b,c = map(int, input('请输入3个数：').split())
if a>b:
    if a>c:
        a=a
        if b>c:
            b=b
    if a<c:
        a,b,c=c,a,b
elif a<b:
    if a<c:
        if b>c:
            a,b,c=b,c,a
        if c>b:
            a,b,c=c,b,a

print(c)
print(b)
print(a)
#  ..