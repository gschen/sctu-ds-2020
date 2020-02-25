# list1 = [1,2,3,2,4,9,0,5]
# a = list1[0]

# for i in list1:
#     if i > a:
#         a = i
# print(a)

#print(isinstance(1,str))

# list2 = [1,2,3,4,'a',1,'b',7,9]

# sum = 0 
# for i in list2:
#     if isinstance(i,int):
#         sum = sum + i
# print(sum)

# x = 6
# for i in range(2,x):
#     if  x % i ==0:
#         print("不是素数")
#         break
# else:
#     print("是素数")

x = 6
sum = 0
for i in range(2,x+1):
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        sum = sum + 1
print(sum)
