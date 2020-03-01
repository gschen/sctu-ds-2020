"""
4.	（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
num_list = [1,2,3,4]
m = 0
for a in num_list:
    for b in num_list:
        for c in num_list:
            if a != b and a != c and b != c:
                num = "".join([str(a),str(b),str(c)])

                print(num)
                m+=1
print("共有%d个"%m)

