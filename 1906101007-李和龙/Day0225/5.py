"""
使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。

"""
a,b,c = map(int,input().split())
list1 = [a,b,c]
for i in range(3):
    for m in range(i,3):
        if list1[i] > list1[m]:
            list1[i],list1[m] = list1[m],list1[i]
print(list1)

