#1.	（使用def函数完成）设f(x)=3x的4次方-9x的2次方+x/2，请将f(x)封装为一个函数，求当x等于以下值时，f(x)是多少.
#X取值：54,96,83,64,234,158,364

x = int(input('请输入一个数：'))
def tang(x):
    p = 3*x**4-9*x**2+x/2
    return p
print(tang(x))