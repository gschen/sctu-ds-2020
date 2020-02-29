def count(x):
    num_number=char_number=space_number=other_number=0
    for char in x:
        if char.isdigit():
            num_number += 1
        elif char.isalpha():
            char_number += 1
        elif char == " ":
            space_number += 1
        else:
            other_number += 1
    print("数字：%d,字母：%d，空格：%d，其他字符：%d"%(num_number,char_number,space_number,other_number))
    return
count("D,a, ,s,1,3,2, ,a,2,d,a, ,")
            

