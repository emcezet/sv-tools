# MIT License
#
# Copyright (c) 2018 Michal Czyz
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#!/usr/bin/env python3

#
# EvalLexer.py
#

from ply.lex import *

t_ignore = ' \t\r\n\f'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    return t


def t_error(t):
    print('Illegal character' + t.value[0])
    t.lexer.skip(1)

def t_symbol(t):
    r'[a-zA-Z]'
    t.value = str(t.value)
    return t

def t_digit(t):
    r'[0-9]'
    t.value = int(t.value)
    return t

tokens = ('symbol', 'digit')

eval_lexer = lex()


def get_tokens(lexer):
    _tokens = []
    while True:
        _token = lexer.token()
        if not _token:
            break
        _tokens.append(_token)
    return _tokens


def count_tokens_type(_tokens, _type):
    _types = [token.type for token in _tokens]
    return _types.count(_type)


def check_tokens_type_all(_tokens, _type):
    num_tokens = count_tokens_type(_tokens, _type)
    return num_tokens == len(_tokens)
