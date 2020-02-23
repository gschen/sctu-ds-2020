#NO.1

def fact(n):
    if n ==1:
        return 1
    if n ==10:
        return 10
    if n ==20:
        return 20
    if n ==30:
        return 30
    if n ==40:
        return 40
    if n ==50:
        return 50
    return n*fact(n-1)
print (fact(32))



#NO.2
P=int(input('本金是：'))
T=int(input('时间是：'))
R=int(input('利率是：'))
X=(P*T*R)/100
print(X)





#NO.3
list1=[14,25,98,75,23,1,4,56,59]
print(max(list1))




#NO.4
n=int(input('n的值大于0，且小于10：'))
def f(n):
    return n*n
r=map(f,[14,25,98,75,23,1,4,56,59])
print(list(r))




#NO.5
list=[14,25,98,75,23,1,4,56,59]
list[N1]='N2'
N1=int(input('输入列表所要被替换的数字位数：'))
N2=input('输入想要替换的数字：')
print(list)