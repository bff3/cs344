%a.
%i.
%directlyIn(olga, katarina).
%directlyIn(natasha, olga).
%directlyIn(irina, natasha).
%in(X, Y):- directlyIn(X, Y).
%in(X, Y):- directlyIn(X, Z),
%    in(Z, Y).
%ii.
%tran(eins,one).
%tran(zwei,two).
%tran(drei,three).
%tran(vier,four).
%tran(fuenf,five).
%tran(sechs,six).
%tran(sieben,seven).
%tran(acht,eight).
%tran(neun,nine).
%listtran([G|Tg], [E|Te]):- tran(G, E).
%listtran([Hg|Tg], [He|Te]):- listtran(Tg, Te).

%b.
%prolog has the :- operator
%which says if X:-Y,
%X is true if Y is true
%in other words: given Y is true, X is true
