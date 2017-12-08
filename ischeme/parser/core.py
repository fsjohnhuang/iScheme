#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..lexer.token import *
from node import *

# 解释器组合子类型的库
# 将(E)BNF写成的规则转换为语法分析程序

# EBNF
# primary : "(" expr ")" | INT | FLOAT | STRING | BOOL | CHAR | SYMBOL | IDENTIFIER
# expr    : IDENTIFIER { primary }
# program : { primary }


class Parser(object):

    def __init__(self, lexer):
        super(Parser, self).__init__()
        self.lexer = lexer

    def raise_syxtaxerror(self, token):
        raise SyntaxError("line:{0}, col:{1}, {2} is error".format(token.linenu, token.colnu, token.value))

    def strip_comment(self):
        while isinstance(self.lexer.peek(), SingleCommentToken):
            self.lexer.read()

    def expr(self):
        self.strip_comment()

        token = self.lexer.read()
        print(token)
        print(token.value)
        if not isinstance(token, IdentifierToken):
            self.raise_syxtaxerror(token)
        else:
            identifier = token
            token = self.lexer.peek()
            nodes = []
            while token is not None and token.value != ")":
                nodes.append(self.primary())
                token = self.lexer.peek()

            self.lexer.read()

            return ExprNode([PrimaryNode(identifier)] + nodes)

    def primary(self):
        self.strip_comment()

        token = self.lexer.read()
        print(token)
        print(token.value)
        type_of_token = type(token)
        if type_of_token in [IntToken,FloatToken,StringToken,BoolToken,CharToken,SymbolToken,IdentifierToken]:
            return PrimaryNode(token)
        elif type_of_token == LeftBraceToken:
            return self.expr()
        else:
            raise SyntaxError("None")

    def program(self):
        nodes = []

        self.strip_comment()
        while self.lexer.peek():
            nodes.append(self.primary())

        return nodes

    def parse(self):
        return self.program()
