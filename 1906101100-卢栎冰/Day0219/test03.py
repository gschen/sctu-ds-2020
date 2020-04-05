list=[14,25,98,75,23,1,4,56,59]
max=list[0]
min=list[0]
for i in range(1,len(list)):
    if max<list[i]:
        max=list[i]
    if min>list[i]:
        min=list[i]
print(max)
print(min)