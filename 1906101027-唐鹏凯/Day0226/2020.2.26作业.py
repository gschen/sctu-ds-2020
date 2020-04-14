#第一题
def fx(x):
    s = (x**4)-(9*x**2)+(x/2)
    return s
x = int(input("enter your number:"))
print(fx(x))

#第二题
def grades(x):
    if 90<=x<=100:
        return "A"
    if 80<=x<90:
        return "B"
    if 60<=x<80:
        return "C"
    if x<60:
        return "D"
x = float(input("输入您的分数:"))
print(grades(x))

#第三题
def list1(x):
    s = x[::2]
    return s
x = [1,2,3,4,5,6,7]
print(list1(x))

#第四题
sum = 0
for i in range(1,5):
    for s in range(1,5):
        for x in range(1,5):
            if i != s and i != x and s != x :
                sum +=1
                print("分别是",i,s,x)
print("共有：",sum,"个")

#第五题
x,y,z = map(str,input().split())
l = [x,y,z]
for i in range(0,3):
    for j in range(i,3):
        if int(l[i]) > int(l[j]):
            s = l[i]
            l[i] = l[j]
            l[j] = s

print(l)

#第六题
a = 1
b = 2
c = 1
sum = 0
x = int(input())
def N(x):
    global a,b,c,sum
    if x % 2 == 0:
        for i in range(x):
            sum = a/b + sum
            a,b = a,b*2
    else:
        for i in range(x):
            sum = a/c + sum
            a,c = a,c+2
    return sum
print(N(x))

#第七题
def N(x):
    a,b,c,d=0,0,0,0
    for i in x:
        if i.isalpha():
            a+=1
        elif i.isdigit():
            b+=1
        elif i.isspace():
            c+=1
        else:
            d+=1
    return '英文字符数{},数字字符数{},空格字符数{},其他字符数{}'.format(a,b,c,d)
x = input()
print(N(x))