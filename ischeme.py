#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from ischeme.lexer.core import Lexer
from ischeme.parser.core import Parser
from ischeme.rt.core import RT

def main(file_path):
    with open(file_path) as f:
        src = [line.strip("\n") for line in f.readlines()]
    # prepend (load 'scm.core)
    src.insert(0, "(load \"/home/john/iScheme/ischeme/rt/scm/core.scm\")")

    lexer = Lexer(src)
    parser = Parser(lexer)
    RT().eval(parser.parse())

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main("/home/john/iScheme/scm_src/test1.scm")
