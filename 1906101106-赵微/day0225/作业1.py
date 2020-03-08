
#必做
'''
1.	（使用def函数完成）设f(x)=3x4-9x2+x/2，请将f(x)封装为一个函数，求当x等于以下值时，f(x)是多少.
X取值：54,96,83,64,234,158,364
'''



def f(x):
    return 3*4-9*2+x/2
print(f(54), f(96), f(83), f(64), f(234), f(158), f(364))






'''
2.	（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.

样例输入
85
样例输出
B
'''





def g(n):
    
    if 90<=n<=100:
        print("A")
    elif 80<=n<90:
        print("B")
    elif 60<=n<80:
        print("C")
    else:
        print("D")
n = int(input("请输入你的成绩："))
print(g(n))



'''
3.	（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表

样例输入
	1,2,3,4,5,6,7
样例输出
1, 3, 5, 7
'''

def f(L1):
    
    L2 = []
    for i in range(len(L1)+1):
        if i % 2 == 1:
            L2.append(i)  #把这些位置的元素添加到空列表
    return L2
L1 = [1, 2, 3, 4, 5, 6, 7]  
print(f(L1))


#法2
def f(L1):
    return L1[::2]   #切片，从第一位到最后一位，中间步数为2


L1 = [1, 2, 3, 4, 5, 6, 7]
print(f(L1))








'''
4.	（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
num = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j)and (j != k)and (k != i):
                num += 1  # print("{}{}{}".format(i,j,k))
                print(i, j, k) 








'''
5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
'''
x = int(input('第一个整数x：'))
y = int(input('第二个整数x：'))
z = int(input('第三个整数x：'))
if y < x:
    x, y = y, x
if z < x:
    x, z = z, x
if z < y:
    y, z = z, y

print(x, y, z)

#法2
x,y,z = map(int,input().split())   #split分隔，括号为空则以空格分隔。split(',')代表以逗号分隔
ls = [x,y,z]
ls.sort()
print(ls)













'''
选做
6.	（使用def函数完成）编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n











7.	（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
样例输入
D,a, ,s,1,3,2, ,a,2,d,a
样例输出
4, 6, 3, 0



'''







