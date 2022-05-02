from __future__ import division
import simcx


def logistic_final_state(r):
    return lambda x: r*x*(1-x)


x0 = [0.1]
r = 4
if __name__ == '__main__':
    sim = simcx.simulators.FunctionIterator(logistic_final_state(r), x0)
    vis = simcx.visuals.FinalStateDiagram(sim, discard_initial=100)
    vis.ax.set_xlabel('r')


    display = simcx.Display()
    display.add_simulator(sim)
    display.add_visual(vis)

    simcx.run()


