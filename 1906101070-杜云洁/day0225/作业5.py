#5.（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
nums=map(int,input('请输入三个不等整数：').split(' '))
for i in sorted(nums):
    print(i)
