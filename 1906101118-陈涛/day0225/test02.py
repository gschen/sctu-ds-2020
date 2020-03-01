# #gather
# A={'a','b','c','c'}
# B=set('aabbcce')
# #删除discard(不会报错),remove(会报错),pop(s随机删除)
# A.remove('a')
# B.update([4,2],{1,3},'f')
# B.pop()
# print(A)
# print(B)
# print(B-A)
# print(A&B)
# print(A|B)
# #dictionary
# dic={'name':'张三','age':'twenty','dender':'male'}
# #修改
# dic['name']='张麻子'
# dic['emotion']='first'
# del dic['emotion']
# dic.pop('name')
# dic.popitem()
# print(dic)

# #
# age=int(input('请输入您的年龄'))
# if age >=18:
#     print('成年')
# else:
#     print('未成年')

# num1=25
# num2=1
# while(num1 !=num2):
#     num2 = int(input('输入你猜的数字'))
#     if num1 >num2:
#         print('猜小了')
#     elif num1<num2:
#         print('猜大了')
# print('猜对了')

# num4 = int(input('输入一个数字'))
# if num4%2==0:
#     if num4%3==0:
#         print('2或3都能整除它')
#     else:
#         print('只能被2整除')
# else:
#     if num4%3==0:
#         print('3能，2不能')
#     else:
#         print("3 or 2 both can't'")

# num5 = 0
# a = 1
# # while(a <= 100):
# #     sum = sum + a
# #     a = a+1
# # print(sum)C

# while a==1:
#     print('!!!!!!!!')

# count = 0
# while count<5:
#     print(str(count),"<5")
#     count = count+1
# else:
#     print(str(count)+"=5")

# list1 = [1,2,3,4,5]
# for i in list1:
#     print(i)

# str1='jsdnfkjs'
# for j in str1:
#     print(j)

# for i in range(20):
#     print(i)

# for i in range(1,20):
#     print(i)

# for i in range(1,20,3):
#     print(i)
# #print(list(range(10)))

# a=0
# for i in [1,2,3,]:
#     if a<i:
#         a=i
# print(a)

# list2 = [1,2,3,4,'a',5]
# sum=0
# for i in list2:
#     if isinstance(i,int):
#         sum = sum + 1
#     elif isinstance(i,str):
#         print(i)
# print(sum)

# x = 6
# for i in range(1,x):
#     if x % i ==0:
#         print('not a prime number')
        
#     else:
#         print("it's a prime number")

# x = 10
# sum = 0
# for i in range(2,x+1):
#     for j in range(2,i):
#         if i % j ==0:
#             break
#     else:
#         sum = sum + 1
# print(sum)


# a = 2
# def main():
#     b = 3
#     print(a)
# main()

# circle2 = lambda r,pi:r**2*pi
# print(circle2(3,3.14))

# def mian(a):
#     b = 3.14*(a**2)
#     return(b)
# print(mian(2))

# def circle(r,pi):
#     area=r*r*pi
#     print(area)
# circle(5,3)

# def change(a):
#     a = 10
# b=2
# change(b)
# print(b)





