# coding=utf-8

# while求前100的和
sum=0
a=1
while a<=100:
    sum+=a
    a+=1
print(sum)

# 无限循环
# a=1
# while a==1:
#     print('无限循环中！！！')

# while 和 else 搭配使用
count=0
while count<5:
    print(str(count),'<5')
    count+=1
else:
    print(str(count)+'=5')