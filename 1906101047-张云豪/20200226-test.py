#1
def m(x): 
    s=(3*x**4)-(9*x**2)+x/2
    return s
print(list(map(m,[54,96,83,64,234,158,364])))



#2
def score(x):
    if 90 <= x <= 100:
        print('A')
    elif 80 <= x < 90:
        print('B')
    elif 60 <= x < 80:
        print('C')
    else:
        print('D')


#3
def serch(l):
    l2=[]
    for i in l:
        if i % 2 == 1:
            l2.append(i)
    return l2
print(serch([1,2,3,4,5,6,7,8,9]))


#4
l=[1,2,3,4]
count=0
for i in l:
    l2=[]
    for j in l:
        for k in l:
            if i !=j and j!=k and i!=k:
                count +=1
                print('{},{},{}'.format(i,j,k))
print('一共有%d个'%count)
                

#5
x=input('请输入第一个整数:')
y=input('请输入第二个整数:')
z=input('请输入第三个整数:')
if x>y:
    x,y = y,x
if x>z:
    x,z = z,x
if y>z:
    y,z = z,y
print(x,y,z)


#6
def s(n):
    l=[]
    l2=[]
    if n == 1:
        return 1
    if n % 2 == 0:
        for i in range(1,n+1):
            sum=0
            if i % 2 == 0:
                l.append(i)
                for k in l:
                    sum=sum+1/k
                    return sum
    if n % 2 == 1:
        for j in range(1,n+1):
            sum2=0
            if h % 2 == 1:
                l2.append(h)
                for m in l2:
                    sum2=sum+1/m
                    return sum2


#7
s=input('请输入一行字符串:')
英文字符=[]
数字=[]
空格=[]
其他字符=[]
for i in iter(s):
    if i.isalpha():
        英文字符.append(i)
    elif i.isdigit():
        数字.append(i)
    elif i.isspace():
        空格.append(i)
    else:
        其他字符.append(i)
print('''
	英文字符:{},个数:{}
	数字:{},个数:{}
	空格:{},个数:{}
	其他字符:{},个数:{}'''\
	.format(英文字符,len(英文字符),	数字,len(数字),空格,len(空格),其他字符,len(其他字符)))	

 