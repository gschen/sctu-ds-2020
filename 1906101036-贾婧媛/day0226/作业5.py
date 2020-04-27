#5、（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
x,y,z = map(int,input().split())
list = [x,y,z]
n = 0
def jia(list,n):
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            list[i],list[i+1] = list[i+1],list[i]
    if n == len(list): #n是一个计数，n=3时函数就递归了三次，每经过一次递归，
        return list    #列表元素就会做一次调整，最多需要经过列表长度次递归，
    else:              #所以为不出错，设置最大次数递归，即列表长度次
        return jia(list,n+1)
print(jia(list,n))