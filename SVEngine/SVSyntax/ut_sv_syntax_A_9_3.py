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


import unittest
import logging
import ply.yacc as yacc
import ply.lex as lex
from SVLexer import *
from SVParser import *
from SVSyntax.sv_syntax_A_9_3 import *
#from SVSyntax.sv_syntax_A_9_4 import *
#from SVSyntax import *

logging.basicConfig(level=logging.DEBUG)



class ut_sv_syntax_A_9_3(unittest.TestCase):

    def test_p_module_identifier(self):
        logging.debug('test_p_module_identifier')
        yacc.yaccdebug = True
        sv_text = 'module name'
        SVLexer.input(sv_text)
        sv_parser.parse(sv_text)
        return False


if __name__ == '__main__':

    unittest.main()
