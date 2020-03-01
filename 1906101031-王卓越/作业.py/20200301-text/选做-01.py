# 6.	（使用def函数完成）编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
from fractions import Fraction
def method(n):
    sums=0
    if n%2==0:
        x=2
        while x<=n:
            sums+=Fraction(1,x)
            x+=2
        return sums
    else:
        x=1
        while x<=n:
            sums+=Fraction(1,x)
            x+=2
        return sums
print(method(7))
