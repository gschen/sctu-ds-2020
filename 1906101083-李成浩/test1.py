l=[1,10,20,30,40,50]
x=int(input())
if x not in l:
    def jc(i):
        if i==1:
            return 1
        return i*jc(i-1)
    print(jc(x))