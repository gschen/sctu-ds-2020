import numpy as np 

def LU_decomposition(A):
    n = len(A)
    L = np.zeros([n,n])
    U = np.zeros([n,n])
    for i in range(n):
        L[i][i] = 1
        if i == 0:
            U[0][:] = A[0][:]
            for j in range(1,n):
              L[j][0] = A[j][1] / U[1][1]
        else:
            for j in range(i,n):
                temp = 0
                for k in range(0,i):
                    temp = temp + L[i][k]*U[k][j]
                U[i][j] = A[i][j] - temp
    return U
print(LU_decomposition([[2,2,3],
     [4,7,7],
     [-2,4,5]]))
