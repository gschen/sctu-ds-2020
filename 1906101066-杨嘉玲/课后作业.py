#1.求给定数的阶乘
def factorial(n):
    if n < 0:
        return -1
    if n == 0:
        return 1
    return n * factorial(n - 1)
print('7的阶乘：' + str(factorial(7)))

#2.单利公式
P,R,T = eval(input('请输入并用逗号隔开：\n P,R,T = '))
P = int(P)
R = int(R)
T = int(T)
sim = (P + R + T)/100
print(sim)

#3.查找数组中的最大元素
list = [14,25,98,75,23,1,4,56,59]
print(max(list))

#4.求数组中的平方和
n = input("请输入：")
n = int(n)
list1 = [14,25,98,75,23,1,4,56,59]
list2 = []
if n <= len(list1):
    for x in list1[0:n]:
        list2.append(x*x)
    print(sum(list2))
else:
    print("请输入小于%d的数"%(len(list1)+1))

#5.交换列表中的两个元素
a1, a2 = eval(input("请输入被置换的两个元素的位置(用逗号隔开)："))
def swap_position(lis,pos1,pos2):
    lis[pos1], lis[pos2] = lis[pos2], lis[pos1]
    return lis
lis = [14,25,98,75,23,1,4,56,59]
pos1, pos2 = a1, a2
print(swap_position(lis,pos1-1,pos2-1))


    
    

   
    
