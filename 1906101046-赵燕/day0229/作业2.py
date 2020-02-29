x=eval(input("成绩："))
def f(x):
    if 90<=x<=100:
        print("A")
    elif 80<=x<90:
        print("B")
    elif 60<=x<80:
        print("C")
    else:
        print("D")
    return x
print(f(x))