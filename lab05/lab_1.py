'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

#5.1.a.i
print('P(Alarm | burglary ∧ ¬earthquake)=', elimination_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
'''This answer can be found by looking in the P(A|B ^ ¬E) entry in the table'''

#5.1.a.ii
print('P(John | burglary ∧ ¬earthquake)', elimination_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
'''This answer can be found by multiplying the probabilities of a burglary, not e, and summing J|a and a|b,-e over +-a.
The other half of the distribution is the sabe but with J notted'''

#5.1.a.iii
print('P(Burglary | alarm)', elimination_ask('Burglary', dict(Alarm=T), burglary).show_approx())
'''The answer can be found by summing the probabilities of B, e, and a|B,e over +-e. The distrobtion is found by notting B'''

#5.1.a.iv
print('P(Burglary | john ∧ mary)', elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
'''sum of  P(B) * P(e) * P(a|B,e) * P(J)'''
