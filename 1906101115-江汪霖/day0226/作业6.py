
def abc(n):
    s = 0
    if n % 2 == 0:
        for i in range(2,n+1,2):
            a = 1/i
            s = s + a
        print(s)
    else:
        for i in range (1,n+1,2):
            a = 1/i
            s = s + a
        print(s)
n = int(input('请输入n:'))
abc(n)

