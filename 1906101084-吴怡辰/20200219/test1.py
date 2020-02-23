n = int(input())
list = [1,10,20,30,40,50]
s = 1
if n in list:
    print("False")
else:
    for i in range(1,n+1):
        s = s*i
    print(s)
