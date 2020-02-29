num=int(input("输"))
if num %2 ==0:
    if num  % 3==0:
        print("能被两个整除")
    else:
        print("能被2，不能被3")
else:
    if num %3 ==0:
        print("能被3，不能被2")
    else:
        print("不能被2，不能被3")