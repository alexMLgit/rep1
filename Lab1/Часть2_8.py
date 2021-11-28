import numpy as np
import matplotlib.pyplot as plt


def matrix_tranform(matrix, N, d):
    
    matrix=np.transpose(matrix)

    for i in range(0,d):
        mn=np.mean(matrix[i])
        st = np.std(matrix[i])
        for j in range(0,N):
            matrix[i][j]=(matrix[i][j]-mn)/st

    matrix=np.transpose(matrix)
    
    return matrix
    
if __name__ == '__main__':
    N=7
    d=2

    matrix = np.zeros((N,d))

    for i in range(0,N):
        matrix[i]=np.random.multivariate_normal(mean=[1,2],cov=[[2,1],[1,3]])

    print(matrix)    
        
    counter = 1
    for i in range(0,N):
        plt.plot(matrix[i][0], matrix[i][1],'ro')
        plt.annotate(counter,xy=(matrix[i][0]+0.1, matrix[i][1]+0.1))
        counter+=1

    matrix=matrix_tranform(matrix, N, d)

    counter = 1
    for i in range(0,N):
        plt.plot(matrix[i][0], matrix[i][1],'bo')
        plt.annotate(counter,xy=(matrix[i][0]+0.1, matrix[i][1]+0.1))
        counter+=1

    print(matrix)