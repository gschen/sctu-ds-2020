list = [14,25,98,75,23,1,4,56,59]
max = 0
maxi = " "
for i in range(0,9):
    if list[i] > max:
        maxi = i
        max = list[maxi]
print(max)
