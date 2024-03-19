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




kobieta(X):-
    \+kobieta(Mężczyzna),
    kobieta(Osoba).

Ojciec(X,Y):-
    Ojciec(Mężczyzna,
