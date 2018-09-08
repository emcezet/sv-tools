# MIT License
# 
# Copyright (c) 2018 Michał Czyż
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


import unittest
import logging

from SVLexer import *

logging.basicConfig(level=logging.DEBUG)




class UtSVUtils(unittest.TestCase):

    def test_comment_one_line(self):
        logging.debug('Start : test_comment_one_line.')
        text_test_sv = '`define TOP 5 module module_name#(parameter = 8.5)(input clk); some text endmodule'
        logging.debug('text_test_sv = ' + text_test_sv)
        logging.debug('Create object lexer.')
        lexer_sv = ply.lex.lex()
        lexer_sv.input(text_test_sv)
        logging.debug('self.lexdata = ' + str(lexer_sv.lexdata))
        logging.debug('self.lexpos = ' + str(lexer_sv.lexpos))
        logging.debug('self.lextokens = ' + str(lexer_sv.lextokens))
        logging.debug('self.lexstateinfo = ' + str(lexer_sv.lexstateinfo))
        logging.debug('---')
        token = lexer_sv.token()
        while token is not None:
            logging.debug('token = ' + str(token))
            #logging.debug('self.lexdata = ' + str(lexer_sv.lexdata))
            #logging.debug('self.lexpos = ' + str(lexer_sv.lexpos))
            #logging.debug('self.lexstateinfo = ' + str(lexer_sv.lexstateinfo))
            #logging.debug('---')
            token = lexer_sv.token()

        result = False
        return result


if __name__ == '__main__':

    unittest.main()



bparser = yacc.yacc()


def parse(data, debug=0):
    bparser.error = 0
    p = bparser.parse(data, debug=debug)
    if bparser.error:
        return None
    return p