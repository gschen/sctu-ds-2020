'''
用递归求n的阶乘
n! = (n-1)!*n = (n-2)!*(n-1)*n = 1*(n-a)*...*(n-2)*(n-1)*n
'''

n = int(input())
def jia(n):
    if n == 0:
        return 1
    return jia(n-1)*n
print(jia(n))