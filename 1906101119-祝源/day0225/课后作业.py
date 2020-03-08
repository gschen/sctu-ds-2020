# 第一题.设f(x)=3x4-9x2+x/2，请将f(x)封装为一个函数，求当x等于以下值时，f(x)是多少？ X取值：54,96,83,64,234,158,364

list1 = [54,96,83,64,234,158,364]
def f(x):
    y = 3*x**4-9*x**2+x/2
    return y
for x in list1:
    print(f(x))


# 第二题.编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D

x = eval(input("请输入成绩："))
def f(x):
    if 90 <= x <= 100:
        print("A")
    elif 80 <= x < 90:
        print("B")
    elif 80 <= x <= 90:
        print("C")
    else:
        print("D")
    return x    
print(f(x))


# 第三题.找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表

def f(x):
    li1 = []
    for i in range(len(x)):
        if i%2 == 1:
            li1.append(x[i])
    return li1
print(f([1,2,3,4,5,6,7]))

# 第四题.（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

n=0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if(a != b) and (b != c) and (c != a):
                n = n+1
                print(a,b,c)
print("一共有%d组"%(n))

#第五题.输入三个整数x,y,z，请把这三个数由小到大输出

x = int(input('第一个整数：'))
y = int(input('第二个整数：'))
z = int(input('第三个整数：'))
lis1 = []
lis1.append(x)
lis1.append(y)
lis1.append(z)                        
for i in lis1:
    if x > y:
        x,y = y,x
    if y > z:
        y,z = z,y
    if x > z:
        x,z = z,x    
print(x,y,z)


#第六题.编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

def odd(n):   
    s = 0
    for i in range(1,n+1,2):        
        s = s+1/i    
    return s
def even(n):    
    s = 0    
    for i in range(2,n+1,2):        
        s = s+1/i        
    return s
n = int(input("请输入一个数："))
if n % 2 == 1:      
    print(odd(n))   
else:
    print(even(n))

#第七题.（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果

s = input('输入一行字符:\n')
i = 0
j = 0
k = 0
l = 0
for c in s:
    if c.isalpha():
        i += 1
    elif c.isspace():
        j += 1
    elif c.isdigit():
        k += 1
    else:
        l += 1
print('英文=%d,空格=%d,数字=%d,其他字符=%d'%(i,j,k,l))