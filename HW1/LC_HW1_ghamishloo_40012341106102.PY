import numpy as np
import matplotlib.pyplot as plt

M_alpha = -8.790  
M_q = -2.075      
M_delta_E = -11.87 

theta_0 = 0.0     
theta_dot_0 = 0.0 

dt = 0.01         
t_max = 10        
t = np.arange(0, t_max, dt)

delta_E_values = [-5, 0, +10]  

delta_E_values_rad = np.deg2rad(delta_E_values)

def euler_method(theta_0, theta_dot_0, delta_E, t, dt):
    theta = np.zeros(len(t))
    theta_dot = np.zeros(len(t))
    
    theta[0] = theta_0
    theta_dot[0] = theta_dot_0
    
    for i in range(1, len(t)):
        theta_dot[i] = theta_dot[i-1] + (M_alpha * theta[i-1] + M_q * theta_dot[i-1] + M_delta_E * delta_E) * dt
        theta[i] = theta[i-1] + theta_dot[i-1] * dt
    
    return theta, theta_dot


plt.figure(figsize=(10, 6))

for delta_E in delta_E_values_rad:
    theta, theta_dot = euler_method(theta_0, theta_dot_0, delta_E, t, dt)
    plt.plot(t, np.rad2deg(theta), label=f'$\delta_E$ = {np.rad2deg(delta_E):.0f} deg')

plt.xlabel('Time (s)')
plt.ylabel('Pitch Angle $\theta$ (deg)')
plt.title('Pitch Angle vs Time for Different Elevator Deflections')
plt.legend()
plt.grid(True)
plt.show()