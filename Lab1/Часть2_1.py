import numpy as np

def Calculate_the_function(x,w,b):
    sum = 0
    i = 0
    n = len(x)
    while(i<n):
        sum = sum + x[i]*w[i]
        i+=1
    return sum+b

if __name__ == '__main__':
    list_vec1 = [5,2,3]
    lict_vec2 = [2,1,2]
    x = np.array(list_vec1)
    w = np.array(lict_vec2)
    b = 5
    sum = Calculate_the_function(x,w,b)
    print(sum)

