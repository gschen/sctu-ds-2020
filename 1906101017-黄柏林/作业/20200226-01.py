# 1.	（使用def函数完成）设f(x)=3x4-9x2+x/2，请将f(x)封装为一个函数，求当x等于以下值时，f(x)是多少.
# X取值：54,96,83,64,234,158,364


list=(54,96,83,64,234,158,364)
for x in list:
    def jisuan(x):
        a=3*x*x*x*x
        b=9*x*x
        c=x/2
        y=a-b+c
        return y
    print(jisuan(x))