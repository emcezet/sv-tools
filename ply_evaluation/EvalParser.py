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
import ply.yacc as yacc
import EvalLexer

# As defined in yacc.py
# p[0] === self.slice[n].value
# There is no type getter
# So use self.slice[n].type

parsed_digits = []
all_digits = []

rule_a = []
rule_b = []


class MadeUpClass:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return  str(self.data)

    def __repr__(self):
        return '__str__:MadeUpClass.data = ' + str(self)

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
        def p_A(p):
            '''A : B
                 | A B'''
            # To append B in both alts
            if len(p) == 2:
                p[0] = p[1]
                all_digits.append(p[1])
            elif len(p) == 3:
                p[0] = p[1]
                all_digits.append(p[1])
                p[0] = p[2]
                all_digits.append(p[2])
            else:
                pass

        def p_B(p):
            '''B : digit'''
            p[0] = p[1] # To propagate value
            parsed_digits.append(p[0])

        def p_C(p):
            '''C : symbol
                 | empty'''
            p[0] = p[1]

        # This is optional arg, but it becomes always optional, which is not that great.
        def p_empty(p):
            '''empty : '''
            pass
    elif grammar_num == 3:
        def p_A(p):
            ''' A : B
                    | A B'''
            # To append B in both alts
            if len(p) == 2:
                p[0] = p[1]
                rule_a.append(p[1])
            elif len(p) == 3:
                p[0] = p[1],p[2]
                #p[0] = p[2]
                #rule_a.append( (p[1],p[2]) )
        def p_B(p):
            ''' B : id
                    | number'''
            data = (p.slice[1].value, p.slice[1].type)
            made_up_object = MadeUpClass(data)
            print(made_up_object)
            #p[0] = (p[1],'B rule hit',p)
            p[0] = made_up_object
            print('This is a very special print, look at it!' + str(p.slice[0].value))
            print('This is a very special print, look at it!' + str(p.slice[1].value))
            print('This is a very special print, look at it!' + str(p.slice[1].type))
            rule_b.append(p[0])
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
    t = eval_parser.parsedebug(data, debug=debug)
    if eval_parser.error:
        return None
    return t
