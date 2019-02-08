"""
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden
@version 6feb2013
"""
import sys
sys.path.append('/home/ben/cs/cs344')
import time
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
import matplotlib.pyplot as plt
from numpy.core.numeric import arange
from numpy.ma.core import sin

from sine import LinearGrowthSin

class AbsVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return self.maximum / 2 - math.fabs(self.maximum / 2 - x)


if __name__ == '__main__':

    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30
    #initial = randrange(0, maximum)
    HCt = []
    SAt = []
    for initial in range(maximum):
        p = LinearGrowthSin(initial, maximum, delta=5)
        print('Initial                      x: ' + str(p.initial)
              + '\t\tvalue: ' + str(p.value(initial))
              )

        t = time.time()
        # Solve the problem using hill-climbing.
        hill_solution = hill_climbing(p)
        print('Hill-climbing solution       x: ' + str(hill_solution)
              + '\tvalue: ' + str(p.value(hill_solution))
              )
        tDelta = time.time() - t
        print("time to solve:\t" + str(tDelta))
        #HCt.append((initial,tDelta))
        HCt.append((initial, p.value(hill_solution)))
        # Solve the problem using simulated annealing.
        t = time.time()
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=maximum)
        )
        print('Simulated annealing solution x: ' + str(annealing_solution)
              + '\tvalue: ' + str(p.value(annealing_solution))
               )
        tDelta = time.time() - t
        SAt.append((initial, p.value(annealing_solution)))
        print("time to solve:\t" + str(tDelta))
    x = arange(0.0, maximum, 0.01)
    print(max(abs(x * sin(x))))
    print(min(abs(x * sin(x))))
    x, y = zip(*SAt)
    plt.scatter(*(x,y))
    plt.show()
