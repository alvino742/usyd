import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_random_grid(row,col):
    matrix = np.random.rand(row, col)
    thresholded = np.where(matrix < 0.5, 0, 1)
    return thresholded

def count_live_neighbours(grid, coordinate):
    x = coordinate[0]
    y = coordinate[1]
    counter = 0

    for i in [-1,0,1]:
        for k in [-1,0,1]:
            if i == 0 and k == 0: 
                continue
            if 0 <= x+i < grid.shape[0] and 0 <= y+k < grid.shape[1]:
                counter += grid[x+i, y+k]
    return counter

def dynamic_function(matrix):
    matrix_next = matrix.copy()
    for i in range(matrix.shape[0]):
        for k in range(matrix.shape[1]):
            current_cell = matrix[i, k]
            current_cell_count = count_live_neighbours(matrix, (i,k))
            if current_cell == 1:
                if current_cell_count < 2:
                    matrix_next[i,k] = 0
                elif current_cell_count > 3:
                    matrix_next[i,k] = 0
            elif current_cell == 0:
                if current_cell_count == 3:
                    matrix_next[i,k] = 1
    return matrix_next 


def simulate(n_steps, row, col, X_0):
    #initiate state vector
    X = np.zeros((n_steps+1, row, col))
    X[0] = X_0

    for k in range(n_steps):
        X[k+1] = dynamic_function(X[k])

    return X

def animate_simulation(X, filename, title):
    fig_, ax_ = plt.subplots()

    im = ax_.imshow(X[0], cmap="gray_r", animated=True)
    title_ = ax_.set_title(title)


    def update(i):
        im.set_data(X[i])
        title_.set_text(f"{title} at time step = {i} \nBlack means alive, white means dead")
        return [im, title_]

    ani = animation.FuncAnimation(fig_, update, frames=len(X), interval=60, blit=True)
    ani.save(filename, writer="pillow", fps = 15)

'''
strategy:

4 by 4 grid means that there are 16 cells 
each cell can either by dead or alive (2 states)
Total number of combinations is 2 * 2 * 2... 16 times = 2 ** 16 = 65536

2**16 can be represented as a 16 bit binary numbeer

therefore we can convert every number from 1 -> 65536 into 16-bit binary, then use np.reshape() to reshape it into a 4x4 grid, thus covering all possible combinations of 4x4 grids

then run the simulation on each grid as initial state, keeping track of which grid produces the higher number of live cells after 15 time steps.

after 65636 iterations, output the best grid

--------------------------------------------------------------------
#testing 

binary_form = format(65535, '016b')
binary_into_array = np.array([int(k) for k in str(binary_form)])    
binary_4by4 = binary_into_array.reshape((4,4))
print(binary_4by4)
'''

best_count_alive = 0
best_initial_config = None
best_data = None
for i in range(1,65536):
    #converting i into 16 bit binary    
    binary_form = format(i, '016b')
    binary_into_array = np.array([int(k) for k in str(binary_form)])    
    binary_4by4 = binary_into_array.reshape((4,4))
    
    X_test = simulate(15,4,4,binary_4by4)
    final_state = X_test[-1]
    count_alive = np.sum(final_state)
    
    if count_alive > best_count_alive:
        best_initial_config = binary_4by4.copy()
        best_count_alive = count_alive
        best_data = X_test.copy()

gif_filename = "optimum configuration of 4 by 4 game of life grid, found by searching through all combinations.gif"
title = "Optimum configuration of 4 by 4 to yield highest alive cells"
animate_simulation(best_data, gif_filename, title)


