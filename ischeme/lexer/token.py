#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

class Token(object):
    def __init__(self, linenu, colnu, value):
        super(Token, self).__init__()
        self.__linenu = linenu
        self.__colnu = colnu
        self.__value = value

    @property
    def linenu(self):
        return self.__linenu

    @property
    def colnu(self):
        return self.__colnu

    @property
    def value(self):
        return self.__value

class IntToken(Token):
    pattern = re.compile(r"\s*([+-]?[1-9][0-9]*)(?:\s+|\))")

    @classmethod
    def match(cls, linenu, pos, line):
        m = cls.pattern.match(line, pos)
        if m:
            return (cls(linenu, m.start(1), m.group(1)), m.end(1))

    def __init__(self, linenu, colnu, value):
        super(IntToken, self).__init__(linenu, colnu, value)

class FloatToken(Token):
    pattern = re.compile(r"\s*([+-]?[1-9][0-9]*\.[0-9]*)")

    @classmethod
    def match(cls, linenu, pos, line):
        m = cls.pattern.match(line, pos)
        if m:
            return (cls(linenu, m.start(1), m.group(1)), m.end(1))

    def __init__(self, linenu, colnu, value):
        super(FloatToken, self).__init__(linenu, colnu, value)


class BoolToken(Token):
    pattern = re.compile(r"\s*(#[tf])\b")

    @classmethod
    def match(cls, linenu, pos, line):
        m = cls.pattern.match(line, pos)
        if m:
            return (cls(linenu, m.start(1), m.group(1)), m.end(1))

    def __init__(self, linenu, colnu, value):
        super(BoolToken, self).__init__(linenu, colnu, value)

class CharToken(Token):
    pattern = re.compile(r"\s*(#\\.+?)\b")

    @classmethod
    def match(cls, linenu, pos, line):
        m = cls.pattern.match(line, pos)
        if m:
            return (cls(linenu, m.start(1), m.group(1)), m.end(1))

    def __init__(self, linenu, colnu, value):
        super(CharToken, self).__init__(linenu, colnu, value)

class StringToken(Token):
    pattern = re.compile(r'\s*"((?:\"|\n|\\|[^"])*)"')

    @classmethod
    def match(cls, linenu, pos, line):
        m = cls.pattern.match(line, pos)
        if m:
            return (cls(linenu, m.start(1), m.group(1)), m.end())

    def __init__(self, linenu, colnu, value):
        super(StringToken, self).__init__(linenu, colnu, value)

class SymbolToken(Token):
    pattern = re.compile(r"\s*'([a-zA-Z~!?@#$%^&*\-+=_./\<>][a-zA-Z~!?@#$%^&*\-+=_./\<>0-9]*)(?:\s+|\))")

    @classmethod
    def match(cls, linenu, pos, line):
        m = cls.pattern.match(line, pos)
        if m:
            return (cls(linenu, m.start(1), m.group(1)), m.end(1))

    def __init__(self, linenu, colnu, value):
        super(SymbolToken, self).__init__(linenu, colnu, value)

class IdentifierToken(Token):
    pattern = re.compile(r"\s*([a-zA-Z~!?@#$%^&*\-+=_./\<>][a-zA-Z~!?@#$%^&*\-+=_./\<>0-9]*)(?:\s+|\))")

    @classmethod
    def match(cls, linenu, pos, line):
        m = cls.pattern.match(line, pos)
        if m:
            return (cls(linenu, m.start(1), m.group(1)), m.end(1))

    def __init__(self, linenu, colnu, value):
        super(IdentifierToken, self).__init__(linenu, colnu, value)

class LeftBraceToken(Token):
    pattern = re.compile(r"\s*(\()")

    @classmethod
    def match(cls, linenu, pos, line):
        m = cls.pattern.match(line, pos)
        if m:
            return (cls(linenu, m.start(1), m.group(1)), m.end(1))

    def __init__(self, linenu, colnu, value):
        super(LeftBraceToken, self).__init__(linenu, colnu, value)

class RightBraceToken(Token):
    pattern = re.compile(r"\s*(\))")

    @classmethod
    def match(cls, linenu, pos, line):
        m = cls.pattern.match(line, pos)
        if m:
            return (cls(linenu, m.start(1), m.group(1)), m.end(1))

    def __init__(self, linenu, colnu, value):
        super(RightBraceToken, self).__init__(linenu, colnu, value)

class DottedPairToken(Token):
    pattern = re.compile(r"\s*( . )\S+")

    @classmethod
    def match(cls, linenu, pos, line):
        m = cls.pattern.match(line, pos)
        if m:
            return (cls(linenu, m.start(1), m.group(1)), m.end(1))

    def __init__(self, linenu, colnu, value):
        super(DottedPairToken, self).__init__(linenu, colnu, value)

class SingleCommentToken(Token):
    pattern = re.compile(r"\s*;(.*)")
    @classmethod
    def match(cls, linenu, pos, line):
        m = cls.pattern.match(line, pos)
        if m:
            return (cls(linenu, m.start(1), m.group(1)), m.end(1))

    def __init__(self, linenu, colnu, value):
        super(SingleCommentToken, self).__init__(linenu, colnu, value)
