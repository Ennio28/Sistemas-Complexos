import simcx

def ex1():
    return lambda x : -0.3 * x + 2

def ex2():
    return lambda x : 1.5 * x - 2

def z1(vi):
    return lambda z: k * vi -b * z - u * vi * z

def v1(xi,z):
    return lambda vi: -1 * vi*(r - p * xi - q * z)
def x1():
    vi = 0
    return lambda xi: -1 * c * vi - b * xi - u * vi * xi


k = 0.12442480625185404
b = 0.7236437427328112
u = 0.022024587030908926
c = 0.7097523067646884
r = 0.9666370843400092
p = 0.09614840180599382
q = 0.6954302472082527
v0 = [1]
x0 = [1]
z0 = [1]

if __name__ == '__main__':
    eq_sim1 = simcx.simulators.FunctionIterator(v1(0, 0), v0[0])
    #eq_sim1 = simcx.simulators.FunctionIterator(x1(), x0[0])
    #eq_sim1 = simcx.simulators.FunctionIterator(z1(0), z0[0])
    cobweb = simcx.visuals.CobWebVisual(eq_sim1, -2, 2, 'func', width=800, height=800)
    #cobweb2 = simcx.visuals.CobWebVisual(eq_sim2, 0, 5, 'func', width=800, height=600)
    #cobweb3 = simcx.visuals.CobWebVisual(eq_sim3, 0, 5, 'func', width=800, height=600)

    display = simcx.Display()
    display.add_simulator(eq_sim1)
   # display.add_simulator(eq_sim2)
   # display.add_simulator(eq_sim3)

    display.add_visual(cobweb)
    ##display.add_visual(cobweb2)
    #display.add_visual(cobweb3)

    simcx.run()