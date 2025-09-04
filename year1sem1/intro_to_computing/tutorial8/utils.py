import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

def animate_ball(y, dt, filename="falling_ball.mp4"):

    radius = 0.4    # Size of ball (m)
    frames = len(y) # Number of frames in the animation

    # Create the figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim(-2, 2)
    ax.set_ylim(0, y[0] + 5)
    ax.set_aspect('equal')
    plt.xlabel("Horizontal Position (m)")
    plt.ylabel("Height (m)")
    plt.title("Ball Falling Under Gravity")
    plt.grid(True)

    # Add a horizontal line to represent the floor
    floor = plt.axhline(y=0, color='black', linewidth=2)

    # Create the ball as a circle
    ball = plt.Circle((0, y[0]), radius, color="blue")
    ax.add_patch(ball)

    # Update function for animation
    def update(frame):
        ball.center = (0, y[frame])
        return ball,

    # Create the animation and save as MP4
    ani = FuncAnimation(fig, update, frames=frames, interval=dt * 1000, blit=True)
    writer = FFMpegWriter(fps=int(1/dt), metadata={"title": "Ball Falling"})
    ani.save(filename, writer=writer)

    return ani
