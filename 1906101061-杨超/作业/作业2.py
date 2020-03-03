'''1.	（使用def函数完成）设f(x)=3x4-9x2+x/2，请将f(x)封装为一个函数，求当x等于以下值时，
f(x)是多少.X取值：54,96,83,64,234,158,364'''
def f(x): 
    y = 3*x**4-9*x**2+x/2
    return y
print(list(map(f,[54,96,83,64,234,158,364])))

'''2.	（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A,80-90为B，
60-80为C,60分以下为D.
样例输入:85
样例输出:B'''
x = int(input("请输入你的成绩： "))
def grade(x):
    if 90 <= x <= 100:
        return "你的成绩等级为A"
    elif 80 <= x < 90:
        return"你的成绩等级为B"
    elif 60 <= x <80:
        return "你的成绩等级为C"
    else:
        return "你的成绩等级为D"
print(grade(x))

'''3.	（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表
样例输入:1,2,3,4,5,6,7
样例输出:1, 3, 5, 7'''
def odd_number(x):
    oddnumber = []
    for i in x:
        if i%2 == 1:
            oddnumber.append(i)
    return(oddnumber)
print(odd_number([1,2,3,4,5,6,7]))
'''4.	（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位
数？各是多少？'''
num=[1,2,3,4]
count = 0
for a in num:
    for b in num:
        for c in num:
            if a !=b and a!=c and b!=c:
                count +=1
                print('{},{},{}'.format(a,b,c))
print("一共有%d个"%count)

'''5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。'''
x = int(input("请输入第一个数： "))
y = int(input("请输入第二个数： "))
z = int(input("请输入第三个数： "))
if x > y:
    x,y = y,x
if x > z:9
    x,z = z,x
if y > z:
    y,z = z,y
print(x,y,z)