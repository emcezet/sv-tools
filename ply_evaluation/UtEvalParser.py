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

#!/usr/bin/env python

import unittest
import logging

from ply.lex import *
from EvalLexer import *
from EvalParser import *

logging.basicConfig(level=logging.DEBUG)


class UtEvalParser(unittest.TestCase):

    def test_grammar0(self):
        logging.debug('\n-------------- TEST START --------------')
        grammar_num = 0
        eval_parser = EvalParser.main(grammar_num)
        _test_text_sv = 'G'
        eval_parser.parse(_test_text_sv, debug=1)
        return True

    def test_grammar1(self):
        logging.debug('\n-------------- TEST START --------------')
        grammar_num = 1
        eval_parser = EvalParser.main(grammar_num)
        _test_text_sv = '2'
        eval_parser.parse(_test_text_sv, debug=1)
        return True

    def test_grammar2(self):
        logging.debug('\n-------------- TEST START --------------')
        grammar_num = 2
        eval_parser = main(grammar_num)
        _test_text_sv = ' 1 2 3 9 8 5 5 '
        eval_parser.parse(_test_text_sv, debug=1)
        print(str(parsed_digits))
        print(str(all_digits))
        return True

    def test_grammar3(self):
        logging.debug('\n-------------- TEST START --------------')
        grammar_num = 3
        eval_parser = main(grammar_num)
        _test_text_sv = 'first 1 second 2 third'
        test_var = eval_parser.parse(_test_text_sv, debug=1)
        print(str(type(test_var)))
        print(str(test_var))
        print(str(rule_a))
        print(str(rule_a[0]))
        print(str(rule_b))
        return True

if __name__ == '__main__':
    unittest.main()
