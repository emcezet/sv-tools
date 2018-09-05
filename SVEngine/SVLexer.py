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

import logging

import ply.lex
from ply.lex import LexToken

# Keywords
keywords = (
    'MODULE', 'ENDMODULE', 'PARAMETER', 'INPUT'
)
# Map lowercase to uppercase
reserved_map = {}
for r in keywords:
    reserved_map[r.lower()] = r

# Delimiters
t_lparen = r'\('
t_rparen = r'\)'
t_lbracket = r'\['
t_rbracket = r'\]'
t_lbrace = r'\{'
t_rbrace = r'\}'
t_comma = r','
t_period = r'\.'
t_semi = r';'
t_colon = r':'

delimiters = (
    'lparen',
    'rparen',
    'lbracket',
    'rbracket',
    'lbrace',
    'rbrace',
    'comma',
    'period',
    'semi',
    'colon'
)

# Assignment operators
t_equals = r'='

# Special char
t_pound = r'\#'

# Ignore tabs
t_ignore = '\t'

# Tokens
tokens = keywords + delimiters + ('identifier', 'equals', 'pound')


def t_comment_one_line(t):
    r'//.*'
    return t


def t_comment_multi_line(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')



def t_id(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value, "identifier")
    return t


def t_newline(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)
