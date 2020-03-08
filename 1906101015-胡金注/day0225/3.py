def f(x):
    lis1 = []
    Q = len(x)
    for i in range(0,Q,2):
        lis1.append(x[i])
    return lis1
print(f(eval(input())))
