import numpy as np
import matplotlib.pyplot as plt

def functions(x, y, z,k):
    #k = 0.45417337083720355
    b = -0.45482582469388344
    u = 0.8452628018285122
    c = 0.966378536424239
    r = 0.8976409287479137
    p = 0.3730231282375587
    q = 0.07271925334265861
    x_dot = -1 * c * y - b * x - u * y * x
    y_dot = -1 * y * (r - p * x - q * z)
    z_dot = k * y - b * z - u * y * z
    return x_dot, y_dot, z_dot


dr = 0.1  # parameter step size
r = np.arange(0, 200, dr)  # parameter range
dt = 0.001  # time step
t = np.arange(0, 10, dt)  # time range

# initialize solution arrays
xs = np.empty(len(t) + 1)
ys = np.empty(len(t) + 1)
zs = np.empty(len(t) + 1)

# initial values x0,y0,z0 for the system

xs[0], ys[0], zs[0] = (1.2320968490204192, 2.4298860334362407, 2.0218848811803576)


# Save the plot points coordinates and plot the with a single call to plt.plot
# instead of plotting them one at a time, as it's much more efficient
r_maxes = []
z_maxes = []
r_mins = []
z_mins = []


for R in r:
    # Print something to show everything is running
    print(f"{R=:.2f}")
    for i in range(len(t)):
        # approximate numerical solutions to system
        x_dot, y_dot, z_dot = functions(xs[i], ys[i], zs[i], R)
        xs[i + 1] = xs[i] + (x_dot * dt)
        if xs[i+1] < 0:
            xs[i + 1] = 0
        ys[i + 1] = ys[i] + (y_dot * dt)
        if ys[i+1] < 0:
            ys[i + 1] = 0
        zs[i + 1] = zs[i] + (z_dot * dt)
        if zs[i+1] < 0:
            zs[i + 1] = 0
    # calculate and save the peak values of the z solution
    for i in range(1, len(zs) - 1):
        # save the local maxima
        if zs[i - 1] < zs[i] and zs[i] > zs[i + 1]:
            r_maxes.append(R)
            z_maxes.append(zs[i])
        # save the local minima
        elif zs[i - 1] > zs[i] and zs[i] < zs[i + 1]:
            r_mins.append(R)
            z_mins.append(zs[i])

    # "use final values from one run as initial conditions for the next to stay near the attractor"
    xs[0], ys[0], zs[0] = xs[i], ys[i], zs[i]


plt.scatter(r_maxes, z_maxes, color="black", s=0.5, alpha=0.2)
#plt.scatter(r_mins, z_mins, color="red", s=0.5, alpha=0.2)

plt.xlim(0, 200)
plt.ylim(-100, 400)
plt.show()