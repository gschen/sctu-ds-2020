x=int(input())
y=1
n=[1,10,20,30,40,50]
if x==0:
    print(0)
if x<0:
    print("wrong")
if x>0:
    if x in n:
        print ("wrong")
    else:
        for i in range(1,x+1):
            y*=i
        print(y)                