# A={'a','b','c',1,2,3,}
# B=set('abcde')
# #集合的差（补）
# print(A-B)
# #集合的并
# print(A|B)
# #集合的交
# print(A&B)
# #不同时包含
# print(A^B)
# #集合增删
# #增加
# A.add('d')
# B.update({1,3},{4,2},'e')
# print(A)
# print(B)
# #删除
# A.remove('a')
# A.discard('a')
# A.pop()




# #字典
# dic={'name':'张三','age':19,'school':'sctu'}
# #修改数据
# dic['name']='李四'
# #查找数据
# dic.get('name')
# dic.setdefault('address','成都')
# print(dic)
# #增加数据
# dic['class']='1班'
# #删除数据
# del dic['name']
# dic.pop('name')
# dic.popitem()
# print(dic)


# age = int(input('请输入你的年龄:'))

# if age >= 18:
#     print('你已经成年了')
# else:
#     print('你还未成年')


# num1 = 25
# num2 = 1
# while(num1 != num2):
#     num2 = int(input('请输入你猜的数字:'))
#     if num1 > num2:
#         print('你输入的值小了')
#     elif num1 < num2:
#         print('你输入的值大了')
# print('猜对了')


# num = int(input('请输入一个数字：'))
# if num % 2 == 0:
#     if num % 3 == 0:
#         print('这个数既能被2也能能被3整除')
#     else:
#         print('这个数能被2整除不能被3整除')
# else:
#     if num % 3 == 0:
#         print('这个数可以被3整除不能被2整除')
#     else:
#         print('这个数既不能被2整除也不能被3整除')

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

# for i in range(0,11,2):
#     print(i)

# print(list(range(5)))


# list1 = [1,2,3,2,6,10,1]
# a=list1[0]
# for i in list1:
#     if i > a:
#         a = i
# print(a)


# circle2=lambda r,pi:r**2*pi
# print(circle2(3,3.14))

# def AplusB(a,b):

#     return a+b
# result=AplusB(1,2)
# print(result)
# print(AplusB(10,12))

# def circle(r,pi):
#     area=r**2*pi

#     return area



# a=2
# def main():
#     b=3
#     print(a)
#     main()
#     print(b)

# c=[1,2,3]
# def change2(x):
#     x.append([1,2,3])
# change2(c)
# print(c)


# b='123'
# b=123

# def main(x,*y):
#    print(x)

# main(1,11,12,13,14)
