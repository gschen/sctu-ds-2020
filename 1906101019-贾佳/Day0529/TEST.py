import numpy as np

def LU(A):
    
    n = len(A[0])
    L = np.zeros([n,n])
    U = np.zeros([n,n])
    for i in range(n):
        #下三角对角线全为A
        L[i][i] = 1
        if i == 0:
            #A的第一行和U的第一行相等
            U[0][:] = A[0][:]
            for j in range(1,n):
                
                #计算l的第一列 利用公式
                L[j][0] = A[j][0] /U[0][0]
        else:

            for j in range(i,n):
                temp = 0
                for k in range(0,i):
                    temp = temp + L[i][k]*U[k][j]
                U[i][j] = A[i][j] - temp
            for j in range(i + 1,n):
                temp = 0
                for k in range(0,i):
                    temp = temp +L[j][k] * U[k][i]
                L[j][i] = (A[j][i]-temp)/U[i][i]

    print(U,"\n")
    print(L)
print(LU([[2,2,3],
     [4,7,7],
     [-2,4,5]]))
