#第五题
X=input('请输入X的值:')
Y=input('请输入Y的值:')
Z=input('请输入Z的值:')
G=[X,Y,Z]
V=[]
a=max(G)
b=min(G)
for n in G:
    if n==b:
        V.append(n)
    else:
        if n<a:
            q=n
        else:
            s=n
V.append(q)
V.append(s)    
print(V)