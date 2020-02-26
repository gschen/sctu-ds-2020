age=int(input(''))

if age>=18:
    print('你已成年')
else:
    print('你还未成年')


n1=25
n2=1
while(n1!=n2):
    n2=int(input('请输入你猜的数：'))
    if n1>n2:
        print('你猜小了')
    elif n1<n2:
        print('你猜大了')
    else:
        print('正确')


        sun=o
a=1
while(a<=100):
    sum+=a
    a+=1
print(sum)

count=0
while count<5:
    print(count,'<5')
    count+=1
else:
    print(count)


    sun=o
a=1
while(a<=100):
    sum+=a
    a+=1
print(sum)



 list1 = [1,2,3,4,5]
 for i in list1:
     print(i)



 str1 = 'abcdefj'
 for i in str1:
     print(i)

 list = [1,2,3,4]
 a=list[0]
 for i in list:
     if i > a:
         a = i
 print(a)



 list2=[1,2,3,4,'a',1]
  sum=0
  for i in list:
      if isinstance(i,int):
          sun+=1
  print(sum)

 x=6
 for i range(2,x):
     if x%i==0:
         print('不是素数')
         break
     else:
         print('是素数')


x=10
sum=0
for i in range(2,x+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum=sum+1
print(sum)

