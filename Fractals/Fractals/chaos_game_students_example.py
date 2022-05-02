import simcx
from matplotlib.transforms import Affine2D


def triangle():
    t1 = Affine2D().scale(0.5, 0.5)
    t2 = Affine2D().scale(0.5, 0.5).translate(0.5, 0)
    t3 = Affine2D().scale(0.5, 0.5).translate(0.25, 0.5)

    s = [1/3] * 3

    return [t1, t2, t3], s

def square():
    a = 1/3
    t1 = Affine2D().scale(a, a)
    t2 = Affine2D().scale(a, a).translate(0, a)
    t3 = Affine2D().scale(a, a).translate(0, a*2)

    t5 = Affine2D().scale(a, a).translate(a, 0)
    t6 = Affine2D().scale(a, a).translate(a, a*2)

    t7 = Affine2D().scale(a, a).translate(a*2, 0)
    t8 = Affine2D().scale(a, a).translate(a*2, a)
    t9 = Affine2D().scale(a, a).translate(a*2, a*2)

    s = [1 / 8] * 8

    return [t1, t2, t3,t5,t6,t7,t8,t9], s

def kochcurve():
    a = 1/3

    t1 = Affine2D().scale(a, a)
    t2 = Affine2D().scale(a, a).rotate_deg(60).translate(a,0)
    t3 = Affine2D().scale(a, a).rotate_deg(-60).translate(0.5, 3**0.5/6)
    t4 = Affine2D().scale(a, a).translate(a*2, 0)

    s = [1/4] * 4
    return [ t1, t2, t3, t4], s

def snowflake():
    a = 1/3

    t1 = Affine2D().scale(1/3**.5 , 1/3**.5).rotate_deg(30)
    t2 = Affine2D().scale(1/3, 1/3).translate(1/3**.5, 1/3)
    t3 = Affine2D().scale(1/3, 1/3).translate(0, 2/3)
    t4 = Affine2D().scale(1/3, 1/3).translate(-1/3**.5, 1/3)
    t5 = Affine2D().scale(1/3, 1/3).translate(-1/3**.5, -1/3)
    t6 = Affine2D().scale(1/3, 1/3).translate(0, -2/3)
    t7 = Affine2D().scale(1/3, 1/3).translate(1/3**.5, -1/3)



    s = [1/7] * 7
    return [ t1, t2, t3, t4,t5,t6,t7], s


if __name__ == '__main__':
    transform, probs = triangle()
    sim = simcx.simulators.IFS(transform, probs, step_size=1000)
    vis = simcx.visuals.Points2D(sim)

    display = simcx.Display()
    display.add_simulator(sim)
    display.add_visual(vis)
    simcx.run()