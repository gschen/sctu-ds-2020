 a= int(input())
wrong_nums = [1,10,20,30,40,50]
def factorial(a):
    if a == 0:
        return 1
    else:
        return a*factorial(a-1)
if a in wrong_nums:
    print(False)
else:
    print(factorial(a))



P,T,R = map(int,input().split())
print((P*T*R)/100)



print(max([14,25,98,75,23,1,4,56,59]))



nums = [14,25,98,75,23,1,4,56,59]
n = int(input())
def squre(x):
    return x*x
print(sum(map(squre,nums[:n])))



a,b = map(int,input().split())
nums = [14,25,98,75,23,1,4,56,59]
num_a,num_b = nums[a],nums[b]
nums[b],nums[a] = num_a,num_b
print(nums)