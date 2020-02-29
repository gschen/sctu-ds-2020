
#7
def my_shun(l):
    a=0;b=0;c=0;d=0
    for i in l:
        if i.isdigit():
            a += 1
        elif i.isalpha():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    print(a,b,c,d)
print('请输入一个列表l[]')
l = list(map(str,input().split(',')))
print(my_shun(l))