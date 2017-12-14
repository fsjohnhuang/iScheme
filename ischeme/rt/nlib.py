#!/usr/bin/env python
# -*- coding: utf-8 -*-

def display(fmt, *exprs):
    if len(exprs):
        print(fmt.format(*exprs))
    elif isinstance(fmt, bool):
        print("#t" if fmt else "#f")
    else:
        print(fmt)

def expr_str(*xs):
    ret = [str(x) for x in xs]
    return "".join(ret)

def add(*ops):
    """
    (+)    ;=> 0
    (+ op) ;=> op
    (+ op1 op2 ...)
    """
    sum = 0
    for op in ops:
        sum += op
    return sum

def minus(a, *ops):
    """
    (- a)    ;=> a
    (- a op) ;=> a - op
    (- a op1 op2 ...)
    """
    for op in ops:
        a -= op
    return a

def mul(*ops):
    ret = 1
    for op in ops:
        ret *= op
    return ret

def div(a, *ops):
    for op in ops:
        a /= op
    return a

def pow(a, n):
    return a ** n

def mod(a, m):
    return a % m

def gt(a, b):
    return a > b

def lt(a, b):
    return a < b

def eq_question_mark(a, b):
    return a is b

def cons(a, xs):
    return [a] + xs

exports = {"display": display,
           "str": expr_str,
           "+": add,
           "-": minus,
           "*": mul,
           "/": div,
           "%": mod,
           "**": pow,
           "<": lt,
           ">": gt,
           "eq?": eq_question_mark,
           "cons": cons}
