a=int(input())
b=1
list=[1,10,20,30,40,50]
if a in list:
    print('False')
else:
    for i in range(1,a+1):
        b=b*i
    print(b)

 