l = ['1','2','3','4']
res = []
for a in l:
    for b in l:
        for c in l:
            if a != b and b != c and a != c:
                res.append(int(a+b+c))
print(len(res),'\n',res)