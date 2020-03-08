votes=['ABC','ACB','ABC','ACB','ACB']
list1=[]
a=sorted(votes[0])
print(a)
for i in a:
    count=0
    for j in votes:
        for k in range(len(a)):
            if i==j[k]:
                count-=1*(100**(len(a)-k))
    list1.append(count)
list1,a=zip(*sorted(zip(list1,a)))
list2=''
for m in a:
    list2 += m
print(list2)