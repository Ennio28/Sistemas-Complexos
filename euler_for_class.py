import simcx



class EulerSimulator(simcx.simulators.Simulator):
    def __init__(self, func, init_state, Dt):
        super(EulerSimulator, self).__init__()
        self._func = func
        self.x = [0]
        self.y = [init_state]
        self.Dt = Dt


    def step(self, delta=0):
        i = 0
        self.y += [self.y[-1] + self._func(self.y[-1]) * self.Dt]
        self.x += [self.x[-1] + self.Dt]
        i+= 1


class EulerVisual(simcx.MplVisual):
    def __init__(self, sim : EulerSimulator):
        super(EulerVisual, self).__init__(sim)
        self.ax = self.figure.add_subplot(111)
        self.l, = self.ax.plot(self.sim.x, self.sim.y, '-.')

    def draw(self):
        self.l.set_data(self.sim.x, self.sim.y)
        self.ax.relim()
        self.ax.autoscale_view()


def simple_function(x):
    return 3

def simple_function2(x):
    return 2 * x

def squared(x):
    return x**2

if __name__ == "__main__":
    Dt = 0.1
    sim = EulerSimulator(simple_function2, 1.0, Dt)
    vis = EulerVisual(sim)
    display = simcx.Display()
    display.add_simulator(sim)
    display.add_visual(vis)
    simcx.run()
