#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ischeme.lexer.core import Lexer
from ischeme.parser.core import Parser
from ischeme.rt.core import RT

if __name__ == '__main__':
    src = []
    with open("./scm_src/test1.scm") as f:
        src = [line.strip("\n") for line in f.readlines()]

    lexer = Lexer(src)
    #lexer.peek(20)
    #print(lexer.queue)
    parser = Parser(lexer)
    ast = parser.parse()
    #print(ast.children[0].children[-1].children[1].token.value)
    RT().eval(ast)
