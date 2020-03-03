[1.2.3.4]
for a in range(1,5):
    for b in range(1,5):
        for i in range(1,5):
            if a != b and b!=i and a!= i:
                print('{}{}{}'.format(a,b,i))