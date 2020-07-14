
import numpy as np
import random as rd

tour = np.array([[5,5,4,1,1,5,0],[4,5,1,5,3,0,5],[4,0,5,0,2,2,4],[3,1,4,4,1,3,5],[2,0,4,1,3,2,3],[1,4,1,5,0,2,2],[5,2,4,5,3,0,4],[4,1,1,4,2,5,2],[5,2,5,0,4,3,5],[2,1,4,1,4,2,0]])
self = np.array([0,0,0,0,0,0,0])
number_3_tour = np.array([4,0,5,0,2,2,4])
target = ["tour1","tour2","tour4","tour5","tour6","tour7","tour8","tour9","tour10"]
self_juli=[]
number_3 = []

for i in range(tour.size//7):#测量自身距离
    
    self_distance = np.sqrt(sum(np.power((tour[i]-self),2))) 
    
    self_juli.append(float(round(self_distance,9)))   #取小数点后九位
# print(self_juli)


for i in range(tour.size//7):#测量欧式距离
    distance_3 = np.sqrt(sum(np.power((tour[i]-number_3_tour),2))) 
    
    number_3.append(float(round(distance_3,9)))
del number_3[2] 
# print(number_3)
tourist = self_juli[2]
del self_juli[2]
triangle_list = []
for i in range(len(number_3)):#测量三角相似度
    
    triangle = (1 - (number_3[i]/(self_juli[i]+tourist)))
    # print(self_juli[i],number_3[i])
    triangle_list.append(float(round(triangle,8)))



knn = dict(zip(triangle_list,target))
triangle_list.sort(reverse=True)

k = 5#k值取5
triangle_list = triangle_list[0:k]
neighbor = []
for i in range(len(triangle_list)):#knn近邻算法
    b = knn[triangle_list[i]]
    neighbor.append(b)


#加权平均法
A = np.delete(tour,2,0)#删除游客三

l = dict(zip(target,A))
jiaquan = []
for i in range(len(neighbor)):
    x = l[neighbor[i]][1] #取出峨眉山列的评分
    y = triangle_list[i]
    jiaquan.append(x*y)
del triangle_list[2]
# print(triangle_list)
y = sum(jiaquan)/sum(triangle_list)

print("加权平均数：",int(round(y,1)+0.5))

#平均法
sum1 = []
for i in range(len(neighbor)):
    x = l[neighbor[i]][1] #取出峨眉山列的评分
    sum1.append(x)
del sum1[1]
y = len(sum1)
pingjun = sum(sum1)/y
print("平均:",int(pingjun+0.5))

#投票法
vote = rd.randint(0,y-1)
vote_an = sum1[vote]
print("投票法:",vote_an)









