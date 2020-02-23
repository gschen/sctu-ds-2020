#4、求数组前n个数的平方和
lis1=[14,25,98,75,23,1,4,56,59]
s=0
n=int(input("计算前n个数,n为："))
m=list(lis1[:n])
if n <9:
     for x in m:
          x=x**2
          s+=x
     print("平方和为: %d" %(s))

else:
     print("抱歉，n为正整数且不能大于数组长度9,请重新输入。")
