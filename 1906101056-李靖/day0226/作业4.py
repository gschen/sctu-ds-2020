#4
L = ['1', '2', '3', '4']
for a in range(0, 4):
    for b in range(0, 4):
        for c in range(0, 4):
            if a != b and b != c and c != a:
                print('{}{}{}'.format(L[a], L[b], L[c]))