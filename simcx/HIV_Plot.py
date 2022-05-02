

from pylab import *
from mpl_toolkits.mplot3d import Axes3D

k = 0.22498816822190482
b = 0.7661122889607678
u = 0.30784246407294336
c = 0.0431206338073481
r = 0.9911087987648054
p = 0.464914462021499
q = 0.6241527730241279
Dt = 0.01

def initialize():
    global x, xresult, v, vresult, z, zresult, t, timesteps
    v= 1.4755312880538518
    x = 0.8629097636376801
    z = 0.029004334017156852
    xresult = [x]
    vresult = [v]
    zresult = [z]
    t = 0.
    timesteps = [t]

def observe():
    global x, xresult, v, vresult, z, zresult, t, timesteps
    xresult.append(x)
    vresult.append(v)
    zresult.append(z)
    timesteps.append(t)

def update():
    global x, xresult, v, vresult, z, zresult, t, timesteps
    nextx = x + (-c*v -b*x - u*v*x) * Dt
    nextv = v + (-r*v + p*x*v +q*z*v) * Dt
    nextz = z + (k*v - b* z -u*v*z) * Dt
    x, v, z = nextx, nextv, nextz
    t = t + Dt

initialize()
while t < 50.:
    update()
    observe()

subplot(3, 1, 1)
plot(timesteps, xresult)
xlabel('t')
ylabel('x')

subplot(3, 1, 2)
plot(timesteps, vresult)
xlabel('t')
ylabel('y')

subplot(3, 1, 3)
plot(timesteps, zresult)
xlabel('t')
ylabel('z')

figure()
ax = gca(projection='3d')
ax.plot(xresult, vresult, zresult, 'b')

show()