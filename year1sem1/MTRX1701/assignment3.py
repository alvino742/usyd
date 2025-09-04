import numpy as np
import matplotlib.pyplot as plt 

def derivatives(X_k, u_k):
    # Put your code here

    X_dot_k = np.array([u_k[0]*np.cos(X_k[2]),u_k[0]*np.sin(X_k[2]),u_k[1]])

    # return X_dot_k
    return X_dot_k

# function: vehicle_model
# inputs:
#   X_k - robot state at time k
#   u_k - control input
#   dt - time since last update
# returns:
#   X_xp1 - robot state at next time k+1
def vehicle_model(X_k, u_k, dt):
    # Put your code here

    dX_k = derivatives(X_k, u_k)
    X_kp1 = X_k + dt * dX_k
    
    # return X_k+1
    return X_kp1

def control_vector(v_r, v_l, d):

    v = (v_r + v_l)/2
    psi_dot = (v_r - v_l)/ (2*d)

    u_k = np.array([v,psi_dot])

    return u_k


v_max = 192.89
d = 50
X_0 = np.array([0,0,0])
dt = 0.1
t_end = 10
list1 = []

time_steps = t_end/dt
X_k = np.array([0.0, 0.0, 0.0])
u_k = control_vector(v_max, v_max, d)
for _ in range(int(time_steps)):
    X_k = vehicle_model(X_k, u_k, dt)
    list1.append(X_k.copy())

x_vals = [pos[0] for pos in list1]
y_vals = [pos[1] for pos in list1]

# Plot the trajectory
plt.figure(figsize=(4, 4))
plt.scatter(x_vals, y_vals, c='blue', s=20, label='Robot Positions')  # no lines
plt.plot(x_vals[-1]+12, y_vals[-1]-50, marker='^', color='red', markersize=10, label='Final Position after 10 seconds: 1928.9mm')
plt.title("vehicle motion with both wheels \nrunning full speed for 10 seconds, d = 50mm, dt = 0.1s")
plt.xlabel("x position (mm)")
plt.ylabel("y position (mm)")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()  # ✅ Save the plot
