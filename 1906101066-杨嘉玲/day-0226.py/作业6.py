def function(n):
    if n % 2 == 0:
        m = int(n/2 + 1)
        s = 0
        for i in range(1,m):
            s += 1/(2*i)
        return s
    else:
        m = int((n+1)/2 + 1)
        s = 0
        for i in range(1,m):
            s += 1/(2*i - 1)
        return s       
n = int(input("请输入一个整数："))
result = function(n)
print("输出结果为：{}".format(result))
    