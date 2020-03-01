a = 1
b = 2
c = 1
sum = 0
x = int(input())
def N(x):
    global a,b,c,sum
    if x % 2 == 0:
        for i in range(x):
            sum = a/b + sum
            a,b = a,b*2
    else:
        for i in range(x):
            sum = a/c + sum
            a,c = a,c+2
    return sum
print(N(x))