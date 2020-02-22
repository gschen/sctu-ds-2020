'''4、求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
要求：n需要是input输入，且小于数组长度，不能固定'''

n=int(input("请输入一个正整数:"))
list= [14,25,98,75,23,1,4,56,59]
sum=0
if n > 9:
    print("输入有误！")
else:
    for i in range(n):
        sum = sum+list[i]**2
    print(sum)