x=int(input("请输入成绩:"))
def dengji(x):
    if 100>=x>=90:
        return "A"
    elif 90>=x>=80:
        return "B"
    elif 80>=x>=60:
        return "C"    
    elif x<60:
        return "D"
print(dengji(x))
