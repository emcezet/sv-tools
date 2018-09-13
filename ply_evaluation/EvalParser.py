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


import ply.yacc as yacc
import EvalLexer

def p_error(p):
    if not p:
        print("SYNTAX ERROR AT EOF.")

def main(grammar_num):
    if grammar_num == 0:
        def p_A(t):
            '''A : B'''

        def p_B(t):
            '''B : symbol'''
    elif grammar_num == 1:
        def p_A(t):
            '''A : B'''

        def p_B(t):
            '''B : digit'''
    elif grammar_num == 2:
        def p_A(t):
            '''A : B'''

        def p_B(t):
            '''B : digit'''
    else:
        def p_A(t):
            '''A : B'''

        def p_B(t):
            '''B : symbol'''
    tokens = EvalLexer.tokens
    eval_parser = yacc.yacc()
    return eval_parser

def parse(data, debug=0):
    eval_parser.error = 0
    t = eval_parser.parse(data, debug=debug)
    if eval_parser.error:
        return None
    return t
