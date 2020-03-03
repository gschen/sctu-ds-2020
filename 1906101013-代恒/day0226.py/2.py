def dai(grade):
    if 90<= grade <=100:
        print("A")
    if 80<= grade <90:
        print("B")
    if 60<= grade <80:
        print("C")
    if grade<60:
        print("D")
grade = int(input())
print(dai(grade)) 