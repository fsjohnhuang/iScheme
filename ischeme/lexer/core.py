#!/usr/bin/env python
# -*- coding: utf-8 -*-
from token import *

class Lexer(object):
    token_types = [FloatToken, IntToken, BoolToken, CharToken, StringToken, SymbolToken, ListLiteralToken, IdentifierToken, LeftBraceToken, RightBraceToken, DottedPairToken, SingleCommentToken]

    def __init__(self, lines):
        super(Lexer, self).__init__()
        self.index = 0
        self.lines = lines
        self.queue = []

    def read(self):
        if self.fill_queue(0):
            return self.queue.pop(0)

    def peek(self, index=0):
        if self.fill_queue(index):
            return self.queue[index]

    def fill_queue(self, idx):
        while idx >= len(self.queue):
            if self.has_more:
                self.readline()
            else:
                return False
        return True

    @property
    def has_more(self):
        return self.index < len(self.lines)

    def readline(self):
        line = self.lines[self.index]
        pos = 0
        end_pos = len(line)
        while pos < end_pos:
            found = None
            for token_type in self.token_types:
                found = token_type.match(self.index, pos, line)
                if found:
                    self.queue.append(found[0])
                    pos = found[1]
                    break
            if found is None:
                pos += 1
        self.index += 1
