#5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。

x,y,z=map(int,input('输入三个整数：').split(','))
s=[x,y,z]
n=len(s)
for i in range(n):
    for j in range(n-i-1):
        if s[j]>s[j+1]:
            s[j],s[j+1]=s[j+1],s[j]
for i in range(n):
    print(s[i])


#起泡排序，别名“冒泡排序”，该算法的核心思想是将无序表中的所有记录，通过两两比较关键字，得出升序序列或者降序序列。