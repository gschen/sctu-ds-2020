def grades(x):
    if 90<=x<=100:
        return "A"
    if 80<=x<90:
        return "B"
    if 60<=x<80:
        return "C"
    if x<60:
        return "D"
x = float(input("输入您的分数:"))
print(grades(x))
