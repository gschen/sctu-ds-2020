n=int(input("请输入一个正整数:"))
list=[14,25,98,75,23,1,4,56,59]
sum=0
if n > 9:
    print("输入有误！")
else:
    for i in range(n):
        sum = sum+list[i]**2
        print(sum)
