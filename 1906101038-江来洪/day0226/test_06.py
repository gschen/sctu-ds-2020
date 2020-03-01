def jiang(n,sum):
    sum += 1/n
    if n == 2 or n == 1:
        return sum
    else:
        return jiang(n-2,sum)
sum = 0
n = int(input())
print(jiang(n,sum))

