import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Drone:
    def __init__(self, mass, area, drag_coefficient, thrust):
        self.mass = mass  
        self.drag_coefficient = drag_coefficient 
        self.thrust = thrust  
        self.position = np.array([0.0, 0.0, 0.0])

    def update_position(self, t):
        """Update the drone's position to follow a helical path"""
        radius = 5  # Radius of the helical path
        speed = 0.1  # Speed of rotation
        vertical_speed = 0.05  # Speed at which the drone gains altitude

        self.position[0] = radius * np.cos(speed * t)  # X position
        self.position[1] = radius * np.sin(speed * t)  # Y position
        self.position[2] = vertical_speed * t  # Z position


def update_plot(i, drone, line):
    drone.update_position(i)
    xs.append(drone.position[0])
    ys.append(drone.position[1])
    zs.append(drone.position[2])
    line.set_data(xs, ys)
    line.set_3d_properties(zs)
    return line,

my_drone = Drone(mass=1.5, area=0.1, drag_coefficient=0.3, thrust=20)
time_steps = 100

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([0, 10])
ax.set_xlabel('X position')
ax.set_ylabel('Y position')
ax.set_zlabel('Z position (Altitude)')

xs, ys, zs = [], [], []
line, = ax.plot([], [], [], lw=2)

ani = FuncAnimation(fig, update_plot, frames=np.arange(0, time_steps),
                    fargs=(my_drone, line), interval=100, blit=False)
plt.show()

