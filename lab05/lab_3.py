'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
'''

from probability import BayesNet, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
happy = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])

# 5.3.a.i
print('P(Raise | Sunny)=', elimination_ask('Raise', dict(Sunny=T), happy).show_approx())
# R and S are independent of each other, so the distribution is <0.01, 0.99> from the table

# 5.3.a.ii
print('P(Raise | happy ^ sunny)=', elimination_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())
# because its always sunny we dont have to sum over sunny
# = α P(R)P(h|R,s)P(s)
# = α <P(s)P(R)P(h|R,s), P(s)P(¬R)P(h|¬R, s)>
# = <0.01*0.7*1/(0.01*0.7*1+0.99*0.7*0.7), 0.99*0.7*0.7/(0.01*0.7*1+0.99*0.7*0.7)>

# 5.b.i
print('P(Raise | happy)=', elimination_ask('Raise', dict(Happy=T), happy).show_approx())
# in this case it could be sunny or not sunny which could effect the happiness
# = α ∑_s P(R)P(h|R,s)P(s)
# = α < P(R)P(h|R,s)P(s) + P(R)P(h|R,¬s)P(¬s), P(¬R)P(h|¬R,s)P(s) + P(¬R)P(h|¬R,¬s)P(¬s)>

#5.b.ii
print('P(Raise | happy ^ ¬sunny)=', elimination_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())
# pretty similar to 5.3.a.ii but not sunny instead of sunny
# = α P(R)P(h|R,¬s)P(¬s)
# = α <P(R)P(h|R,¬s)P(¬s), <P(¬R)P(h|¬R,¬s)P(¬s)>
# = <0.01*0.9/(0.01*0.9+0.99*0.1), 0.99*0.1/(0.01*0.9+0.99*0.1)> = <0.0833, 0.917>
