def AplusB(a,b):
    return a+b
    result=AplusB(1,2)
    print(result)
    print(AplusB(10,12))
def circle(r):
    return r**2*3.14
    print(circle(5))

def change(a):
    a=10
b=2
change(b)
print(b)

c=([1,2,3])
def change2(x):
    x.append([1,2,3])
change2(c)
print(c)

def main(x,*y):
    print(x)
    for i in y:
        print(y)
main(1,11,12,13,14)

#
