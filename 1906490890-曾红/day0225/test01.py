# 条件判断
#1

# age = int(input("输入年龄："))
# if age >= 18:
#     print("你已成年")
# else:
#     print("你是未成年")


num=int(input("输入一个数字"))
if num%2==0:
    if num%3 == 0:
        print("这个数既能被2整除也能被3整除")
    else:
        print("这个数能被2整除，不能被3整除")
else:
    if num%3 ==0:
        print("这个数能被3整除，不能被2整除")
    else:
        print("既不能被2整除，也不能被3整除")





#  循环语句
#2

#  l1 = 25
#  l2 = 1
#  while(l1 != l2):
#      l2 = int(input("输入一个数字："))
#      if l1 > l2:
#          print("你输入的值小了")
#      elif l1 < l2:
#          print("你输入的值大了")
#  print("你猜对啦")


#  求1到100的和
#3

#  sum = 0
#  a = 1
#  while (a <= 100):
#      sum = sum + a
#      a = a + 1
#  print(sum)


# 无限循环
#4

# while():
#     print("无限循环中")




#while 循环使用 else 语句
#5

#  x = 0
#  while x < 6:
#      x = x + 1
#      print(str(x),"<6")
#  else:
#      print(str(x)+"=6")  #加号起连接作用，将字符串x和后面的连接起来



#for循环
#for循环可以遍历任何序列的项目，如一个列表或者一个字符串
#6

# list = [1,2,3,4,5]
# for  i in list:
#     print(i)


# str = 'abcdef'
# for i in str:
#     print(i)


# for i in range(5):
#     print(i)

# for i in range(2,10):  #左闭右开
#     print(i)

# for i in range(1,11,2):  #从1开始，每两位取一个数
#     print(i)


# print(list(range(6)))






