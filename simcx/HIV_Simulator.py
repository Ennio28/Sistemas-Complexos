import random

import numpy as np
import math
import simcx

global k
global b
global u
global c
global r
global p
global q
global v0
global x0
global z0


class HIVSimulator(simcx.Simulator):
    def __init__(self, vi, xi, z, intitial_state_vi, initial_state_xi, initial_state_z, step=1):
        super(HIVSimulator, self).__init__()
        self._xi_func = xi
        self._vi_func = vi
        self._z_func = z
        self._state_xi = initial_state_xi[:]
        self._state_vi = intitial_state_vi[:]
        self._state_z = initial_state_z[:]
        self._n_states = len(self._state_vi)
        self.x = [0]
        self.time = 0
        self._xi = [[state] for state in initial_state_xi]
        self._vi = [[state] for state in intitial_state_vi]
        self._z = [[state] for state in initial_state_z]

    def step(self, delta=0):
        self.time += 1
        for i in range(self._n_states):
            old_xi_state = self._state_xi[i]
            old_vi_state = self._state_vi[i]
            old_z_state = self._state_z[i]
            #print("xi: %.10f \nvi: %.10f \nz: %.10f " % (old_xi_state, old_vi_state, old_z_state))

            self._state_xi[i] = self._xi_func( old_vi_state,old_xi_state)
            self._xi[i].append(self._state_xi[i])
            # old_xi_state = self._state_xi[i]

            self._state_vi[i] = self._vi_func(old_vi_state, old_xi_state, old_z_state)
            self._vi[i].append(self._state_vi[i])

            self.x.append(self.time)  # eixo dos x

            self._state_z[i] = self._z_func(old_z_state, old_vi_state)
            self._z[i].append(self._state_z[i])


class HIVVisual(simcx.MplVisual):
    def __init__(self, sim):
        super(HIVVisual, self).__init__(sim)
        self.ax = self.figure.add_subplot(111)
        self.l, = self.ax.plot(self.sim.x, self.sim._xi, '-', label="xi")
        self.l1, = self.ax.plot(self.sim.x, self.sim._vi, '-', label="vi")
        self.l2, = self.ax.plot(self.sim.x, self.sim._z, '-', label="z")

        self.ax.set_xlabel("time")
        self.ax.legend()

    def draw(self):
        self.l.set_data(self.sim.x, self.sim._xi)
        self.l1.set_data(self.sim.x, self.sim._vi)
        self.l2.set_data(self.sim.x, self.sim._z)
        self.ax.relim()
        self.ax.autoscale_view()


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

def z(z, vi):
    t = z + (k * vi - b * z - u * vi * z)
    if t < 0:
        return 0
    return t


def linear():

    global k
    global b
    global u
    global c
    global r
    global p
    global q
    global v0
    global x0
    global z0
    k = 0.12442480625185404
    b = 0.7236437427328112
    u = 0.022024587030908926
    c = 0.7097523067646884
    r = 0.9666370843400092
    p = 0.09614840180599382
    q = 0.6954302472082527
    v0 = [3.4603066040025974]
    x0 = [4.250350554154812]
    z0 = [1.4501681222276335]


def chaotic():
    global k
    global b
    global u
    global c
    global r
    global p
    global q
    global v0
    global x0
    global z0
    x0 = [1.2320968490204192]
    v0 = [2.4298860334362407]
    z0 = [2.0218848811803576]
    k = 0.45417337083720355
    b = -0.45482582469388344
    u = 0.8452628018285122
    c = 0.966378536424239
    r = 0.8976409287479137
    p = 0.3730231282375587
    q = 0.07271925334265861


def periodic():
    global k
    global b
    global u
    global c
    global r
    global p
    global q
    global v0
    global x0
    global z0
    x0 = [0.604275697582336]
    v0 = [0.67048370620909]
    z0 = [0.15451007937415162]
    k = 0.06319226271725653
    b = -0.8026310615455257
    u = 0.4755867761890036
    c = -0.3543348404606479
    r = -0.8330282398491504
    p = -0.1889978596607591
    q = 0.3227333626934952



def chaotic2():

    global k
    global b
    global u
    global c
    global r
    global p
    global q
    global v0
    global x0
    global z0

    k = random.uniform(-1,1)
    b = random.uniform(-1,1)
    u = random.uniform(-1,1)
    c = random.uniform(-1,1)
    r = random.uniform(-1,1)
    p = random.uniform(-1,1)
    q = random.uniform(-1 ,1)


    v0 = [random.uniform(0,2)]
    x0 = [random.uniform(0,2)]
    z0 = [random.uniform(0,2)]

    import os
    os.system('clear')
    print("x0 = [" + x0[0].__str__()+ "]")
    print("v0 = [" + v0[0].__str__()+ "]")
    print("z0 = [" + z0[0].__str__() + "]")
    print("k = " + k.__str__())
    print("b = " + b.__str__())
    print("u = " + u.__str__())
    print("c = " + c.__str__())
    print("r = " + r.__str__())
    print("p = " + p.__str__())
    print("q =  " + q.__str__())

