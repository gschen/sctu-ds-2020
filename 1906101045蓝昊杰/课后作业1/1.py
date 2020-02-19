n=int(input())
s=1
if n!=1 and n!=10 and n!=20 and n!=30 and n!=40 and n!=50:
    while n>1:
        s=s*n
        n-=1
if s!=1:     
    print(s)
