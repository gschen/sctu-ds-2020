#1.	（使用def函数完成）设f(x)=3x4-9x2+x/2，请将f(x)封装为一个函数，求当x等于以下值时，f(x)是多少.
# X取值：54,96,83,64,234,158,364
def f(x):
    return 3*x**4-9*x**2+x/2
for x in [54,96,83,64,234,158,364]:
    print(f(x))


#2.	（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.
# 样例输入  85
# 样例输出   B
n = int(input("请输入成绩："))
def main(n):
    if 90 <= n <= 100:
        return 'A'
    elif 80 <= n < 90:
        return 'B'
    elif 60 <= n < 80:
        return 'C'
    elif n < 60:
        return 'D'
print(main(n))


# 3.	（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表
# 样例输入
# 	1,2,3,4,5,6,7
# 样例输出
# 1, 3, 5, 7
def mai(*x):
    list1=[]
    y=len(x)
    for i in range(0,y,2):
        list1.append(x[i])
    print(list1)
mai(1,2,3,4,5,6,7)


# 4.	（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
count=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (i!=k) and (j!=k):
                count=count+1
                print(str(i)+str(j)+str(k),end=' ')
print('')
print('最终结果为：%s个'%count)


# 5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
x,y,z=map(int,input("输入三个整数：").split(','))
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print(x,y,z)



# 选做
# 6.	（使用def函数完成）编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
n=int(input("请输入n:"))
def he(n):
    sum=0
    if n % 2==0:
        for x in range(2,n+1,2):
            y=1/x
            sum=sum+y
        return sum
    else :
        for x in range(1,n+1,2):
            y=1/x
            sum=sum+y
        return sum
print(he(n))


# 7.	（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
# 样例输入
# D,a, ,s,1,3,2, ,a,2,d,a
# 样例输出
# 4, 6, 3, 0
def count_strs(strs):
    char_number,num_number,space_number,other_number=0,0,0,0
    for i in strs:
        if i.isalpha():
            char_number+=1
        elif i.isdigit():
            num_number+=1
        elif i==' ':
            space_number+=1
        else:
            other_number+=1
    print('字符串中有%d个字母，%d个数字，%d个空格，%d个其他字符'%(char_number,num_number,space_number,other_number))
count_strs('Da s132 a2da')