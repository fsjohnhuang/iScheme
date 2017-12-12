#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ASTree(object):
    def __init__(self):
        super(ASTree, self).__init__()
        self.children = []

    def get_child(self, index):
        return self.children[index]

class ASTLeaf(ASTree):
    def __init__(self, token):
        super(ASTLeaf, self).__init__()
        self.token = token

class ASTList(ASTree):
    def __init__(self, children):
        super(ASTList, self).__init__()
        self.children = children

class PrimaryNode(ASTLeaf):
    def __init__(self, token):
        super(PrimaryNode, self).__init__(token)

class ExprNode(ASTList):
    def __init__(self, children):
        super(ExprNode, self).__init__(children)

class ProgramNode(ASTList):
    def __init__(self, children):
        super(ProgramNode, self).__init__(children)

class LambdaNode(ASTLeaf):
    def __init__(self, lexical_scope, param_list, token):
        super(LambdaNode, self).__init__(token)
        self.param_list = param_list
        self.lexical_scope = lexical_scope
