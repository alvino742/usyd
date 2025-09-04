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
    

row, col = 20, 20
n_steps = 200

grid_0 = generate_random_grid(row, col)
#testing if the count functions works
#print(count_live_neighbours(grid_0, (0,0)))


X_1 = simulate(n_steps, row, col, grid_0)

final_state = X_1[-1,:,:]
fig0, ax0 = plt.subplots(1,2)

fig0.suptitle("3.2.1 randomly initialised grid over 200 time steps \nBlack means alive, White means dead")

ax0[0].imshow(grid_0, cmap="gray_r")
ax0[0].set_title("Initial")
ax0[1].imshow(final_state, cmap="gray_r")
ax0[1].set_title("After 200 time steps")
plt.tight_layout()
plt.savefig("3.2.1 randomly initialised grid over 200 time steps.png")

#question 3.2.2.1

row1, col1 = 21, 21
grid2_0 = np.zeros((row1, col1))
grid2_0[9:12, 9:12] = 1

X_2 = simulate(n_steps, row1, col1, grid2_0)


gif_filename1 = "3.2.2.1 dead cells with 3x3 live cells in middle for 200 time steps.gif"
title1 = "Game of life, 3x3 middle live cells"
animate_simulation(X_2, gif_filename1, title1)

#question 3.2.2.2

#Assuming shape of grid is still 21 by 21 

for k in [6,7,8,9]:
    row2, col2 = 21, 21
    mid_col = col2 // 2 
    grid3_0 = np.zeros((row2, col2))
    start_row = (row2 - k)//2 

    for i in range(k):
        grid3_0[start_row+i, mid_col] = 1
    

    X_3 = simulate(n_steps, row2, col2, grid3_0)
    
    gif_filename_k = f"3.2.2.2 dead cells with vertical line of {k} cells in the middle.gif"
    title_k = f"Game of life, vertical line length {k}"
    animate_simulation(X_3, gif_filename_k, title_k)
    


plt.show()






