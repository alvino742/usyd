import numpy as np
from utils import density, plot_earth
import matplotlib.pyplot as plt

C_d = 0.8

SID: 550388193
A = 9
B = 3


def compute_drag_force(altitude, v_x, v_y):
    rho = density(altitude)
    v_total = np.sqrt(v_x**2 + v_y**2)


    drag_force_x = 0.5 * rho * C_d * v_x * v_total
    drag_force_y = 0.5 * rho * C_d * v_y * v_total


    return np.array([drag_force_x, drag_force_y])


## code from 1.1 ##
mu = 3.986e14           # Gravitational parameter for Earth (m^3/s^2)
earth_rad = 6378e3      # Radius of Earth (m)

t_max = 300 * 60         # Maximum simulation time (s)
dt = 0.1                # Time step (s)
n_steps = int(t_max/dt) # Total number of simulation steps

x0 = 200e3 + earth_rad  # Initial x position, including radius of Earth (m)
y0 = 0                  # Initial y position (m)
vx0 = 0                 # Initial x velocity (m/s)
vy0 = 9e3

#vy0 = ((2/9.9) * (9 + 0.1 * 3) + 7.5) * 1000            # Initial y velocity (m/s)

X = np.zeros((n_steps+1, 4))        # Set up a state array (fill in below)
X[0] = np.array([x0, y0, vx0, vy0]) # Set the initial state

def satellite_dynamics(X_k, mu, dt):

    # Split up the state vector
    x = X_k[0]
    y = X_k[1]
    vx = X_k[2]
    vy = X_k[3]

    # Compute the distance from Earth
    r = np.sqrt(x**2 + y**2)

    # Update the states
    x_next = x + vx * dt
    y_next = y + vy * dt
    vx_next = vx - (mu/(r**3) * x + compute_drag_force(x-earth_rad, vx, vy)[0]) * dt
    vy_next = vy - (mu/(r**3) * y + compute_drag_force(x-earth_rad, vx, vy)[1]) * dt 

    #crash:
    r_next = np.sqrt(x_next**2 + y_next**2)
    if r_next <= earth_rad:
        x_next = x_next * earth_rad / r_next
        y_next = y_next * earth_rad / r_next
        vx_next = 0
        vy_next = 0

    # Store and return the new state
    X_next = np.array([x_next, y_next, vx_next, vy_next])
    return X_next

for k in range(n_steps):
    X[k+1] = satellite_dynamics(X[k], mu, dt)

x_values = X[:,0]
y_values = X[:,1]

# Make a plot
plt.plot(x_values, y_values, color="red")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Satellite orbit")
plt.grid()

# Add the Earth to the plot
ax = plt.gca()
plot_earth(ax)

# Make sure aspect ratio is equal
ax.set_aspect("equal")
plt.savefig("satelite orbit.png")
plt.show() 

## code from 1.1 ##
'''
example_drag_forces = compute_drag_force(200e3, (A+0.5)*1000, (B+0.5)*1000)

print(f'Example drag force x direction: {example_drag_forces[0]:2f}')
print(f'Example drag force y direction: {example_drag_forces[1]:2f}') 
'''
