# 1、
# age = int(input("请输入你的年龄"))
# if age >= 18:
#     print("你已经成年啦")
# else:
#     print("你还未成年")



# 2、
# num = int(input("请输入一个数字："))
# if num % 2 ==0:
#     if num % 3 ==0:
#         print("这个数字既能被2也能被3整除")
#     else:
#         print("这个数字能被2整除，不能被3整除")
# else:
#     if num % 3 == 0:
#         print("这个数字能被3整除，不能被2整除")
#     else:
#         print("既不能被2整除，也不能被3整除")



# 3、
# list1 = [1,2,3,4,5]

# for i in list1:
#     print(i)


# str1 = 'abcdefg'
# for j in str1:
#     print(j)


# for i in range(5):
#     print(i)



# for i in range(2,10):
#     print(i)


# for i in range(o,11,3):
#     print(i)


# print(list(range(5))


# 4、
list00 = [1,2,2,4,5,6]
a = list00[0]
for i in list00:
    if i > a:
        a = i
print(a)


print(isinstance(1,str))


list2 = [1,2,3,4,'a',1,'b',7,9]
sum = 0 
for i in list2:
    if isinstance(i,int):
        sum = sum + i
print(sum)


x = 6
for i in range(2,x):
    if  x % i ==0:
        print("不是素数")
        break
else:
    print("是素数")


# 5、
x = 6
sum = 0
for i in range(2,x+1):
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        sum = sum + 1
print(sum)