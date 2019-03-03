'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
'''

from probability import BayesNet, elimination_ask

# Utility variables
T, F = True, False

cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
    ])

# 5.2.a
print('P(Cancer | test1 ^ test2)=', elimination_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
# The probability that t1 and t2 given C is the same as t1|C and t2|C
# a second positive test reduces the odds of a misdiagnosis
# P(C|t1,t2) = α <P(C)P(t1|C)P(t2|C), P(¬C)P(t1|¬C)P(t2|¬C)>
# = <(0.01*0.9)^2/(0.01*0.9^2+0.99*0.2^2), 0.99*0.2^2/(0.01*0.9^2+0.99*0.2^2)> = <0.83, 0.17>

# 5.2.b
print('P(Cancer | test1 ^ not test2)=', elimination_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())
# because it's much more likely you don't have cancer, a negative test weighs more heavily than a positive one
# P(C|t1,¬t2) = α <P(C)P(t1|C)P(¬t2|C), P(¬C)P(t1|¬C)P(t2|¬C)>
# = <0.01*0.9*0.1/(0.01*0.9*0.1+0.99*0.2*0.8), 0.99*0.2*0.8/(0.01*0.9*0.1+0.99*0.2*0.8)> = <0.994, 0.00565>

print('P(Cancer | test1)=', elimination_ask('Cancer', dict(Test1=T), cancer).show_approx())
# a negative test increases the odds of not having cancer by 3.7%
# two positive tests increases the confidence of having cancer by 12.6%
