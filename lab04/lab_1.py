'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print(PC.show_approx())
#  p(Cavity|Catch) = .18/.34 = 0.529
PCatch = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PCatch.show_approx())

#T = heads, F = tails
M = JointProbDist(['Coin1', 'Coin2'])
M[T, T] = 0.25; M[T, F] = 0.25
M[F, T] = 0.25; M[F, F] = 0.25

MC = enumerate_joint_ask('Coin1', {'Coin2': T}, M)
print(MC.show_approx())