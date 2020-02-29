#习题1
lis=[54,96,83,64,234,158,364]
for i in lis:
    def asd(i):
        return 3*i**4-9*i**2+i/2
    print(asd(i))

#习题2
n=int(input('请输入成绩：'))
def chengji(n):
    if n>=90 and n<=100:
        return 'A'
    if n>=80 and n<90:
        return 'B'
    if n>=60 and n<80:
        return 'C'
    if n<60:
        return 'D'
print(chengji(n))

#习题3
li = []
def jishu(n):
    for i in range(len(n)):
        if i % 2 == 0:
            li.append(n[i])
    return li
ret = jishu([1,2,3,4,5,6,7])
print(ret)

#习题4
n=0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a!=b and b!=c and c!=a:
                n+=1
                print(a,b,c)
print(n)

#习题5
x,y,z=map(int,input('请输入x,y,z:').split())
if x>y>z:
    print(z,y,x)
elif x>z>y:
    print(y,z,x)
elif y>x>z:
    print(z,x,y)
elif y>z>x:
    print(x,z,y)
elif z>x>y:
    print(y,x,z)
else:
    print(x,y,z)

#习题6
n=int(input('请输入一个数：'))
def asd(n):
        sum=0
        if n==1:
            return 1/1
        elif n==2:
            return 1/2
        else:
            return 1/n+asd(n-2)
print('函数求和结果为：',asd(n))

#习题7
n=input('输入一行字符:\n')
a,b,c,d=0,0,0,0
for i in n:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        b+=1
    elif i.isspace():
        c+=1
    else:
        d+=1
print(a,b,c,d)


    
    
        

    

