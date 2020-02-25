"""
def APluSB(a,b):
    return a+b
result =APluSB(1,2)
print(result)

def circle(r):
    return r**2*3.14
print(circle(5))
print(circle(10))

a=2
def main():
    b=3
    print(a)
main()
print(b)
"""
#lambda函数：格式；变量名=lambda 参数1 参数2 返回
circle=lambda r,pi:r**2*pi
print(circle(3,3.14))