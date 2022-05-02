import simcx

class TankSimulator(simcx.Simulator):
    def __init__(self,country_x,country_y,intitial_state_x,initial_state_y,step=1):
        super(TankSimulator, self).__init__()
        self.country_x = country_x
        self.country_y = country_y
        self._state_x = intitial_state_x
        self._state_y = initial_state_y
        self._n_states = len(self._state_x)
        self.x = [0]
        self.time = 0
        self.country_x = [[state] for state in intitial_state_x]
        self.country_y = [[state] for state in initial_state_y]

        def step(self, delta=0):
            self.time +=1
            for i in range(self._n_states):
                old_x_state = self._state_x[i]
                self._state_x[i] = self.coutry_x_func(self._state_x[i],self._state_y[i])
                self.coutry_x[i].append(self._state_x[i])
                self._state_y[i] = self.coutry_y_func(self._state_y[i],old_x_state)
                self.coutry_y[i].append(self._state_y[i])
                self.x.append(self.time)

class HIVSimulator(simcx.Simulator):
    def __init__(self,vi,xi,z,intitial_state_x,initial_state_y,initial_state_z,step=1):
        super(HIVSimulator, self).__init__()
        self.vi = vi
        self.xi = xi
        self.z = z
        self._state_x = intitial_state_x
        self._state_y = initial_state_y
        self._n_states = len(self._state_x)
        self.x = [0]
        self.time = 0
        self.vi = [[state] for state in intitial_state_x]
        self.xi = [[state] for state in initial_state_y]
        self.z = [[state] for state in initial_state_z]

        def step(self, delta=0):
            self.time +=1
            for i in range(self._n_states):
                old_x_state = self._state_x[i]
                self._state_x[i] = self.coutry_x_func(self._state_x[i],self._state_y[i])
                self.coutry_x[i].append(self._state_x[i])

                self._state_y[i] = self.coutry_y_func(self._state_y[i],old_x_state)
                self.coutry_y[i].append(self._state_y[i])
                self.x.append(self.time)

            for i in range(self._n_states):
                old_x_state = self._state_vi[i]
                self._state_vi[i] = self.vi_func(self._state_vi[i],self._state_xi[i],self._state_z[i])
                self.vi[i].append(self._state_vi)

                self._state_xi[i] = self.coutry_xi_func(old_x_state,self._state_xi[i],self._state_z[i])
                self.coutry_xi[i].append(self._state_xi[i])
                self.x.append(self.time)
                """
                self._state_z[i] = self.coutry_z_func(self._state_z[i])
                self.coutry_z[i].append(self._state_z[i])
                self.x.append(self.time)
                    """




class TanksVisual(simcx.MplVisual):
    def __init__(self,sim):
        super(TanksVisual, self).__init__()
        self.ax = self.figure.add_subplot(111)
        self.l = self.ax.plot(self.sim.x,self.sim.coutry_x, '_')
        self.l1 = self.ax.plot(self.sim.x,self.sim.coutry_y, '_')

    def draw(self):
        self.l.set_data(self.sim.x,self.sim.coutry_x)
        self.l1.set_data(self.sim.x,self.sim.coutry_y)
        self.ax.relim()
        self.ax.autoscale_view()

class HIVVisual(simcx.MplVisual):
    def __init__(self,sim):
        super(HIVVisual, self).__init__()
        self.ax = self.figure.add_subplot(111)
        self.l = self.ax.plot(self.sim.x,self.sim.xi, '_')
        self.l1 = self.ax.plot(self.sim.x,self.sim.vi, '_')

    def draw(self):
        self.l.set_data(self.sim.x,self.sim.xi)
        self.l1.set_data(self.sim.x,self.sim.vi)
        self.ax.relim()
        self.ax.autoscale_view()

def country_x(x,y):
    return x - 0.3*.4*y

def country_y(x,y):
    return y - x*.2*.35

def vi(vi,xi,z):
    r = 1
    p = 1
    q = 1
    z = 1
    return -vi(r - p*xi - q*z)

def xi(vi,xi,z):
    c = 1
    b = 1
    u = 1
    v = 1
    return -c*vi - b * xi - u*v*xi

def z(z):
    if(z < 0 ):
        return 0
    k = 1
    b = 1
    u = 1
    v = 1
    return k * v - b * z - u * v * z


r = 0
p = 0
q = 0
c = 0
u = 0
k = 0

v0 = [0]
x0 = [0]
z0 = [0]

#sim = TankSimulator(country_x,country_y,x0,y0)
sim = HIVSimulator(vi,xi,z,v0,v0,z0)
vis = HIVVisual(sim)

display = simcx.Display()
display.add_simulator(sim)
display.add_visual(vis)

simcx.run()


