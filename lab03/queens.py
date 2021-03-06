'''
Run the various CSP solvers on the nQueens problem.
These calls are mostly copied/adapted from AIMA Python.

@author: kvlinden
@version 14feb2013
'''

from csp import backtracking_search, NQueensCSP, min_conflicts, mrv, \
    forward_checking, AC3
from tools.aima.search import depth_first_graph_search
import logging
from time import time

# 1. Set up the problem.
n = 300
problem = NQueensCSP(n)

# 2. Solve the problem.
# There is a bug in the DFS code (even for 1-queens), so skip this one.
# solution = depth_first_graph_search(problem)

# t0 = time()
# solution = AC3(problem);
# t = time() - t0

t0 = time()
# solution = backtracking_search(problem, select_unassigned_variable=mrv, inference=forward_checking)
# solution = backtracking_search(problem, inference=forward_checking)
# solution = backtracking_search(problem, select_unassigned_variable=mrv)
solution = backtracking_search(problem)
t = time() - t0

# t0 = time()
# solution = min_conflicts(problem, max_steps=3000)
# t = time() - t0

# 3. Print the results.
print("Time to complete:\t" + str(t))
print
# Handle AC3 solutions (boolean values) first, they behave differently.
if type(solution) is bool:
    if solution and problem.goal_test(problem.infer_assignment()):
        print('AC3 Solution:')
    else:
        print('AC Failure:')
    print(problem.curr_domains)

# Handle other solutions next.
elif problem.goal_test(solution):
    print('Solution:')
    print(solution)
#    problem.display(problem.infer_assignment())
else:
    print('Failed - domains: ' + str(problem.curr_domains))
    problem.display(problem.infer_assignment())
