#5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。

x=input('请输入第一个整数：')
y=input('请输入第二个整数：')
z=input('请输入第三个整数：')
arr = [x,y,z]
for i in range(0,3):
    for j in range(i,3):
        if int(arr[i])>int(arr[j]):
            k = arr[i]
            arr[i] = arr[j]
            arr[j] = k
print(arr)