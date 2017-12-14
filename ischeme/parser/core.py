#!tusr/bin/env python
# -*- coding: utf-8 -*-
from ..lexer.token import *
from node import *

# 将(E)BNF写成的规则转换为语法分析程序

# EBNF
# primary : INT | FLOAT | STRING | BOOL | CHAR | SYMBOL | IDENTIFIER | LIST_LITERAL | expr
# expr    : "(" { primary } ")"
# program : { expr }

class Parser(object):

    def __init__(self, lexer):
        super(Parser, self).__init__()
        self.lexer = lexer

    def strip_comment(self):
        while isinstance(self.lexer.peek(), SingleCommentToken):
            self.lexer.read()

    def primary(self):
        self.strip_comment()

        token = self.lexer.peek()
        type_of_token = type(token)
        if type_of_token in [ListLiteralToken,IntToken,FloatToken,StringToken,BoolToken,CharToken,SymbolToken,IdentifierToken]:
            return PrimaryNode(self.lexer.read())
        elif type_of_token == LeftBraceToken:
            return self.expr()
        else:
            raise SyntaxError("line:{0}, col:{1}, {2} is error".format(token.linenu, token.colnu, token.value))

    def expr(self):
        self.strip_comment()

        token = self.lexer.read()
        if isinstance(token, LeftBraceToken):
            children = []
            while not isinstance(self.lexer.peek(), RightBraceToken):
                children.append(self.primary())
            self.lexer.read()
            return ExprNode(children)
        else:
            raise SyntaxError("line:{0}, col:{1}, {2} is error".format(token.linenu, token.colnu, token.value))

    def program(self):
        nodes = []

        self.strip_comment()
        while self.lexer.peek():
            nodes.append(self.expr())
            self.strip_comment()

        return ProgramNode(nodes)

    def parse(self):
        return self.program()
