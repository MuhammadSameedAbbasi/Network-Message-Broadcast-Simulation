import random
import sys
import numpy as np

# Define the size of the grid and the number of time steps
grid_size = (50, 50)



# Manually declare the initial state for the cellular automaton
initial_state = np.zeros(grid_size)
# Function to update the plot for each time step
def update(step, current_state):
    #global current_state  # Declare current_state as a global variable

    # Create a copy of the current state
    new_state = current_state.copy()

    # Apply the rules of the cellular automaton to update the state
    if step > 0:
        for i in range(1, grid_size[0] - 1):
            for j in range(1, grid_size[1] - 1):
                # Apply the rule: top, bottom, left, and right cells of an active cell become live
                if current_state[i, j] == 1:
                    if(current_state[i-1, j] != 2):
                        new_state[i-1, j] = 1
                    if(current_state[i+1, j] != 2):
                        new_state[i+1, j] = 1
                    if(current_state[i, j-1] != 2):
                        new_state[i, j-1] = 1
                    if(current_state[i, j+1] != 2):
                        new_state[i, j+1] = 1

    # Update the current state
    current_state = new_state
    
    # Check if all cells are filled
    if np.all(current_state >= 1):
        #print(step)
        return step
         # Stop the animation
    
    return update(step+1,current_state)

min_steps = 150
step=0
init_coordinates=[27, 9, 10, 29, 40, 47] #[33, 23, 13, 18, 43, 45] #[33,23,13,24,43,45]
while (True):
    # Manually declare the initial state for the cellular automaton
    initial_state = np.zeros(grid_size)

    
    #set edges to unresponsive cells
    initial_state[0, :] = 2
    initial_state[grid_size[0]-1, :] = 2
    initial_state[:, 0] = 2
    initial_state[:, grid_size[1]-1] = 2


    #set a block of unresponsive cells
    initial_state[10, 0:10] = 2
    initial_state[0:10, 40] = 2
    initial_state[30:47, 13] = 2
    initial_state[44, 10:45] = 2
    initial_state[35:45, 35:40] = 2
    initial_state[26:45, 25] = 2
    initial_state[26, 25:50] = 2

    #make a swirl of unresponsive cells
    initial_state[10, 20:30] = 2
    initial_state[10:20, 30] = 2
    initial_state[20, 20:31] = 2
    initial_state[12:20, 20] = 2
    initial_state[12, 20:28] = 2
    initial_state[12:18, 28] = 2
    initial_state[18, 24:29] = 2


    #coordinates[random.randint(0,5)]+=random.randint(-3,3)
    coordinates=init_coordinates.copy()
    # change one coordinate randomly
    xindex=0
    xgrid_diff=0
    yindex=0
    ygrid_diff=0

    yindex = random.choice([0,2,4])
    ygrid_diff= random.randint(-3,3)

    xindex = random.choice([1,3,5])
    xgrid_diff= random.randint(-3,3)

    new_x_coordiante=coordinates[xindex]+xgrid_diff
    new_y_coordiante=coordinates[yindex]+ygrid_diff

    count=0
    while( new_x_coordiante<=0 or new_x_coordiante>=50 or new_y_coordiante<=0 or new_y_coordiante>=50 or initial_state[ new_y_coordiante , new_x_coordiante ]==2):

        xindex= random.randint(0,5)
        xgrid_diff= random.randint(-3,3)

        yindex = random.randint(0,5)
        ygrid_diff= random.randint(-3,3)
        
        new_x_coordiante=coordinates[xindex]+xgrid_diff
        new_y_coordiante=coordinates[yindex]+ygrid_diff

        count+=1
        if count>3:
            new_x_coordiante=random.randint(2,45)
            new_y_coordiante=random.randint(2,45)
            count=0

    
    coordinates[xindex]+=xgrid_diff

    # Set a block of live cells
    initial_state[coordinates[0], coordinates[1]] = 1
    initial_state[coordinates[2], coordinates[3]] = 1
    initial_state[coordinates[4], coordinates[5]] = 1

    # Initialize the current state
    current_state = initial_state.copy()

    totalsteps=0
    # start the grid simulation
    totalsteps = update(step,current_state)
    
    

    if totalsteps<=min_steps:
        min_steps=totalsteps
        init_coordinates=coordinates
        print(totalsteps , init_coordinates)


