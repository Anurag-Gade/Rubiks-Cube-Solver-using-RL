'''
In this script we are declaring the rotation class, containing 12 rotation functions. We have front, back, up, down, left, and right functions
along with their counterclockwise rotation functions. 
F -> Front (Fc -> Front counterclockwise)
B -> Back (Bc -> Front counterclockwise)
U -> Up (Uc -> Front counterclockwise)
D -> Down (Dc -> Front counterclockwise)
L -> Left (Lc -> Front counterclockwise)
R -> Right (Rc -> Front counterclockwise)
'''

class Rotation:

    def __init__(self, cube_array):
        self.cube_array = cube_array

    def F(self): 
        cube_arr = self.cube_array
        column_right = cube_arr[0,0,:].copy()
        center_bottom = cube_arr[0,1,2].copy()
        column_left = cube_arr[0,2,:].copy()
        center_top = cube_arr[0,1,0].copy()
        cube_arr[0,:,2] = column_right 
        cube_arr[0,2,1] = center_bottom
        cube_arr[0,:,0] = column_left
        cube_arr[0,0,1] = center_top

    def Fc(self): 
        cube_arr = self.cube_array
        row_top = cube_arr[0,:,2].copy()
        center_right = cube_arr[0,2,1].copy()
        row_bottom = cube_arr[0,:,0].copy()
        center_left = cube_arr[0,0,1].copy()
        cube_arr[0,0,:] = row_top
        cube_arr[0,1,2] = center_right
        cube_arr[0,2,:] = row_bottom
        cube_arr[0,1,0] = center_left

    def B(self):
        cube_arr = self.cube_array
        row_top = cube_arr[2,:,2].copy()
        center_right = cube_arr[2,2,1].copy()
        row_bottom = cube_arr[2,:,0].copy()
        center_left = cube_arr[2,0,1].copy()
        cube_arr[2,0,:] = row_top
        cube_arr[2,1,2] = center_right
        cube_arr[2,2,:] = row_bottom
        cube_arr[2,1,0] = center_left 

    def Bc(self):
        cube_arr = self.cube_array
        column_right = cube_arr[2,0,:].copy()
        center_bottom = cube_arr[2,1,2].copy()
        column_left = cube_arr[2,2,:].copy()
        center_top = cube_arr[2,1,0].copy()
        cube_arr[2,:,2] = column_right 
        cube_arr[2,2,1] = center_bottom
        cube_arr[2,:,0] = column_left
        cube_arr[2,0,1] = center_top

    def U(self):
        cube_arr = self.cube_array
        row_front = cube_arr[:,0,2].copy()
        center_left = cube_arr[0,0,1].copy()
        row_back = cube_arr[:,0,0].copy()
        center_right = cube_arr[2,0,1].copy()
        cube_arr[0,0,:] = row_front
        cube_arr[1,0,0] = center_left
        cube_arr[2,0,:] = row_back
        cube_arr[1,0,2] = center_right

    def Uc(self):
        cube_arr = self.cube_array
        row_right = cube_arr[0,0,:].copy()
        center_front = cube_arr[1,0,0].copy()
        row_left = cube_arr[2,0,:].copy()
        center_back = cube_arr[1,0,2].copy()
        cube_arr[:,0,2] = row_right
        cube_arr[0,0,1] = center_front
        cube_arr[:,0,0] = row_left
        cube_arr[2,0,1] = center_back

    def D(self):
        cube_arr = self.cube_array
        row_right = cube_arr[0,2,:].copy()
        center_front = cube_arr[1,2,0].copy()
        row_left = cube_arr[2,2,:].copy()
        center_back = cube_arr[1,2,2].copy()
        cube_arr[:,2,2] = row_right
        cube_arr[0,2,1] = center_front
        cube_arr[:,2,0] = row_left
        cube_arr[2,2,1] = center_back

    def Dc(self):
        cube_arr = self.cube_array
        row_front = cube_arr[:,2,2].copy()
        center_left = cube_arr[0,2,1].copy()
        row_back = cube_arr[:,2,0].copy()
        center_right = cube_arr[2,2,1].copy()
        cube_arr[0,2,:] = row_front
        cube_arr[1,2,0] = center_left
        cube_arr[2,2,:] = row_back
        cube_arr[1,2,2] = center_right   

    def L(self):
        cube_arr = self.cube_array
        column_front = cube_arr[:,0,0].copy()
        center_top = cube_arr[2,1,0].copy()
        column_back = cube_arr[:,2,0].copy()
        center_bottom = cube_arr[0,1,0].copy()
        cube_arr[0,:,0] = np.flip(column_front)
        cube_arr[1,0,0] = center_top
        cube_arr[2,:,0] = np.flip(column_back)
        cube_arr[1,2,0] = center_bottom

    def Lc(self):
        cube_arr = self.cube_array
        column_front = cube_arr[:,2,0].copy()
        center_top = cube_arr[0,1,0].copy()
        column_back = cube_arr[:,0,0].copy()
        center_bottom = cube_arr[2,1,0].copy()
        cube_arr[0,:,0] = column_front
        cube_arr[1,0,0] = center_top
        cube_arr[2,:,0] = column_back
        cube_arr[1,2,0] = center_bottom

    def R(self):
        cube_arr = self.cube_array
        row_front = cube_arr[:,2,2].copy()
        center_top = cube_arr[0,1,2].copy()
        row_back = cube_arr[:,0,2].copy()
        center_bottom = cube_arr[2,1,2].copy()
        cube_arr[0,:,2] = row_front
        cube_arr[1,0,2] = center_top
        cube_arr[2,:,2] = row_back
        cube_arr[1,2,2] = center_bottom

    def Rc(self):
        cube_arr = self.cube_array
        row_top = cube_arr[2,:,2].copy()
        center_front = cube_arr[1,0,2].copy()
        bottom_row = cube_arr[0,:,2].copy()
        center_back = cube_arr[1,2,2].copy()
        cube_arr[:,0,2] = row_top
        cube_arr[0,1,2] = center_front
        cube_arr[:,2,2] = bottom_row
        cube_arr[2,1,2] = center_back

'''
Now we define the mover function, which enables movement in accoradance with the functions defined in the Rotation class
'''
def mover(rot, cube_array):

    rot_obj = Rotation(cube_array)

    if rot == "F":
        rot_obj.F(cube_array)

    elif rot == "Fc":
        rot_obj.Fc(cube_array)

    elif rot == "B":
        rot_obj.B(cube_array)

    elif rot == "Bc":
        rot_obj.Bc(cube_array)

    elif rot == "U":
        rot_obj.U(cube_array)

    elif rot == "Uc":
        rot_obj.Uc(cube_array)

    elif rot == "D":
        rot_obj.D(cube_array)

    elif rot == "Dc":
        rot_obj.Dc(cube_array)

    elif rot == "L":
        rot_obj.L(cube_array)

    elif rot == "Lc":
        rot_obj.Lc(cube_array)

    elif rot == "R":
        rot_obj.R(cube_array)

    elif rot == "Rc":
        rot_obj.Rc(cube_array)

