# Zad 1
a) rodzeństwo
b) kuzyni
c) Dziadkowie tego samego wnuka ale każde od innej strony rodziców
d) Y toprzybrany rodzic a X to przybrane dziecko
e) pół rodzeństwo
f) szwagrami
g) rodzeństwo w trzech czwartych

# Zad 2

:- set_prolog_flag(occurs_check,error).
:- set_prolog_stack(global, limit(8000000)).
:- set_prolog_stack(local, limit(2000000)).


kobieta(X) :-
    osoba(X),
    \+ mezczyzna(X).


ojciec(X, Y) :-
    rodzic(X, Y),
    mezczyzna(X).


matka(X, Y) :-
    rodzic(X, Y),
    kobieta(X).


corka(X, Y) :-
    rodzic(Y, X),
    kobieta(X).

brat_rodzony(X, Y) :-
    mezczyzna(X),
    rodzic(Z, X),
    rodzic(Z, Y).
    

brat_przyrodni(X, Y) :-
    mezczyzna(X),
    rodzic(Z, X),
    rodzic(W, Y),
    \+ brat_rodzony(X, Y).

kuzyn(X, Y) :-
    rodzic(Z, X),
    rodzic(W, Y),
    brat_rodzony(Z, W).


dziadek_od_strony_ojca(X, Y) :-
    ojciec(X, Z),
    rodzic(Z, Y).


dziadek_od_strony_matki(X, Y) :-
    matka(X, Z),
    rodzic(Z, Y).


dziadek(X, Y) :-
    ojciec(X, Z),
    rodzic(Z, Y);
    matka(X, Z),
    rodzic(Z, Y).


babcia(X, Y) :-
    matka(X, Z),
    rodzic(Z, Y);
    ojciec(X, Z),
    rodzic(Z, Y).

wnuczka(X, Y) :-
    kobieta(X),
    babcia(Y,X).



przodek_do2pokolenia_wstecz(X, Y) :-
    rodzic(X, Z),
    rodzic(Z, Y).


przodek_do3pokolenia_wstecz(X, Y) :-
    rodzic(X, Z),
    przodek_do2pokolenia_wstecz(Z, Y).
