# list=[1,2,3,2]
# a=list[0]
# for i in list:
#     if i >a:
#         a=i
# print(a)


# print(isinstance(1,int))


# list2=[1,2,3,4,'a,',1]
# sum=0
# for i in list2:
#     if isinstance(i,int):
#         sum =sum+i
# print(sum)



# x=13
# for i in range(2,x):
#     if x%i==0:
#         print('不是素数')
#         break
#     else:
#         print('是素数')



x=5
sum=0
for i in range(2,x+1):
    for j in range(2,i):
        if i%j==0:
            break

    else:
       sum=sum+1
print(sum)


