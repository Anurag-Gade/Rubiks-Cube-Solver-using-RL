from utils import *
# import numpy as np
# import seaborn as sns

load_libraries()

def display_cube(cube_arr, cmap=None, axes=None):

    if cmap==None:

        cmap=["black","blue","white","green","yellow","red","orange"]

    sns.heatmap(cube_arr, linewidth=1, linecolor="black", cmap=cmap, ax=axes)

def solved_view():

    arr = np.zeros(108)
    final_arr = arr.reshape((9,12))

    '''Blue'''
    final_arr[3:6,:3]= 100 
    '''White'''
    final_arr[3:6,3:6]=200 
    '''Green'''
    final_arr[3:6,6:9]=300 
    '''Yellow'''
    final_arr[3:6,9:]=400 
    '''Red'''
    final_arr[:3,3:6]=500 
    '''Orange'''
    final_arr[6:,3:6]=600 
    return final_arr


def rotate(cube_arr, clockwise=True):
    if clockwise:
        A = zip(*cube_arr[::-1])
        A = list(A)
    else:
        for i in range(3):
            A = zip(*cube_arr[::-1])
            A = list(A)
    arr_A = np.array(A)

    return arr_A.reshape((3,3))

'''
Below we will be declaring the functions for displaying the rotations.
'''
#Clockwise Rotations

def display_front(cube_arr):

    shift = cube_arr[3,3:].copy()
    move = cube_arr[3,:3].copy()
    cube_arr[3,9:] = move
    cube_arr[3,:9] = shift
    face = cube_arr[:3,3:6].copy()
    face = rotate(face)
    cube_arr[:3,3:6] = face 

def display_back(cube_arr):

    shift = cube_arr[5,:9].copy()
    move = cube_arr[5,9:].copy()
    cube_arr[5,3:] = shift
    cube_arr[5,:3] = move
    face = cube_arr[6:,3:6].copy()
    cube_arr[6:,3:6] = rotate(face)     

def display_left(cube_arr):

    row_yellow = cube_arr[3:6,11].copy()
    row_red = cube_arr[:3,3].copy()
    row_white = cube_arr[3:6,3].copy()
    row_orange = cube_arr[6:,3].copy()
    cube_arr[:3,3] = np.flip(row_yellow)
    cube_arr[3:6,3] = row_red
    cube_arr[6:,3] = row_white
    cube_arr[3:6,11] = np.flip(row_orange)
    face = cube_arr[3:6,:3].copy()
    cube_arr[3:6,:3] = rotate(face)     

def display_right(cube_arr):

    shift = cube_arr[3:,5].copy()
    movetop = cube_arr[:3,5].copy()
    moveback = cube_arr[3:6,9].copy()
    cube_arr[:6,5] = shift
    cube_arr[6:,5] = np.flip(moveback)
    cube_arr[3:6,9] = np.flip(movetop)
    face = cube_arr[3:6,6:9].copy()
    cube_arr[3:6,6:9] = rotate(face)

def display_up(cube_arr):
    
    row_red = cube_arr[3:6,8].copy()
    row_blue = cube_arr[0,3:6].copy()
    row_orange = cube_arr[3:6,0].copy()
    row_green = cube_arr[8,3:6].copy()
    cube_arr[0,3:6] = row_red
    cube_arr[3:6,0] = np.flip(row_blue)
    cube_arr[8,3:6] = np.flip(row_orange)
    cube_arr[3:6,8] = row_green
    face = cube_arr[3:6,9:].copy()
    cube_arr[3:6,9:] = rotate(face)    

def display_down(cube_arr):

    row_red = cube_arr[2,3:6].copy()
    row_green = cube_arr[3:6,6].copy()
    row_orange = cube_arr[6,3:6].copy()
    row_blue = cube_arr[3:6,2].copy()
    cube_arr[3:6,6] = np.flip(row_red)
    cube_arr[6,3:6] = np.flip(row_green)
    cube_arr[3:6,2] = row_orange
    cube_arr[2,3:6] = row_blue
    face = cube_arr[3:6,3:6].copy()
    cube_arr[3:6,3:6] = rotate(face) 

#Anticlockwise Rotations

def display_front_anti(cube_arr):

    display_front(cube_arr)
    display_front(cube_arr)
    display_front(cube_arr)

def display_back_anti(cube_arr):

    display_back(cube_arr)
    display_back(cube_arr)
    display_back(cube_arr)

def display_left_anti(cube_arr):

    display_left(cube_arr)
    display_left(cube_arr)
    display_left(cube_arr)

def display_right_anti(cube_arr):

    display_right(cube_arr)
    display_right(cube_arr)
    display_right(cube_arr)

def display_up_anti(cube_arr):

    display_up(cube_arr)
    display_up(cube_arr)
    display_up(cube_arr) 

def display_down_anti(cube_arr):

    display_down(cube_arr)
    display_down(cube_arr)
    display_down(cube_arr) 



def moves_display(cube_array, move):

    if move == 'F':
        display_front(cube_array)

    elif move == 'B':
        display_back(cube_array)
    
    elif move ==  'L':
        display_left(cube_array)

    elif move ==  'R':
        display_right(cube_array)

    elif move ==  'U':
        display_up(cube_array)
    
    elif move == 'D':
        display_down(cube_array)

    elif move == 'Fa':
        display_front_anti(cube_array)

    elif move == 'Ba':
        display_back_anti(cube_array)

    elif move == 'La':
        display_left_anti(cube_array)

    elif move == 'Ra':
        display_right_anti(cube_array)

    elif move == 'Ua':
        display_up_anti(cube_array)
   
    elif move == 'Da':
        display_down_anti(cube_array)

def cube_cube(moves):

    cube = solved_view()

    for i in moves:

        moves_display(cube,i)

    return cube