def jc(x):
    if x < 0:
        return -1
    if x == 0:
        return 1
    return n * jc(x - 1)