% Question a.
% Question i.
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

% Question ii.
%true, because ron is a wizard is a fact
%undefined, because the atom 'witch' is undefined
%false, because hermione is not defined as a witch
%undefined procedure, because witch doesn't exist'
%true, because harry is a quidditchPlayer and quidditchPlayer hasBroom. Harry also hasWand and since X is a wizard if
%    he hasBroom and hasWand, harry is a wizard.
%Y = ron, prolog looks through the list of things defined as being a wizard and returns them.
%undefined, witch is not defined.

% Question b.
% yes, example:
bar(spam).
foo(eggs):- bar(spam).

% would return
% ?- foo(eggs).
% true.

% Question c.
% increased computational efficiency/ reduction of comp. complexity

% Question d.
% No. The syntax for assigning foo(bar) is the same as querying ?-foo(bar)
