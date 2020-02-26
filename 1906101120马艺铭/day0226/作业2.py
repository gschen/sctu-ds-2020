#第一题
def fa(x):
    return (3*x*x*x*x-9*x*x+x)/2
print (fa(56))
#依次输入54，96，83，64，234，158，364
#第二种方案
fa03=lambda x:(3*x*x*x*x-9*x*x+x)/2
print(fa03(56))


#第二题
# grade  = int(input('请输入你的成绩'))
# if grade>= 90:
#     print("A")
# else:
#     grade>=80，grade>90
#     print("B")
# elif:
#     grade>=60，grade>80
#      print("C")
# print("D")
#第二种方案
def grade(score):
    ret = []
    score = int(input('请输入你的成绩'))
if 0 <= score < 60:
    print("D")
elif score < 80:
    print("输入成绩属于C级别。")
    print("祝贺你通过考试！")
elif score < 90:
    print("输入成绩属于B级别。")
    print("祝贺你通过考试！")
else:
    print("输入成绩属于A级别。")
    print("祝贺你通过考试！")
    return ret
print(grade(score(85)))


#第三题
def func(l):
    return l[1::2]
print(func([1,2,3,4,5,6,7]))

#第四题
numberList=[1,2,3,4]
complexList=[]
def permutationNum():
    for i in numberList:
        for j in numberList:
                for k in numberList:
                    if i!=j and k != j and i!=k:
                        complexList.append(str(i)+str(j)+str(k))
    print("共有{}种组合，分别为{}".format(len(complexList),complexList))
permutationNum()


#第五题
x = input('请输入x：')
y = input('请输入y：')
z = input('请输入z：')
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(x, y, z)

