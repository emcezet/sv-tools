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
# SVLexer.py
# IEEE Standard for SystemVerilog—Unified Hardware Design,Specification, and Verification Language
# Downloaded from : https://ieeexplore.ieee.org/document/8299595/, on 05.09.2018

import logging

import ply.lex
#from ply.lex import LexToken

# From 5.2 of IEEE(...):
# The types of lexical tokens in the language are as follows:
# White space
# Comment
# Operator
# Number
# String literal
# Identifier
# Keyword
# * Maintain this order in this file.

# Ignore tabs and spaces
t_ignore = ' \t'

# Comment
def t_comment_one_line(t):
    r'//.*'
    return t

def t_comment_multi_line(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Operator
# Operators
t_plus = r'\+'
t_minus = r'-'
t_times = r'\*'
t_divide = r'/'
t_mod = r'%'
t_op_or = r'\|'
t_op_and = r'&'
t_op_not = r'~'
t_op_xor = r'\^'
t_lshift = r'<<'
t_rshift = r'>>'
t_lor = r'\|\|'
t_land = r'&&'
t_lnot = r'!'
t_lt = r'<'
t_gt = r'>'
t_le = r'<='
t_ge = r'>='
t_eq = r'=='
t_ne = r'!='

operators = (
    'plus',
    'minus',
    'times',
    'divide',
    'mod',
    'op_or',
    'op_and',
    'op_not',
    'op_xor',
    'lshift',
    'rshift',
    'lor',
    'land',
    'lnot',
    'lt',
    'gt',
    'le',
    'ge',
    'eq',
    'ne'
)

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
t_tick = r'`'
t_apostrophe = r'\''

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
    'colon',
    'tick',
    'apostrophe'
)

# Assignment operators
t_equals = r'='

# Special char
t_pound = r'\#'

# Integer literal
t_iconst = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_fconst = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

# String literal
t_sconst = r'\"([^\\\n]|(\\.))*?\"'

# Character constant 'c' or L'c'
t_cconst = r'(L)?\'([^\\\n]|(\\.))*?\''

# Keywords
# From 5.6.2:
# All keywords are defined in lowercase only.
keywords = ( 'accept_on', 'alias', 'always', 'always_comb', 'always_ff', 'always_latch', 'and', 'assert',
'assign', 'assume', 'automatic', 'before', 'begin', 'bind', 'bins', 'binsof',
'bit', 'break', 'buf', 'bufif0', 'bufif1', 'byte', 'case', 'casex',
'casez', 'cell', 'chandle', 'checker', 'class', 'clocking', 'cmos', 'config',
'const', 'constraint', 'context', 'continue', 'cover', 'covergroup', 'coverpoint', 'cross',
'deassign', 'default', 'defparam', 'design', 'disable', 'dist', 'do', 'edge',
'else', 'end', 'endcase', 'endchecker', 'endclass', 'endclocking', 'endconfig', 'endfunction',
'endgenerate', 'endgroup', 'endinterface', 'endmodule', 'endpackage', 'endprimitive', 'endprogram', 'endproperty',
'endspecify', 'endsequence', 'endtable', 'endtask', 'enum', 'event', 'eventually', 'expect',
'export', 'extends', 'extern', 'final', 'first_match', 'for', 'force', 'foreach',
'forever', 'fork', 'forkjoin', 'function', 'generate', 'genvar', 'global', 'highz0',
'highz1', 'if', 'iff', 'ifnone', 'ignore_bins', 'illegal_bins', 'implements', 'implies',
'import', 'incdir', 'include', 'initial', 'inout', 'input', 'inside', 'instance',
'int', 'integer', 'interconnect', 'interface', 'intersect', 'join', 'join_any', 'join_none',
'large', 'let', 'liblist', 'library', 'local', 'localparam', 'logic', 'longint',
'macromodule', 'matches', 'medium', 'modport', 'module', 'nand', 'negedge', 'nettype',
'new', 'nexttime', 'nmos', 'nor', 'noshowcancelled', 'not', 'notif0', 'notif1',
'null', 'or', 'output', 'package', 'packed', 'parameter', 'pmos', 'posedge',
'primitive', 'priority', 'program', 'property', 'protected', 'pull0', 'pull1', 'pulldown',
'pullup', 'pulsestyle_ondetect', 'pulsestyle_onevent', 'pure', 'rand', 'randc', 'randcase', 'randsequence',
'rcmos', 'real', 'realtime', 'ref', 'reg', 'reject_on', 'release', 'repeat',
'restrict', 'return', 'rnmos', 'rpmos', 'rtran', 'rtranif0', 'rtranif1', 's_always',
's_eventually', 's_nexttime', 's_until', 's_until_with', 'scalared', 'sequence', 'shortint', 'shortreal',
'showcancelled', 'signed', 'small', 'soft', 'solve', 'specify', 'specparam', 'static',
'string', 'strong', 'strong0', 'strong1', 'struct', 'super', 'supply0', 'supply1',
'sync_accept_on', 'sync_reject_on', 'table', 'tagged', 'task', 'this', 'throughout', 'time',
'timeprecision', 'timeunit', 'tran', 'tranif0', 'tranif1', 'tri', 'tri0', 'tri1',
'triand', 'trior', 'trireg', 'type', 'typedef', 'union', 'unique', 'unique0',
'unsigned', 'until', 'until_with', 'untyped', 'use', 'uwire', 'var', 'vectored',
'virtual', 'void', 'wait', 'wait_order', 'wand', 'weak', 'weak0', 'weak1',
'while', 'wildcard', 'wire', 'with', 'within', 'wor', 'xnor', 'xor'
)


# Tokens
tokens = operators + keywords + delimiters + ('identifier', 'equals', 'pound', 'fconst',\
                                  'iconst', 'cconst', 'sconst')


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    return t

def t_identifier(t):
    #r'[A-Z][A-Z0-9]*'
    r'[A-Za-z_][\w_]*'
    if t.value in keywords:
        t.type = t.value
    return t


def t_error(t):
    print('Illegal character' + t.value[0])
    t.lexer.skip(1)
