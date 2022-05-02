from pylab import *

#k = 0.45417337083720355
b = -0.45482582469388344
u = 0.8452628018285122
c = 0.966378536424239
r = 0.8976409287479137
p = 0.3730231282375587
q = 0.07271925334265861

def initialize():
    global x,v,z, result
    x = 1.2320968490204192
    v = 2.4298860334362407
    z = 2.0218848811803576
    result = []

def observe():
    global x,v,z, result
    result.append(z)

def update():
    global x,v,z, result
    x = x + xi(v,x)
    v = v + vi(v,x,z)
    z = z + zi(z,v)


def vi(vi, xi, z):
    t = vi  + (-1 * vi * (r - p * xi - q * z))
    if t < 0:
        return 0
    return t
def xi(vi, xi):
    t = xi + (-1 * c * vi - b * xi - u * vi * xi)
    if t < 0:
        return 0
    return t
def zi(z, vi):
    t = z + (k * vi - b * z - u * vi * z)
    if t < 0:
        return 0
    return t
def plot_asymptotic_states():
    initialize()
    for t in range(2500):  # first 100 steps are discarded
        update()
    for t in range(2500):  # second 100 steps are collected
        update()
        observe()
    plot([k] * 2500, result,'b.', alpha = 0.1)

for k in arange(0, 50, 0.01):
    plot_asymptotic_states()

xlabel('r')
ylabel('x')
show()