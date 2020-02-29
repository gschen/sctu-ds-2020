a=int(input())
if a==0:
    print(1)
elif a in [1,10,20,30,40,50]:
    print('wrong')
else:
    for i in range(1,a):
        a*=i
    print(a)