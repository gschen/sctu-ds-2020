n=['5','2','C','D','+']
ans=[]
for i in n:
    if ord(i)!=67 and ord(i)!=68 and ord(i)!=43:
        ans.append(int(i))
        
    elif i=='C':
        ans.pop()
    elif i=='D':
        ans.append(eval(n[0])*2)
        
    elif i=='+':
        ans.append(eval(n[0])*3)
        print(ans)
print(sum(ans))