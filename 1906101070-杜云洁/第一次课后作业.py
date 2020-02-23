#第一题
n=eval(input('请输入一个非负整数:'))
a=1
if n==1 or n==10 or n==20 or n==30 or n==30 or n==40 or n==50:
    print('不能输入这个数')
elif n==0:
    print(1)
else:
    for i in range(1,n+1):
        a=a*i
    print(a)
#第二题
p=int(input())
t=int(input())
r=int(input())
a=(p*t*r)/100
print(a)
#第三题
nums=[14,25,98,75,23,1,4,56,59]
nums.sort()
print('最大的元素为：',nums[-1])
#第四题
nums=[14,25,98,75,23,1,4,56,59]
n=int(input())
sum=0
if n<len(nums):
    while n>0:
        sum=sum+nums[n-1]**2
        n=n-1
    print(sum)
#第五题
import random
nums=[14,25,98,75,23,1,4,56,59]
a=int(input())
b=int(input())
c=random.randint(1,len(nums))
d=random.randint(1,len(nums))
nums[c]=a
nums[d]=b
print(nums)
