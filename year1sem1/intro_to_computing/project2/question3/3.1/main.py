import numpy as np
import matplotlib.pyplot as plt


def generate_random_grid(row,col):
    matrix = np.random.rand(row, col)
    thresholded = np.where(matrix < 0.5, 0, 1)
    return thresholded

def count_live_neighbours(grid, coordinate):
    x = coordinate[0]-1
    y = coordinate[1]-1
    counter = 0

    for i in [-1,0,1]:
        for k in [-1,0,1]:
            if i == 0 and k == 0: 
                continue
            if grid[x+i, y+k] == 1:
                counter += 1

    return counter


matrix1 = generate_random_grid(5,5)
matrix2 = generate_random_grid(5,5)
matrix3 = generate_random_grid(5,5)

fig, ax = plt.subplots(1,3)
ax[0].imshow(matrix1, cmap= "gray")
ax[1].imshow(matrix2, cmap= "gray")
ax[2].imshow(matrix3, cmap= "gray")

plt.tight_layout()

for a in ax:
    a.set_xticks([])
    a.set_yticks([])
    a.scatter(0, 0, s=200, facecolors='none', edgecolors='red', linewidths=2)


plt.show()
