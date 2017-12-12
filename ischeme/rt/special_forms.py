#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..lexer.token import *
from ..parser.node import *

def sf_if(rt, cond, true_expr, false_expr=None):
    if rt.eval(cond):
        return rt.eval(true_expr)
    elif false_expr is not None:
        return rt.eval(false_expr)

def sf_begin(rt, expr, *exprs):
    ret = rt.eval(expr)
    for expr in exprs:
        ret = rt.eval(expr)

    return ret

def sf_or(rt, expr, *exprs):
    ret = False or rt.eval(expr)
    exprs = [expr for expr in exprs]
    while not ret and len(exprs):
        ret = ret or rt.eval(exprs.pop(0))

    return ret

def sf_and(rt, expr, *exprs):
    ret = True and rt.eval(expr)
    exprs = [expr for expr in exprs]
    while ret and len(exprs):
        ret = ret and rt.eval(exprs.pop(0))

    return ret

def sf_define(rt, l_val, r_val):
    if isinstance(l_val, PrimaryNode) and isinstance(l_val.token, IdentifierToken):
        rt.globals[l_val.token.value] = rt.eval(r_val)
