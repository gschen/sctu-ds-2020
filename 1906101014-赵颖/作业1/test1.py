n=int(input())
def luo(n):
    false_nums=[1,10,20,30,40,50]
    if n == 0:
        return 1
    if n < 0 :
        return"break"
    else:
        return n*luo(n-1)
if n in false_nums:
    print("false")
else: 
    print(luo(n))
