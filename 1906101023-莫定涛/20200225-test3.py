def AplusB(a,b):

    return a+b
result = AplusB(1,2)
print(result)


#计算圆的面积
def sb(r):
    return r**2*3.14
print(sb(6))


def circle(r,pi):
    
print(circle(5,3.14))
print(circle(pi=3,r=6))


def circle(r,pi):
    area = r**2*pi

    return area
area =circle(3,3.14)
print(area)

circle = lamda r,pi:r**2*pi
print(circle(3,3.14))



def change(a):
    a = 10 

b = 2
change(b)
print(b)

c =[1,2,3]
def change2(x):
    x.append([1,2,3])
change2(c)
print(c)

def main(x,*y):
    print(x)
    for i in range(len(y)):
        print(y[i])

main(1,12,13,11)





