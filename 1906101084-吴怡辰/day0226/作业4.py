l =[]
def qiushu():
    for a in range(1,5):
        for b in range(1,5):
            for c in range(1,5):
                if a != b and a != c and b != c:
                    l.append(str(a)+str(b)+str(c))
    print('{}种组合,{}'.format(len(l),l))
qiushu()
