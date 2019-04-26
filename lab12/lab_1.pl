killer(butch).
%butch is a killer is a fact
married(mia, marsellus).
married(marsellus, mia).
%mia is marred to marsellus and marsellus is married to mia
dead(zed).
%zed being dead is a fact
kills(marcellus, X):- givesFootrub(X, mia).
% a rule where marsellus kills X if X gives a footrub to mia
loves(mia, Y):- goodDancer(Y).
% a rule where mia loves, Y if Y is a goodDancer
eats(jules, Z):-
    nutritious(Z);
    tasty(Z).
% jules eats Z if Z is nutritious or tasty
