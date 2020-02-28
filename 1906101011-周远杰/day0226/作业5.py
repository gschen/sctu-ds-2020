# （使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
x,y,z=map(int,input().split())
m=[x,y,z]
for a in m:
    for b in m:
        for c in m:
            if a!=b and a!=c and b!=c:
                if a>b>c:
                    print(c,b,a)
                elif a>c>b:
                    print(b,c,a)
                elif b>c>a:
                    print(a,c,b)
                elif b>a>c:
                    print(c,a,b)
                elif c>a>b:
                    print(b,a,c)
                else:
                    print(a,b,c)
    break