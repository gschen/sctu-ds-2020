def jiang(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade < 90:
        return 'B'
    elif 60 <= grade < 80:
        return 'C'
    else:
        return 'D'
grade = int(input())
print(jiang(grade))