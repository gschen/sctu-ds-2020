#给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。
#幸运数是指矩阵中满足同时下列两个条件的元素：
# #在同一行的所有元素中最小，在同一列的所有元素中最大
#示例 1：
#输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
#输出：[15]
#解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。

#解法一：
matrix = [[3,7,8],[9,11,13],[15,16,17]]
mins = {min(rows) for rows in matrix}
maxes = {max(columns) for columns in zip(*matrix)}
print(list(mins & maxes))

#zip函数的用法：
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b) 
print(zipped)    
print(zip(a,c))       #元素个数与最短的列表一致       
print(zip(*zipped))          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
l = ['a', 'b', 'c', 'd', 'e','f']
print(l)
print(list(zip(l[:-1],l[1:])))


#解法二：
matrix = [[3,7,8],[9,11,13],[15,16,17]]
row_min = list(map(lambda x: min(x), matrix))
col_max = list(map(lambda x: max(x), zip(*matrix)))
print(list(set(row_min).intersection(set(col_max))))
#set.intersection即返回交集


#解法三：
matrix = [[3,7,8],[9,11,13],[15,16,17]]
ans=[]
for i in range(len(matrix)):
    minIn=min(matrix[i])
    index=matrix[i].index(minIn)
    line=[]
    for j in range(len(matrix)):
        line.append(matrix[j][index])
    if min(matrix[i])==max(line):
        ans.append(matrix[i][index])
print(ans)


