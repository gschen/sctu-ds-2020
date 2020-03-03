#2、单利公式为：单利=(P*T*R)/100其中，P是本金T是时间，R是利率   例如输入：P=10000 R=5 T=5 输出:2500  要求P、T、R都是input输入的，不能固定
P=int(input('p='))
T=int(input('T='))
R=int(input('R='))
m=(P*T*R)/100
print(m)