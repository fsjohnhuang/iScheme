#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ischeme.lexer.core, ischeme.parser.core

if __name__ == '__main__':
    lexer = ischeme.lexer.core.Lexer(["(* 2 (- 1 3)"])
    #lexer.peek(20)
    parser = ischeme.parser.core.Parser(lexer)
    ast = parser.parse()
    print(ast[0].children)
