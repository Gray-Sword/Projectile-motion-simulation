import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(v0, angle, g=9.81):

    angle_rad = np.radians(angle) 

    t_flight = 2 * v0 * np.sin(angle_rad) / g

    t = np.linspace(0, t_flight, num=500)

    x = v0 * np.cos(angle_rad) * t
    y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2

    return x, y

v0 = float(input("Enter the initial velocity (m/s): "))
angle = float(input("Enter the launch angle (degrees): "))

x, y = projectile_motion(v0, angle)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f"v0 = {v0} m/s, angle = {angle}°")
plt.title("Projectile Motion")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.grid()
plt.axhline(0, color='black',linewidth=0.5)
plt.legend()
plt.show()
