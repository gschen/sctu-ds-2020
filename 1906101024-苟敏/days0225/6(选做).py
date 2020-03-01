n=int(input("请输入n:"))
def num(n):
    s=0
    if n%2==0:
        for i in range(2,n+1,2):
            j=1/i
            s+=j
        return s
    else:
        for i2 in range(1,n+1,2):
            j2=1/i2
            s+=j2
        return s
print(num(n))