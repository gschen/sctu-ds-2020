'''1、（使用def函数完成）设f(x)=3*x**4-9*x**2+x/2，请将f(x)封装为一个函数，求当x等于以下值时，f(x)是多少.
X取值：54,96,83,64,234,158,364'''

def f(x):
    return 3*x**4-9*x**2+x/2
list=[54,96,83,64,234,158,364]
for i in range(len(list)):
    x=list[i]
    print('f(%d)=%d'%(x,f(x)))
