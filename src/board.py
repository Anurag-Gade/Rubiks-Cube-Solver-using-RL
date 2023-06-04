#Cube Functions
from utils import *
from rotations import *

load_libraries()

'''
Basically, as the Rubik's Cube is a "cube", we would be using a 3-dimensional array, which will be square matrices stacked on each other.
Taking into account of the "cubic" nature, the number of channels must be equal to say "m", where "m" is the side of the square.
Here we use a conventional 3x3x3 Rubik's Cube. 

We store the entries in the NumPy array of the cube, in the form of a string. In order to unpack the entries into coordinates, 
we write the below function.
Coordinates are in the form (x,y,z)
'''
def unpack(entry):
    return (float(entry[0]),float(entry[1]),float(entry[2]))

'''
Since we have talked about a cube, we will now initialize a cube which would display a perfect cube when plotted. Assuming one is clear
with plane theory, here we denote the entries with three numbers which are intrinsically a string such as '121'. This string represents
the point (1,2,1) in the 3-dimensional space. In other words, the point (1,2,1) represents the intersection of the planes x=1, y=2, and
x=1. There will be 8, 4, and 8 points respectively on the front, middle, and last channel/plane. We mimic this fact. We also take the
front plane to be x=0, middle to be x=1, and last to be x=2. This will be used to check if the cube is solved, by comparing the indexing 
of the array at that particular instant with the entry at that particular index position.

'''

def perfect_cube():
    perfect_list = [['000', '001', '002'],
                    ['010', 'xxx', '012'],
                    ['020', '021', '022'],
                    ['100', 'xxx', '102'],
                    ['xxx', 'xxx', 'xxx'],
                    ['120', 'xxx', '122'],
                    ['200', '201', '202'],
                    ['210', 'xxx', '212'],
                    ['220', '221', '222']]

    perfect_arr = np.array(perfect_list)
    perfect_array = perfect_arr.reshape((3,3,3))
    return perfect_array

'''
The function below serves as a cube shuffler. We randomly select the number of rotations, and we perform the rotation after which it is 
recorded in a list.
'''

def shuffler(cube_array, start=100, stop=200, leng=None):
    moves = ['F','Fc','B','Bc','U','Uc','D','Dc','L','Lc','R','Rc']
    if leng == None:
        turns = np.random.randint(start,stop)
    else:
        turns=leng
    
    shuffle_history = []
    for i in range(turns):
        j = np.random.randint(0,len(moves)-1)
        mover(moves[j], cube_array)
        shuffle_history.append(moves[j])

    return cube_array, shuffle_history

