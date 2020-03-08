'''6、（使用def函数完成）编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
当输入n为奇数时，调用函数1/1+1/3+...+1/n'''
def jia(n,sum):
    sum = sum + 1/n
    if n == 1 or n == 2:
        return sum
    else:
        return jia(n-2,sum)
sum = 0
n = input()
print(jia(n,sum))