#1、求给定数的阶乘
#def jiecheng(n):
     #if n == 0 or n ==1:
          #return 1
     #else:
         # return n * jiecheng(n-1)
#print(jiecheng(6))



#2、单利公式
#def danli():
     #p=input("请输入本金P：")
     #t=input("请输入时间T:")
     #r=input("请输入利率r:")
     #c=float((float(p)*float(t)*float(r))/100)
     #print("单利是: %d" %(c))
#danli()



#3、查找数组中的最大元素
#list=[14,25,98,75,23,1,4,56,59]
#list.sort()
#print(list[-1])


#4、求数组前n个数的平方和
#lis1=[14,25,98,75,23,1,4,56,59]
#s=0
#n=int(input("计算前n个数,n为："))
#m=list(lis1[:n])
#if n <9:
     #for x in m:
          #x=x**2
          #s+=x
     #print("平方和为: %d" %(s))

#else:
     #print("抱歉，n为正整数且不能大于数组长度9,请重新输入。")



#交换列表中的任意两个元素：
lis1=[14,25,98,75,23,1,4,56,59]
m=int(input("请输入位置一："))
n=int(input("请输入位置二："))
x=lis1[m]
y=lis1[n]
lis1[n]=x
lis1[m]=y
print(lis1)