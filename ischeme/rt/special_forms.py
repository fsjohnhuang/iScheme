#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..lexer.token import *
from ..parser.node import *
from ..lexer.core import Lexer
from ..parser.core import Parser
import core

def sf_load(rt, expr):
    with open(rt.eval(expr)) as f:
        src = [line.strip("\n") for line in f.readlines()]
    lexer = Lexer(src)
    parser = Parser(lexer)
    _rt = core.RT()
    _rt.eval(parser.parse())
    rt.locals.insert(0, _rt.globals)

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

def sf_not(rt, expr):
    return not rt.eval(expr)

def sf_define(rt, l_val, r_val):
    if isinstance(l_val, PrimaryNode) and isinstance(l_val.token, IdentifierToken):
        rt.globals[l_val.token.value] = rt.eval(r_val)
    else:
        raise SyntaxError("There is invalid identity name after define special form.")

def sf_let(rt, local_vars, expr, *exprs):
    kvs = {}
    if isinstance(local_vars, ExprNode):
        for child in local_vars.children:
            if isinstance(child, ExprNode) and len(child.children) == 2:
                l_val = child.children[0]
                r_val = child.children[1]
                if isinstance(l_val, PrimaryNode):
                    kvs[l_val.token.value] = rt.eval(r_val)
                else:
                    raise SyntaxError("special form 'let'")
            else:
                raise SyntaxError("special form 'let'")
        rt.locals.append(kvs)
        ret = None
        ret = rt.eval(expr)
        for expr in exprs:
            ret = rt.eval(expr)
        rt.locals.pop(-1)
        return ret
    else:
        raise SyntaxError("special form 'let'")

def sf_let_asterisk(rt, local_vars, expr, *exprs):
    kvs = {}
    rt.locals.append(kvs)
    try:
        if isinstance(local_vars, ExprNode):
            for child in local_vars.children:
                if isinstance(child, ExprNode) and len(child.children) == 2:
                    l_val = child.children[0]
                    r_val = child.children[1]
                    if isinstance(l_val, PrimaryNode):
                        kvs[l_val.token.value] = rt.eval(r_val)
                    else:
                        raise SyntaxError("special form 'let'")
                else:
                    raise SyntaxError("special form 'let'")
            rt.eval(expr)
            for expr in exprs:
                rt.eval(expr)
        else:
            raise SyntaxError("special form 'let'")
    finally:
        rt.locals.pop(-1)

def sf_lambda(rt, param_list, expr):
    params = map(lambda child: child.token.value, param_list.children)
    id_nodes = __find_refs(expr, params)
    kvs = {}
    for id_node in id_nodes:
        try:
            kvs[id_node.token.value] = rt.eval(id_node)
        except Exception, e:
            pass

    return LambdaNode(kvs, param_list, expr)

def __find_refs(expr, excludes):
    if isinstance(expr, ExprNode):
        refs = []
        for child in expr.children[1:]:
            refs += __find_refs(child, excludes)
        return refs
    elif isinstance(expr, PrimaryNode) and isinstance(expr.token, IdentifierToken) and expr.token.value not in excludes:
        return [expr]
    else:
        return []

alias = {"let*": sf_let_asterisk}
