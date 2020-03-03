# 6. 数列
def sl(n):
    if n == 0:
        return '重新输入'
    else:
        s = 0
        if n % 2 == 0:
            for i in range(2, n + 1, 2):
                s += 1 / i
            return s
        else:
            for i in range(1, n + 1, 2):
                s += 1 / i
            return s


print(sl(3))