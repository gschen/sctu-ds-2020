n = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (i != k ) and (j != k ):
                n += 1
print( f"一共有{n}组")