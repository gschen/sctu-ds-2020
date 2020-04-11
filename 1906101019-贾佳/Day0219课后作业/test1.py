def func(n):
    if n ==1:
        return 1
    else:
        return n * func(n - 1)
n = int(input())
if n in [1,10,20,30,40,50]:
    print("Wrongly Input")
else:
    print(func(n))
