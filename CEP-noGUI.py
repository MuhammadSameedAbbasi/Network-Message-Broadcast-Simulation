import sys
import numpy as np

# Define the size of the grid and the number of time steps
grid_size = (50, 50)


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


# Set a block of live cells
initial_state[33, 23] = 1
initial_state[13, 24] = 1
initial_state[13, 45] = 1


# Initialize the current state
current_state = initial_state.copy()

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
        print(step)
        sys.exit()  # Stop the animation
    
    return update(step+1,current_state)

step=0
while (True):
    # Create
    step=update(step,current_state)
