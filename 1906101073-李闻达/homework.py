# 1、求给定数的阶乘 
x = eval(input('请输入一个数:')) 
y = 1 
if x==1 or x==10 or x==20 or x==30 or x==40 or x==50: 
    print('不能输入这个数') 
6 else: 
    for i in range(1,x+1): 
        y = y*i 
    print(y)  
 
 
# 2、求单利 
P = eval(input('请输入本金:')) 
T = eval(input('请输入时间:')) 
R = eval(input('请输入利率:')) 
SI = (p*t*r)/100 
print(SI)    

# 3、查找数组中的最大元素 
list =  [14,25,98,75,23,14,56,59] 
print(max(list))  
 
 

# 4、求前n个数的平方和 
n = eval(input('请输入一个数:')) 
L0 = [14,25,98,75,23,14,56,59] 
L1 = L0[0:n] 
sum = 0 
for x in (L1): 
    sum+=x*x 
print(sum)  
 

 
# 5、交换列表中的任意两个元素 
L2 = [14,25,98,75,23,14,56,59]
a = int(input('请输入要替换的位置:')) 
b = int(input('请输入要替换的位置:')) 
L2[a],L2[b] = L2[b],L2[a] 
print(L2) 
