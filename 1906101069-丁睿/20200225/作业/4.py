x=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (i!=k) and (j!=k):
                x+=1
                print(str(i)+str(j)+str(k),end=" ")
print(" ")
print("最终结果是：%s个"%x)