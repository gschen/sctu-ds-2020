#求数组中的前n个和
list=[14,25,98,75,23,1,4,56,59]
n=int(input("输入数字:"))
def H(x):
    return x*x
print(sum(map(H,list[:n])))




