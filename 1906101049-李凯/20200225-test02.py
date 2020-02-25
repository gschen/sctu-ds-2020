#集合
#构b建集合两种方法

A={"a","b","c","d"}
B=set("aabbcceedd")
#集合之间的运算
#集合的差（补）
#print（A-B)
#集合的并
#print(A|B)
#集合的交
#print(A&B)
#不同时包含
print(A^B)
#集合的增删
#添加元素的两种方法
#A.add("hh")  B.update({1,2},[3,4]"e","f")
#删除元素的方法
#A.remove('a')
#A.remove('m')#删除集合中不存在的元素会报错
#A.discard('m')#删除集合中不存在的元素不会报错
#A.pop()#随机删除一个元素
#print(A)

#字典
dic={"name":"kl","age":"22","home":"chengdu"}
#修改数据
#dic["name"]="张三"
#删除数据
#del dic['name']
#print(dic)
#dic.pop('name')
#dic.popitem()
#print(dic)
#查找数据
#dic.get('name')#不能查找字典里没有的元素
#dic.setdefault('name')
#dic.setdefault('address',default='成都')
#print(dic)
#增加数据
#dic['class']='1班'
#print(dic)


#条件判断

# age = int(input("请输入你的年龄”))
#ifage>=18:
#
print("你已经成年啦" )
# else:
4
print("你还未成年")
###
numl = 25
num2 = 1
while(num1 !- num2):
num2 = int(input(" 请输入你猜的数字: "))
if numl》num2 :
print(“你输入的值小了"啊
elif num1 < num2 :
print(“你输大的值大了")
print(“猜对了")
    
#if嵌套
num = int(input(请输入个数子: )
ifnum%2==6:
ifnum%3==0:
print("这个数子既能被2也能被3整除”)
else :
print("这个数字能被2整除，不能放3整除”)
e lse:
ifnum%3==Q:
print(“这个数字可以被3整除，不能被2整除》
else:
print("既不能被3整除，也不能被?整除”)

###
sum=。
a =1
while(a <= 100):
sum= sum + a
a =a+1
print(sum)

###
while count < 5:
    print(str(count),"<5")
count = count + 1
el se:
print(str( count)+"=5"]

###
# list1 = [1,2,3,4,5] 
# for i in list1:
print(i)
# str1 =
abcdefg
# for j in str1:
print(j)
for i in range(5):
print(i)
for i in range(2;10):
print(i)
i
###
for i in range(0,11,3):
print(i) 
print(list(range(5)))

###
list1 = [1,2;3,2,6,10,1]
a = list1[0]
for i in list1:
ifi>a:
a
i
print(a)

###
list2 = [1,2,3,4,'a',1,'b',21]
sum=0
for i in list2:
if isinstance(i,int):
sum=sum+i
print ( sum)

###
x=6
for i in range(2,x): 
ifxxi=a
0:
print("不是素數")
break
else:
print("是素数")

###
x=5
sum=6
for i in range(2,x+1):
for j in range(2,i):
if i%j==0:
break
else:
sum=sum+1
print(sum)


#函数
