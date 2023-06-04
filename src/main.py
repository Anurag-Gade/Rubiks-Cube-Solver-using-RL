#Runner Function

from utils import *
from display import *
from board import *
from rotations import *
from algorithm import *

load_libraries()

'''
Below we will be declaring some parameters required for the operation of the game.
'''

#Whether the game is finished or not
finished = False

#History of moves
history = []

#List of possible moves
moves = ['F','B','U','D','L','R','Fc','Bc','Uc','Dc','Lc','Rc']

#Set the cube
complete_cube = perfect_cube()

#Move counter
move_number = 0

#Moves per iter
moves_iter = 3

'''
Path Generator Function
'''

def path_gen(moves, moves_iter):

    paths = itertools.permutations(moves, moves_iter)
    paths_list = list(paths)

    return paths_list

paths = path_gen(moves, moves_iter) 

'''
Set Cube
'''
cube, random_moves = shuffler(perfect_cube(), leng=7)

print("Number of random moves: {num}".format(num=len(random_moves)))
print("Random Moves: {moves_list}".format(moves_list = random_moves))

tick = time.perf_counter()

while((not finished) and (move_number<50)):

    G = 100

    dist_before = dist_series(cube)

    for i in range(len(paths)):
        cube_c = cube.copy()
        g = path_scan(cube_c, paths[i], dist_before=dist_before)
        if(g<G):
            G = g 
            j = i
        

    path = paths[j]
    for i in range(moves_iter):
        history.append(path[i])

    move_number = move_number + moves_iter

    if(cube==complete_cube).all():
        finished = True

        print("Rubik's Cube Solved!")


tock = time.perf_counter()

all_moves = random_moves + history



fig, ax = plt.subplots(2,1)
fig.set_figheight(12)
fig.set_figwidth(10)
ax[0].title.set_text('Shuffled Cube')
ax[1].title.set_text('After solving with RL')
display_cube(cube_cube(random_moves), axes=ax[0])


display_cube(cube_cube(all_moves), axes=ax[1])
print('# of Moves: ',move_number)
print('Moves: ',history)
print('Program Duration: ',round(tock-tick,1),' sec or ', round((tock-tick)/60,1),' min')




