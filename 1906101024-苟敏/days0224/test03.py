 def syuan(r):
     return r**2*3.14
 print(syuan(3))

 def syuan(r,pi):
     area=r**2*pi
     return area
 print(syuan(4,3.14))
 print(syuan(pi=3.14,r=4))

#命名空间
 a=2
 def main():
     b=3
     print(a)
 main()
 print(b)

#不可变对象
def dl(a):
    a=10
b=2
dl(b)
print(b)

#可更改对象
 c=[1,2,3]
 def dl(x):
     x.append([1,2,3])
 dl(c)
 print(c)

#关键字参数
 def main(x,*y):
     print(x)
     for i in y:
         print(y)
 main(1,11,12,13,14)