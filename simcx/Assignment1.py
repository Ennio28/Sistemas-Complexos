import simcx
import math
from simcx.simulators import FunctionIterator
from simcx.visuals import TimeSeries

#Exercise 1.2
"""
loan = 80.000
duration = 20 years
monthly_payment = 880.87
interest_rate= 0.01 monthly

1)
loan_n+1 = loan_n * interest_rate - 880.87 
2)
"""
loan = 80000
duration = 20
monthly_payment = 880.87
interest_rate= 1.01


for i in range(72):
    loan = loan * interest_rate - monthly_payment

print(loan)
#2) after 72 months the debt is 71532.10

"""
Exercise 1.4
x_n+1 = sqrt(x_n)
"""
#1)x0 = 2 -> x5 =1,0219

x1 = 2
x2 = 1
x3 = 3/4

for i in range (5):
    x1 = math.sqrt(x1)
    x2 = math.sqrt(x2)
    x3 = math.sqrt(x3)
#2)x0 = 1 -> x5 = 1.0

#3)x0 = 3/4 -> x5 = 0.9910

#4)negative exponetial function
#5)yes in positive and negative one and in zero

#Exercise 1.5

#1 x_n+1 = 1/2x_n + 4
#fixed points is 8

#2 x_n+1 = x_n² - 1
# formula resolvente (x² -x -1) x = 1.6181 e x = -0,6181

#3 x_n+1 = x_n² + 1
# formula resolvente (x² -x +1) nao tem raizes reais

#Exercise 1.6

def eq1():
    return  lambda x: x * x

def eq2():
    return  lambda x: x * x * x
def eq3():
    return  lambda x: 2 * x - 1

a = [0.8,0.9,1.2]
# K = 1000x0
x0 = .8
# x0 = [2,4,
display = simcx.Display()

simulator = FunctionIterator(eq3(), a )

vis = TimeSeries(simulator)

display.add_simulator(simulator)  #call step method
display.add_visual(vis)  # make a visual the new processed point

simcx.run()

