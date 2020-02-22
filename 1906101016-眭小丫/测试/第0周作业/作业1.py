list1=[1,10, 20,30,40,50]
def XI(n):
    if n==0:
        return 1
    else:
        return n*XI(n-1)
while True:
    m=int(input())
    if m in list1 or m<0:
        break
    else:
        print(XI(m))

