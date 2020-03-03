def f(x):
    sum=0
    if x %2 == 0:
        for i in range(2,x+1,2): 
             sum += 1/i
        return sum
    else :
        for i in range(1, x+1, 2):
            sum += 1/i
        return sum
print(f(int(input())))