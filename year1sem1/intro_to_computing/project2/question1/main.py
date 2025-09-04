import numpy as np
from utils import density, plot_earth
import matplotlib.pyplot as plt

C_d = 0.8

SID: 550388193
A = 9
B = 3


#question 1
def compute_drag_force(altitude, v_x, v_y):
    rho = density(altitude)
    v_total = np.sqrt(v_x**2 + v_y**2)


    drag_force_x = 0.5 * rho * C_d * v_x * v_total
    drag_force_y = 0.5 * rho * C_d * v_y * v_total


    return np.array([drag_force_x, drag_force_y])

example_drag_forces = compute_drag_force(200e3, (A+0.5)*1000, (B+0.5)*1000)

print(f'Example drag force x direction: {example_drag_forces[0]:.2f}')
print(f'Example drag force y direction: {example_drag_forces[1]:.2f}') 

#Question 2
## code from 1.1 ##
mu = 3.986e14           # Gravitational parameter for Earth (m^3/s^2)
earth_rad = 6378e3      # Radius of Earth (m)

t_max = 6 * 60 * 60      # Maximum simulation time (s)
dt = 0.1                # Time step (s)
n_steps = int(t_max/dt) # Total number of simulation steps

x0 = 200e3 + earth_rad  # Initial x position, including radius of Earth (m)
y0 = 0                  # Initial y position (m)
vx0 = 0                 # Initial x velocity (m/s)
vy0 = 9e3

#vy0 = ((2/9.9) * (9 + 0.1 * 3) + 7.5) * 1000            # Initial y velocity (m/s)

def generate_state_vector(x0, y0, vx0, vy0):
    X = np.zeros((n_steps+1, 4))        # Set up a state array (fill in below)
    X[0] = np.array([x0, y0, vx0, vy0]) # Set the initial state
    return X

def satellite_dynamics(X_k, mu, dt, drag_force = False):

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
    if drag_force:
        vx_next = vx - ((mu/(r**3)) * x + compute_drag_force(r-earth_rad, vx, vy)[0]) * dt
        vy_next = vy - ((mu/(r**3)) * y + compute_drag_force(r-earth_rad, vx, vy)[1]) * dt 
    else: 
        vx_next = vx - (mu/(r**3)) * x  * dt
        vy_next = vy - (mu/(r**3)) * y  * dt 


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


x_without_drag = generate_state_vector(x0,y0,vx0,vy0)
x_with_drag = generate_state_vector(x0,y0,vx0,vy0)


for k in range(n_steps):
    x_without_drag[k+1] = satellite_dynamics(x_without_drag[k], mu, dt, drag_force = False)
    x_with_drag[k+1] = satellite_dynamics(x_with_drag[k], mu, dt, drag_force = True)

x_without_drag_values = x_without_drag[:,0]
y_without_drag_values = x_without_drag[:,1]
altitude_without_drag = np.sqrt(x_without_drag_values**2 + y_without_drag_values**2) - earth_rad

x_with_drag_values = x_with_drag[:,0]
y_with_drag_values = x_with_drag[:,1]
altitude_with_drag = np.sqrt(x_with_drag_values**2 + y_with_drag_values**2) - earth_rad


#plotting the two graphs

# Figure for graph without drag
fig1, ax1 = plt.subplots()
ax1.plot(x_without_drag_values, y_without_drag_values, color="red")
ax1.set_title("Trajectory of sattelite without drag force applied")
ax1.set_xlabel("x (m)")
ax1.set_ylabel("y (m)")
ax1.grid()
plot_earth(ax1)
ax1.set_aspect("equal")
fig1.savefig("Trajectory of sattelite without drag force applied", dpi=300)

# Figure for graph with drag
fig2, ax2 = plt.subplots()
ax2.plot(x_with_drag_values, y_with_drag_values, color="red")
ax2.set_title("Trajectory of sattelite with drag force applied")
ax2.set_xlabel("x (m)")
ax2.set_ylabel("y (m)")
ax2.grid()
plot_earth(ax2)
ax2.set_aspect("equal")
fig2.savefig("Trajectory of sattelite with drag force applied.png", dpi=300)


#This is not related but just for me to visualise

#plotting altitudes of satellite with and without drag forces 
time = np.arange(0, (n_steps + 1) * dt, dt)

#plotting altitudes against time for each cases:

fig, ax = plt.subplots()
plt.plot(time, altitude_without_drag, label="without drag", color="red", linestyle = "--")
plt.plot(time, altitude_with_drag, label="with drag", color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Altitudes (m)")
plt.xlim(0, 22000)
plt.ylim(0,7e6)
plt.title("Altitudes of both satellites with and without drag over time")
plt.grid()
plt.legend()
plt.savefig("Altitudes of satellite with and without drag force agains time.png", dpi=300)
plt.show()

#question 3: 
#decreasing the altitude in increments of 50 until altitude < 10km
minimum_initial_altitude = None
for altitude_initial in range(200, 9, -50):
    x0_test = altitude_initial * 1000 + earth_rad
    y0_test = 0
    vx0_test = 0
    vy0_test = 9e3

    X_test = generate_state_vector(x0_test, y0_test, vx0_test, vy0_test)

    crash = False
    for k in range(n_steps):
        X_test[k+1] = satellite_dynamics(X_test[k], mu, dt, drag_force = True)
        r = np.sqrt(X_test[k+1][0]**2 + X_test[k+1][1]**2) 
        altitude = r - earth_rad

        if altitude < 10000: 
            crash = True
            break
    if crash == False:
        minimum_initial_altitude = altitude_initial

    else: 
        break


for altitude_initial in range(minimum_initial_altitude+50, 9, -10):
    x0_test = altitude_initial * 1000 + earth_rad
    y0_test = 0
    vx0_test = 0
    vy0_test = 9e3

    X_test = generate_state_vector(x0_test, y0_test, vx0_test, vy0_test)

    crash = False
    for k in range(n_steps):
        X_test[k+1] = satellite_dynamics(X_test[k], mu, dt, drag_force = True)
        r = np.sqrt(X_test[k+1][0]**2 + X_test[k+1][1]**2) 
        altitude = r - earth_rad

        if altitude < 10000: 
            crash = True
            break
    if crash == False:
        minimum_initial_altitude = altitude_initial

    else: 
        break


for altitude_initial in range(minimum_initial_altitude+10, 9, -1):
    x0_test = altitude_initial * 1000 + earth_rad
    y0_test = 0
    vx0_test = 0
    vy0_test = 9e3

    X_test = generate_state_vector(x0_test, y0_test, vx0_test, vy0_test)

    crash = False
    for k in range(n_steps):
        X_test[k+1] = satellite_dynamics(X_test[k], mu, dt, drag_force = True)
        r = np.sqrt(X_test[k+1][0]**2 + X_test[k+1][1]**2) 
        altitude = r - earth_rad

        if altitude < 10000: 
            crash = True
            break
    if crash == False:
        minimum_initial_altitude = altitude_initial

    else: 
        break

if minimum_initial_altitude == None: 
    print("The satellite crashes even at 200km")
else: 
    print(f"Minimum safe initial altitude that would not cause a crash in a 6 hour period is {minimum_initial_altitude:.0f} km")

#output is 108 km



