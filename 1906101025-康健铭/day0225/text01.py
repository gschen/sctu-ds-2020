#第一题：
#  def yht(x):
#     s=3*x**4-9*x**2+X/2
#     return s
# l=[54,96,83,64,234,158,364]
# for x in l[0:-1] :
#     print(s)


# 第二题：
# def lovr(g):
#     if g>=90 and g<=100 :
#         return "A"
#     if g >=80 and g<=90 :
#         return "B"
#     if g>=60 and g<=80 :
#         return "C"
#     else:
#         return "D"
# print(lovr(85))

# 第三题：
# def yhtre(n):
#     l=[]
#     for i in range(len(n)):
#         if i % 2==1:
#             l.append(n[i])
#     return l
# ret=yhtre([1,2,3,4,5])
# print(ret)


# 第四题：
# l=["1","2","3","4"]
# count=0
# for i in l :
#     for j in l :
#         for k in l :
#             if len(set(i+j+k))==3 :
#                 print("%s%s%s" % (i,j,k))
#                 count+=1

# print("最终结果为：%s个" % count)



# 第五题：
# x=input("请输入第一个数字:")
# y=input("请输入第二个数字:")
# z=input("请输入第三个数字:")
# L=[x,y,z]
# for i in range(0,3):
# 	for j in range(i,3):
# 	    if int(L[i])>int(L[j]):
# 	        k=L[i]
# 	        L[i]=L[j]
# 	        L[j]=k
# print(arr)




# 第六题：
# def yht(num):
#     s = 0
#     for i in range(2, num+1, 2):
#         s += 1 / i
#     return s

# def kjm(num):
#     s = 0
#     for i in range(1, num+1, 2):
#         s += 1 / i
#     return s

# def love(fx, n):
#     s = fx(n)
#     return s

# if __name__ == "__main__":
#     num = int(input("请输入一个整数："))
#     if num % 2 == 0:
#         print("偶数")
#         sum = love(yht,num)
#     else:
#         print("奇数")
#         sum = love(kjm, num)
#     print(sum)
