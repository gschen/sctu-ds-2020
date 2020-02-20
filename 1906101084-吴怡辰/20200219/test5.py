list = [14,25,98,75,23,1,4,56,59]
m,n = map(int,input().split())
if m < len(list) and n < len(list):
    list[m],list[n] = list[n],list[m]
print(list)
