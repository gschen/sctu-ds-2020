# （使用def函数完成）编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，
# 调用函数1/1+1/3+...+1/n
def math(n):
    sum=0
    for i in range(1,int(n+1)+1):
        sum =sum+1/(2*i)
        print(sum)
def num(n):
    sum=0
    for i in range(1,int((n+1)/2)+1):
        sum=sum+1/(2*i-1)
        print(sum)
n=int(input('请输入:'))
if (n%2==0):
    math(n)
else:
    num(n)