periodic()
sim = HIVSimulator(vi, xi, z, v0, x0, z0)
vis = HIVVisual(sim)

display = simcx.Display()
display.add_simulator(sim)
display.add_visual(vis)
simcx.run()

# azul e o xi
# laraja e o vi
# verde e o z

"""
periodic 
x0 = [0.2866655903001992]
v0 = [1.658747741373268]
z0 = [1.686685066519443]
k = -0.9528855794900433
b = -0.24292535790031722
u = 0.7856774397459927
c = -0.6998075356916964
r = -0.622159378913165
p = -0.08330527759107698
q =  0.31217608574908584 

"""
"""
mais perto de caotico
x0 = [1.2320968490204192]
v0 = [2.4298860334362407]
z0 = [2.0218848811803576]
k = 0.45417337083720355
b = -0.45482582469388344
u = 0.8452628018285122
c = 0.966378536424239
r = 0.8976409287479137
p = 0.3730231282375587
q =  0.07271925334265861

"""
"""
3 linears with no zero values
x0 = [0.09037890113926106]
v0 = [0.8733831718770466]
z0 = [1.2518948538986587]
k = 0.948165797500546
b = 0.18994839614510717
u = 0.20716545559116506
c = -0.46064436062423253
r = -0.5320555911344476
p = 0.31900544164027567
q =  -0.7008804089471798


"""
"""
as 3 periodicas 
x0 = [0.604275697582336]
v0 = [0.67048370620909]
z0 = [0.15451007937415162]
k = 0.06319226271725653
b = -0.8026310615455257
u = 0.4755867761890036
c = -0.3543348404606479
r = -0.8330282398491504
p = -0.1889978596607591
q =  0.3227333626934952

"""

"""
2 periodicos e 1 linear
x0 = [0.030065098245442234]
v0 = [1.9772086107748197]
z0 = [1.4647158383378802]
k = 0.07171773322240282
b = 0.4133838997935442
u = 0.6927001532892643
c = 0.2105659291173123
r = -0.17295699984388269
p = -0.7514505729330483
q =  -0.22508135033016186


"""

"""
2 periodicos e 1 linear
x0 = [0.9534940907065732]
v0 = [1.699375779740957]
z0 = [1.3850027023240443]
k = 0.6475196246946215
b = -0.35446708609588296
u = 0.9583934508792413
c = 0.6602423298654747
r = -0.5842538384033318
p = 0.24995842195216178
q =  -0.1877578401281943

"""
"""
chaotic 
x0 = [1.2266316771861558]
v0 = [0.3665334220527041]
z0 = [0.8066682606757656]
k = 0.6547673847039939
b = 0.9605255800572661
u = -0.908883840594398
c = -0.5542512390433671
r = -0.593931558025087
p = -0.3601994453005015
q =  -0.4464162528277118


"""

"""
lienar 
x0 = [0.32601643077432185]
v0 = [0.47416480276924355]
z0 = [1.504237340279932]
k = 0.3886365372111653
b = 0.7660424971293502
u = -0.9507980754587673
c = -0.23631897850018246
r = -0.024738389495263746
p = -0.8745603390314385
q =  -0.1283814788570592
"""

"""
chaotic 
x0 = [0.33628515220675315]
v0 = [0.7099693966148926]
z0 = [1.1524546234132238]
k = -0.8518696402046306
b = -0.466018120708686
u = 0.2904347505929743
c = -0.09085101024078024
r = 0.9684071772582401
p = 0.910685600178589
q =  0.5642289168507946
"""

"""
linear
x0 = [0.6067303966875148]
v0 = [0.23592797714277003]
z0 = [0.22450050203760674]
k = 0.47841057690363087
b = 0.6833454481032806
u = -0.19418305449266038
c = -0.4020330422978484
r = -0.5462128647197746
p = -0.39485780371178425
q =  -0.27964581727995297


"""
"""
periodic 
x0 = [0.09037853220210756]
v0 = [0.19032586078609826]
z0 = [1.2715656261018466]
k = -0.7109615821986925
b = 0.6631034159095053
u = 0.9831018383547925
c = -0.16158311496185074
r = -0.10399408304507718
p = -0.6063954029334548
q =  -0.613680323528758 
"""

"""
good linear 
x0 = [0.054860489530661694]
v0 = [0.5888585838687885]
z0 = [1.4690973259255442]
k = 0.7207790085804264
b = 0.8566381427976779
u = 0.07955290482250144
c = -0.36286047460543713
r = -0.575907636089783
p = 0.09287266122633797
q =  -0.15983849314778742

"""
"""
x0 = [0.6543137563020933]
v0 = [1.4513404940222856]
z0 = [1.078499452015581]
k = -0.7525780896298673
b = 0.9294969049208377
u = 0.9503014194304535
c = -0.7811713568965319
r = -0.4463118122554304
p = -0.8255582241660502
q =  0.4098847819056244 
"""