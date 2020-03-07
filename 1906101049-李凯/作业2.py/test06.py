'''6.	（使用def函数完成）编写一个函数，输入n为偶数时，
调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n'''
def num(n):
    s=0
    if n%2==0:
        for i in range(2,n+1,2):
            k=1/i
            s+=k
        return s
    else:
        for ii in range(1,n+1,2):
            kk=1/ii
            s+=kk
        return s
print(num(4))
print(num(5))
