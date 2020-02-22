#求数组中的前n个数的平方和.




list=[14,25,98,75,23,1,4,56,59]
n=int(input('请输入一个数（n小于等于9）:'))
m=0
for x in list:
    while n>0:
        m=m+x**2
        n=n-1