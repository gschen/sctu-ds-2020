def f(x):
    return 3*(x**4)-9*(x**2)+x/2
x_nums = [54,96,83,64,234,158,364]
for x in x_nums:
    print('f(%d)=%d' % (x,f(x)))