#第一题
def f(*x):
    for i in x:
        a=3*i**4-9*i**2+i/2
        print(a)
    f(54,96,83,64,234,158,364)
#第二题
def hs(x):
    if x=<100 and x>90:
        return 'A'
    elif x=<90 and x>80:
        return 'B'
    elif x=<80 and x>60:
        return 'C'
    else x=<60:
        return 'D'
print(hs(x=85)