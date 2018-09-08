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
# Notation 'From number.number' refers to section of this standard.

import logging
from ply.lex import *

# From 5.2:
# The types of lexical tokens in the language are as follows:
# White space
# Comment
# Operator
# Number
# String literal
# Identifier
# Keyword
# * Maintain this order in this file.

# From 5.3
# White space shall contain the characters for spaces, tabs, newlines, and formfeeds. These characters shall be
# ignored except when they serve to separate other lexical tokens.
#
# token_ignore := space tab return_carriage new_line form_feed
t_ignore = ' \t\r\n\f'


# From 5.4
# A one-line comment shall start with the two characters // and end with a newline character.
def t_comment_one_line(t):
    r'//.*'
    return t


# From 5.4
# A block comment shall start with /* and end with */.
def t_comment_block(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# From 5.5
# Operators are single-, double-, or triple-character sequences and are used in expressions.
# Defined in order in which they appear in standard.
# b is for bitwise, l is for logical
# Unary operators
t_plus = r'\+'
t_minus = r'-'
t_lnot = r'!'
t_bnot = r'~'
t_band = r'&'
t_bnand = r'~&'
t_bor = r'\|'
t_bnor = r'~\|'
t_bxor = r'\^'
t_bnxor = r'~\^'
t_bxnor = r'\^~'
# Binary operators
t_times = r'\*'
t_divide = r'/'
t_mod = r'%'
t_eq = r'=='
t_ne = r'!='
t_seq = r'===' # Strict equal = seq
t_nseq = r'!==' # Not strict equal = nseq
t_weq = r'=\?=' # Wildcard equality operator
t_nweg = r'!\?=' # Wildcard not equality operator
t_land = r'&&'
t_lor = r'\|\|'
t_pow = r'\*\*'
t_lt = r'<'
t_nbass = r'<=' # Non-blocking assignment
t_gt = r'>'
t_ge = r'>='
t_rshift = r'>>'
t_lshift = r'<<'
t_arshift = r'>>>'
t_alshift = r'<<<'
t_impl = r'->'
t_equiv = r'<->'
# Inc or dec ops
t_inc = r'\+\+'
t_dec = r'--'

operators = (
    'plus',
    'minus',
    'lnot',
    'bnot',
    'band',
    'bnand',
    'bor',
    'bnor',
    'bxor',
    'bnxor',
    'bxnor',
    'times',
    'divide',
    'mod',
    'eq',
    'ne',
    'seq',
    'nseq',
    'weq',
    'nweg',
    'land',
    'lor',
    'pow',
    'lt',
    'nbass',
    'gt',
    'ge',
    'rshift',
    'lshift',
    'arshift',
    'alshift',
    'impl',
    'equiv',
    'inc',
    'dec'
    )

# From 5.6
# An identifier is used to give an object a unique name so it can be referenced. An identifier is either a simple
# identifier or an escaped identifier (see 5.6.1). A simple identifier shall be any sequence of letters, digits,
# dollar signs ($), and underscore characters (_).
# Warning : first implementation will only accept simple identifiers.
def t_identifier(t):
    r'[A-Za-z_][A-Za-z0-9_$]*'
    if t.value in keywords:
        t.type = t.value
    return t


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

# Special char
t_pound = r'\#'

# Integer literal
t_iconst = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_fconst = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

# String literal
# From A.8.8:
# string_literal ::= " { Any_ASCII_Characters } "
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


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    return t


def t_error(t):
    print('Illegal character' + t.value[0])
    t.lexer.skip(1)


# Tokens
tokens = operators + keywords + delimiters + ('identifier', 'equals', 'pound', 'comment_one_line',
          'comment_block') +  ( 'iconst', 'fconst', 'sconst', 'cconst')


SVLexer = lex()

# Let's add some utility to lex. Method runmain prints tokens via:
# while True:
#        tok = _token()
#        if not tok:
#            break
#        sys.stdout.write('(%s,%r,%d,%d)\n' % (tok.type, tok.value, tok.lineno, tok.lexpos))
# I want to put these tokens in a list for testing purposes.


def get_tokens(lexer):
    _tokens = []
    while True:
        _token = lexer.token()
        if not _token:
            break
        _tokens.append(_token)
    return _tokens


def count_tokens_type(_tokens, _type):
    _values = [token.value for token in _tokens]
    return _values.count(_type)


def check_tokens_type_all(_tokens, _type):
    num_tokens = count_tokens_type(_tokens, _type)
    return num_tokens == len(_tokens)
