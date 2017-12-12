#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..parser.node import *
from ..lexer.token import *
import special_forms, libs

class RT(object):
    def __init__(self):
        super(RT, self).__init__()
        self.special_forms = {}
        for name in dir(special_forms):
            if name.startswith("sf_"):
                self.special_forms["_".join(name.split("_")[1:])] = getattr(special_forms, name)

        self.globals = {}
        for name in dir(libs):
            if name.endswith("_exports"):
                exports = getattr(libs, name)
                for kv in exports.items():
                    self.globals[kv[0]] = kv[1]


    def eval(self, node):
        type_of_node = type(node)
        if type_of_node == ProgramNode:
            return self.eval_program(node)
        elif type_of_node == ExprNode:
            return self.eval_expr(node)
        elif type_of_node == PrimaryNode:
            return self.eval_primary(node)

    def eval_program(self, node):
        for child in node.children:
            self.eval(child)

    def eval_expr(self, node):
        identifier = node.children[0].token
        args = node.children[1:]
        special_form = self.special_forms.get(identifier.value, None)
        if special_form is None:
            expr = self.globals.get(identifier.value, None)
            if expr is not None:
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
            try:
                return self.globals[token.value]
            except Exception:
                raise Exception("identity {0} @{1}:{2} is not defined".format(token.value, token.linenu, token.colnu))

