rating = [2,5,3,4,1]
long=len(rating)
nums=max(rating)
n=0
for m in range(2):
    if m==1:
        rating.reverse()
    for i in range(long-2):
        if rating[i]>nums-2:
            continue
        for j in range(i+1,long):
            for k in range(j+1,long):
                if rating[i]<rating[j]<rating[k]:
                    n+=1
print(n)