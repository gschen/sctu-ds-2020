#第一题
n=int(input())
m=[1,10,20,30,40,50]
def nian(n):
    if n == 0:
        return 1
    else:
        return n*nian(n-1)

if n in m:
    print("请重新输入")
else:
    print(nian(n))

#第二题
P = int(input())
R = int(input())
T = int(input())
S = (P*R*T)/100
print("输出%d"%(S))

#第三题
print(max([14,25,98,75,23,1,4,56,59]))

#第四题
list=[14,25,98,75,23,1,4,56,59]
n=int(input())
def nian(m):
    return m*m
print(sum(map(nian,list[:n])))

#第五题
a,b = map(int,input().split())
nums = [14,25,98,75,23,1,4,56,59]
num_a,num_b = nums[a],nums[b]
nums[b],nums[a] = num_a,num_b
print(nums)


