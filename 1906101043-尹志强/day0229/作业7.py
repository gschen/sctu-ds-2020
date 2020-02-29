def count1(x):
    int_count,space_count,other_count,str_count=0,0,0,0
    for i in x:
        if i.isdigit():
            int_count += 1
        if i.isalnum():
            str_count=str_count+1
        elif i.isspace():
            space_count += 1
        else:
            other_count += 1
    return int_count,str_count,space_count,other_count
a='D,a, ,s,1,3,2, ,a,2,d,a'
count2=count1(a)
print('数字，字母，空格，其他字符分别是',count2)
