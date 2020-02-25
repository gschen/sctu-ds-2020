#A={'a','b','c','c',1}
#B=set('aabbcce')
#print(A,B)
#print(A|B)
#print(A&B)
#print(A^B)

#print(A-B)
#print(B-A)



#集合增删
#A.add('d')
#B.update({1,3},[4,2],'e')
#print(A)
#print(B)

#删除
#A.remove('f')
#A.discard('f')
#A.pop()
#print(A)

#字典
#dict={'name':'张三'，'age':19,'school':'sctu'}
#print(dict)
#修改数据
#dict['name']='李四'
#print(dict)
#查找数据
#dic.get('name')
#dic.setdefault('address','成都')
#dic['class']='2班'
#删除
#del dic['name']
#print(dic)
#dic.pop('name')
#dic.popitem()

#条件判断和循环
# age=int(input('年龄 '))

# if age>=18:
#     print('你成年了')
# else:
#     print('你未成年')

# num1=25
# num2=1
# while(num1 != num2):
#     num2=int(input('数字： '))
#     if num1>num2:
#         print('你的值小了')
#     elif num1<num2:
#         print('你的值大了')
# print('猜对了')


#嵌套
# num=int(input('输入一个数 ：'))
# if num % 2 ==0:
#     if num % 3 ==0:
#         print('能被2和3整除')
#     else:
#         print('能被2不能被3整除')
# else:
#     if num % 3==0:
#         print('能被3不能被2整除')
#     else:
#         print('不能被2也不能被三整除')

#循环 1到100的和
# sum=0
# a=1
# while a <= 100:
#     sum=sum+a
#     a=a+1
# print(sum)

#无限循环
# while(a==1):
#     print('无限')

# count=0

# while count<5:
#     print(count,'<5')
#     count=count+1
# else:
#     print(count,'=5')

#for 循环
# list1=[1,2,3,4,5]
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

#小练习
#寻找最大
# list1 = [1,2,3,2,45,67]

# a = list1[0]

# for i in list1:
#     if i > a:
#         a = i    
# print(a)

#计算和
# print(ininstance(1,int))

# list2 = [1,2,3,4,'a',1]
# sum=0
# for i in list2:
#     if isinstance(i,int):
#         sum=sum+i
# print(sum)


# x = 5
# for i in range(2,x):
#     if x  % i == 0:
#         print('不上素数')
#         break
# else:
#     print('是素数')

# x=10
# sum=0
# for i in range(2,x+1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         sum=sum+1
# print(sum)

#函数
# def ApusB(a,b):
#     c=a+b
#     return a+b
# result=ApusB(1,2)
# print(result)
# print(ApusB(12,13))

# def he(r):
#     area= r**2*3.14
#     pi=3.14
#     return area,pi
# area,pi=he(5)
# print(area,pi)

# def circle(r,pi):
#     area=r**2*pi

#     return area
# print(circle(6,3.14))
# print(circle(r=6,pi=3.14))

# a=2
# def main():
#     b=3
#     print(a)
# main()
# print(b)

# circle=lambda r,pi:r**2*pi
# print(circle(3,3.14))

# def Change(a):
#     a=10

# b=2
# Change(b)
# print(b)


# C=[1,2,3]
# def Change(x):
#     x.append([1,2,3])
# Change(c)
# print(c)


# b='123'
# b=123

def main(x,*y):
    print(x)
    for i in range(len(y)):
        print(y[i])
main(1,11,12,131,41)