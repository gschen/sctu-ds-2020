#集合

#集合的构建
#A={'a','b','c','d',1}
#B=set('aabbccdd')
#集合之间的运算
#集合的差
#print(A-B)
#集合并操作
#print(A|B)
#集合的交
#print(A&B)
#不同时包含
#print(A^B)

#集合的增删
#添加元素的两种方法
#A.add('f')
#B.update({1,2},[3,4],'e','f')
#print(A)
#print(B)


#删除元素的三种方法
#A.remove('a')
#A.remove('m')#删除集合中不存在的元素会报错
#A.discard('m')#删除集合中不存在的元素不会报错
#A.pop()#随机删除一个元素
#print(A)


#字典

#dic={'name':'李四','age':18,'school':'sctu'}
#print(dic)

#修改数据
#dic['name']='张三'
#print(dic)

#查找数据
#dic.get('name')#不能查找字典里没有的元素
#dic.setdefault('name')
#dic.setdefault('address','成都')
#print(dic)

#增加数据
#dic['class']='1班'
#print(dic)

#删除数据
#del dic['name']
#print(dic)
#dic.pop('name')
#dic.popitem()
#print(dic)


#age=int(input("请输入你的年龄"))
#if age > 18:
#    print("你已经成年了")
#else:
#    print("你还未成年")



#num = 25
#num2 = 1
#while (num !=num2):
#    num2 = int(input('请输入你猜的数据'))
#    if num > num2:
#        print('你输入的值太小了')
#    elif num < num2:
#        print('你输入的值太大了')
#    else:
#        print('猜对了')



#num = int(input("请输入一个数字"))
#if num % 2 ==0:
#    if num % 3 == 0:
#        print("这个数字既能被2整除，也能被3整除")
#    else:
#        print("这个数字可以被2整除，不能被3整除")
#else:
#    if num % 3== 0:
#        print("这个数字可以被3整除，不能被2整除")
#    else:
#        print("这个数既不能被2整除也不能被3整除")


# sum = 0
# a = 1
# while (a <= 100):
#     sum = sum + a
#     a = a+1
# print(sum)


# count = 0
# while count < 5:
#     print(str(count),"< 5")
#     count=count+1
# else:
#     print(str(count)+"=5")


# list1 = [1,2,3,4,5]
# for i in list1:
#     print(i)


# str1 = 'abcde'
# for j in str1:
#     print(j)


# for i in range(5):
#     print(i)


# for i in range (2,10):
#     print(i)


# for i in range(0,11,2):
#     print(i)


#print(list(range(5)))


#练习题

#给定一个列表，找列表中最大的元素

# list = [1,2,3,4]
# a = list[0]
# for i in list:
#     if i > a:
#         a=i
# print(a)


#计算列表中数字之和

# list = [1,2,3,4,'a',5]
# sum = 0
# for i in list:
#     if isinstance(i,int):
#         sum = sum+i
# print(sum)


#输入n，检查2到n之间有多少素数

# x = int(input())
# for i in range(2,x):
#     if x % i ==0:
#         print("不是素数")
#         break
# else:
#     print("是素数")

# x = 5
# sum = 0 
# for i in range(2,x+1):
#     for j in range(2,i):
#         if i %j == 0:
#             break
#     else:
#         sum = sum+1
# print(sum)