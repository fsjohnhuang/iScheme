#!/usr/bin/env python
# -*- coding: utf-8 -*-

def display(fmt, *exprs):
    if len(exprs):
        print(fmt.format(*exprs))
    else:
        print(fmt)

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

def sqrt(a):
    return a * a


exports = {"display": display,
           "+": add,
           "-": minus,
           "*": mul,
           "/": div,
           "**": pow,
           "sqrt": sqrt}
