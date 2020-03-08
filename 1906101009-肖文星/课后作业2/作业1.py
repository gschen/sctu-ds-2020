lis=[54,96,83,64,234,158,364]
lis1=[]
def f():
    for x in lis:
        ans=3*x**4-9*x**2+x/2
        lis1.append(ans)
    return lis1
print(f())