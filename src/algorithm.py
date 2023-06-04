from utils import *
from board import *
from rotations import *

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import itertools
# import time

load_libraries()

dims = 3
'''
Initializing a gradient function, which computes the change in distance.
'''
def gradient(dist_before, dist_after):
    return np.average(dist_after - dist_before)

'''
For clarity, we can visualize this as a function which averages the distance. This is a vital cog for selecting the path, as the one with
the greatest returned gradient function value is chosen.
'''

'''
The below function is to compute the euclidean distance between two points in a 3D space.
'''
def euclidean_distance(p1,p2):
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)**(0.5)

'''
In the below function we aim to return a Series data structure of the distance between the current and final position of a piece.    
'''
def dist_series(cube_array):
    pos = ['000','001','002','010','012','020','021','022','100','102','120','122','200',
           '201','202','210','212','220', '221','222']
    dist_ser = pd.Series(data = np.zeros(len(pos)), index=pos)
    for i in range(dims):
        for j in range(dims):
            for k in range(dims):
                goal_state = cube_array[i,j,k].copy()
                if goal_state!="xxx":
                    goal_coordinates = unpack(goal_state)
                    dist = euclidean_distance([i,j,k], goal_coordinates)
                    dist_ser[goal_state] = dist
    
    return dist_ser

'''
The next function will be checking the possible moves and will assign a score to the possible move. Below, we first create a copy of the 
cube_array. The ".all()" function returns true if all elements of  that particular data structure is true. So we obtain the prior distance.
We then move our cube according the the given path and check how close are the moved pieces of the cube with the original cube.
'''
def path_scan(cube_arr, path, dist_before=None):

    if dist_before.all():
        dist_before = dist_series(cube_arr) 
    
    cube_arr_2 = cube_arr.copy()

    for i in path:
        mover(i, cube_arr)
    
    dist_after = dist_series(cube_arr)

    if (cube_arr_2 == cube_arr).all():
        return 50
    
    else:
        return gradient(dist_before, dist_after) 


    
