n=int(input('请输入一个数：'))
x=[1,10,20,30,40,50]
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return (n*factorial(n-1))
    if n in x:
        print(False)
    else:
        print(factorial(n))
#
R,T,P=map(int,input().split())
print((P*T*R)/100)
#
print(max[14,25,98,75,23,1,4,56,59])
#
nums=[14,25,98,75,23,1,4,56,59]
n=int(input())
def squre(x):
    renturn x*x
print(sum(map(squre,nums[:n])))
#
a,b=map(int,input().split())
nums=[14,25,98,75,23,1,4,56,59]
num_a,num_b=nums[a],nums[b]
nums[b],nums[a]=num_a,num_b
print(nums)