def intro(x):
    result = 3*x**4-9*x**2+x/2
    return result
list = [54,96,83,64,234,158,364]
for i in list:
    intro(i)
    print("当数为%d时，输出为：%d"%(i,intro(i)))