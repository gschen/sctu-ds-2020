# 1题
# a=int(input("请输入一个数字："))
# sum=1
# l1=[1,10,20,30,40,50]
# if a not in l1 :
#     for i in range(1,a+1):
#         sum=sum*i
#     print(sum)
# else:
#     print("不能求该数阶乘")



# 2题
# p,t,r=map(int,input("请输入三个数").split(","))
# print(p*t*r//100)


# 3题
# L=[14,25,98,75,23,1,4,56,59]
# print(max(L))


# 4题
#n=int(input("请输入一个数："))
#sum=0
# l2=[14,25,98,75,23,1,4,56,59]
# if n<=len(l2) :
#     for i in l2[0:n] :
#         sum=sum+i**2
#     print(sum)
# else:
#     print("数字太大了")


# 5题
a,b=map(int,input("请输入：").split(","))
l3=[14,25,98,75,23,1,4,56,59]
if a<=len(l3) and b<=len(l3):
    c=l3[a]
    l3[a]=l3[b]
    l3[b]=c
    print(l3)
else:
    print("数字太大了")