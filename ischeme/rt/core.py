#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from ..parser.node import *
from ..parser.core import Parser
from ..lexer.token import *
from ..lexer.core import Lexer
import special_forms, nlib

class RT(object):
    def __init__(self):
        super(RT, self).__init__()
        self.path = os.getcwd()

        self.special_forms = {}
        for name in dir(special_forms):
            if name.startswith("sf_"):
                self.special_forms["_".join(name.split("_")[1:])] = getattr(special_forms, name)
        for kvs in special_forms.alias.items():
            self.special_forms[kvs[0]] = kvs[1]

        self.globals = {"'()": []}
        exports = nlib.exports
        for kv in exports.items():
            self.globals[kv[0]] = kv[1]

        self.locals = []

    def resolve(self, node):
        token = node
        try:
            idx = range(len(self.locals))
            idx.reverse()
            for i in idx:
                if self.locals[i].has_key(token.value):
                    return self.locals[i][token.value]
            return self.globals[token.value]
        except Exception:
            raise Exception("identity {0} @{1}:{2} is not defined".format(token.value, token.linenu, token.colnu))

    def eval(self, node):
        type_of_node = type(node)
        if type_of_node == ProgramNode:
            return self.eval_program(node)
        elif type_of_node == ExprNode:
            return self.eval_expr(node)
        elif type_of_node == PrimaryNode:
            return self.eval_primary(node)

    def eval_program(self, node):
        ret = None
        for child in node.children:
            ret = self.eval(child)

        return ret

    def eval_expr(self, node):
        identifier = node.children[0].token
        args = node.children[1:]
        special_form = self.special_forms.get(identifier.value, None)
        if special_form is None:
            expr = self.resolve(identifier)
            if isinstance(expr, LambdaNode):
                return self.eval_lambda(expr, [self.eval(arg) for arg in args])
            elif expr is not None:
                return expr(*[self.eval(arg) for arg in args])
        else:
            args = [self] + args
            return special_form(*args)

    def eval_primary(self, node):
        token = node.token
        type_of_token = type(token)
        if type_of_token == IntToken:
            return int(token.value)
        elif type_of_token == FloatToken:
            return float(token.value)
        elif type_of_token == BoolToken:
            return token.value[-1] == "t"
        elif type_of_token == StringToken:
            return token.value
        elif type_of_token == IdentifierToken:
            return self.resolve(token)
        elif type_of_token == SymbolToken:
            return token.value.replace("'","")
        elif type_of_token == ListLiteralToken:
            if not self.globals.has_key(token.value):
                xs = map(lambda x: x if x != "(" else "(list ", token.value[1:])
                code = "".join(xs)
                self.globals[token.value] = self.eval(Parser(Lexer(["(load \"/home/john/iScheme/ischeme/rt/scm/core.scm\")", code])).parse())
            return self.globals[token.value]

    def eval_lambda(self, node, args):
        lexical_scope = node.lexical_scope
        param_list = node.param_list
        for child in param_list.children:
            lexical_scope[child.token.value] = args.pop(0)
        self.locals.append(lexical_scope)
        ret = self.eval(node.token)
        self.locals.pop(-1)

        return ret
