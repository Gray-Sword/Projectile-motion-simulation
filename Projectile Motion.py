import numpy as np
import matplotlib.pyplot as plt


def projectile_motion(v0, angle, h0=0, air_resistance=False):
 
    g = 9.81  
    angle_rad = np.radians(angle)  
    
    dt = 0.01
    t = [0]
    
    x, y = [0], [h0]
    vx = v0 * np.cos(angle_rad)
    vy = v0 * np.sin(angle_rad)
    
    mass = 1.0  
    drag_coefficient = 0.05  
    
    while y[-1] >= 0:  
        if air_resistance:
            speed = np.sqrt(vx**2 + vy**2)
            drag_force = drag_coefficient * speed**2
            ax = -drag_force * vx / (mass * speed)
            ay = -g - (drag_force * vy / (mass * speed))
        else:
            ax = 0
            ay = -g
        
        vx += ax * dt
        vy += ay * dt
        x.append(x[-1] + vx * dt)
        y.append(y[-1] + vy * dt)
        t.append(t[-1] + dt)
    
    return x, y


v0 = float(input("Enter initial velocity (m/s): "))
angle = float(input("Enter launch angle (degrees): "))
h0 = float(input("Enter initial height (m): "))
air_resistance = input("Include air resistance? (yes/no): ").lower() == 'yes'

x, y = projectile_motion(v0, angle, h0, air_resistance)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Projectile Path", color="blue")
plt.title("Projectile Motion Simulation", fontsize=16)
plt.xlabel("Horizontal Distance (m)", fontsize=14)
plt.ylabel("Vertical Distance (m)", fontsize=14)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.grid(True)
plt.legend()
plt.show()
