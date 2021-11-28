import numpy as np
import random

def Calculate_the_angle(v,q):
    v_u = (q / np.linalg.norm(v))
    q_u = (v / np.linalg.norm(q))
    radians = np.arccos(np.clip(np.dot(v_u, q_u), -1.0, 1.0))
    angle = np.degrees([radians.real])[0]
    return angle

if __name__ == '__main__':
    
    list_vec = []
    V = 1000
    d = 6
    for i in range(V):
        temp_list = []
        for j in range(d):
            temp_list.append( random.randint(-10, 10) )
        list_vec.append( np.array(temp_list) )

    temp_list = []
    for j in range(d):
            temp_list.append( random.randint(-10, 10) )
    q =  np.array(temp_list) 

    angle_90 = angle_30 = 0
    for i in range(V):
        angle = Calculate_the_angle(list_vec[i],q)
        if angle < 90:
            angle_90 += 1
        if angle < 30:
            angle_30 += 1
            
    print(angle_90/V)
    print(angle_30/V)