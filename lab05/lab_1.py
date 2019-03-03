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

# 5.1.a.i
print('P(Alarm | burglary ∧ ¬earthquake)=', elimination_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
'''This answer can be found by looking in the P(A|B ^ ¬E) entry in the table'''

# 5.1.a.ii
print('P(John | burglary ∧ ¬earthquake)', elimination_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
'''This answer can be found by multiplying the probabilities that John calls given an alarm and that an alarm sounds
given a burglary and not an earthquake or that John calls if an alarm does not sound and that an alarm does not
sound given a burglary and not an earthquake, and the probabilities of a burglary and not an earthquake.
The other half of the distribution is the same but with not J'''

# 5.1.a.iii
print('P(Burglary | alarm)', elimination_ask('Burglary', dict(Alarm=T), burglary).show_approx())
'''The answer can be found by multiplying the probabilities of an alarm sounding given a burglary or earthquake with the
probabilities of a burglary and an earthquake or a burglary and not an earthquake. The distribution is found
by using not B'''

# 5.1.a.iv
print('P(Burglary | john ∧ mary)', elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
'''the answer would be αP(B)P(e)∑_a P(j|a)P(m|a)P(a|B,e).
We need the probability of j|a and m|a. For those we need a|B,e. For that we need B and e. Because
a is not guaranteed so we need to include the cases where John and Mary call even if the alarm doesn't sound'''
