import simcx

from simcx.simulators import FunctionIterator
from simcx.visuals import TimeSeries


def eq1(a):
    def growth(x):
        return a * x

    return growth  # lambda x: a * x


display = simcx.Display()

a = 1.3
# K = 1000
x0 = 2
# x0 = [2,4,10] ->we will see the evolution of the three funcitions with diferent sartting points

simulator = FunctionIterator(eq1(a), x0)

vis = TimeSeries(simulator)

display.add_simulator(simulator)  #call step method
display.add_visual(vis)  # make a visual the new processed point

simcx.run()


"""
in order to have two equations we need to make another simulation
"""