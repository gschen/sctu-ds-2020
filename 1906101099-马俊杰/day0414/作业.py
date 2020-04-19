#用递归求n的阶乘

def fact(n):
    if n == 1:
        return 1
    result = n * fact(n - 1)
    return result
n=int(input('请输入一个值：'))    
print (fact(n))