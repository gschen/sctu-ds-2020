#1
x = int(input())
wrong_nums = [1,10,20,30,40,50]
def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)
if x in wrong_nums:
    print(False)
else:
    print(factorial(x))

#2
P,T,R = map(int,input().split())
print((P*T*R)/100)

#3
print(max([14,25,98,75,23,1,4,56,59]))

#4
nums = [14,25,98,75,23,1,4,56,59]
n = int(input())
def squre(x):
    return x*x
print(sum(map(squre,nums[:n])))

#5
a,b = map(int,input().split())
nums = [14,25,98,75,23,1,4,56,59]
num_a,num_b = nums[a],nums[b]
nums[b],nums[a] = num_a,num_b
print(nums)
