x = int(input("请输入一个整数:"))
list = [1,10,20,30,40,50]
def jia(x):
    if x == 0:
        return 1
else:
    return x*jia(x-1)
if x in list or x < 0 :
    print('不能输入此数！')
else:
    print(jia(x))
