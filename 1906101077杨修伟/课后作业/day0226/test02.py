def yxw(n):
    if n>90 and n<100:
        return "A"
    if n>80:
        return "B"
    if n>60:
        return "C"
    if n<60:
        return "D"
n=int(input())
print(yxw(n))