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

logging.basicConfig(level=logging.DEBUG)


def check_equal(list_a, list_b):
    return len(list_a) == len(list_b) and sorted(list_a) == sorted(list_b)


def test_routine_basic(test_text_sv = ''):
    eval_lexer.input(test_text_sv)
    _tokens_list = get_tokens(eval_lexer)
    logging.debug('\n_tokens_list = ' + str(_tokens_list))
    _values = [token.value for token in _tokens_list]
    return _tokens_list, _values


class UtEvalLexer(unittest.TestCase):

    def test_symbol(self):
        _test_text = 'A B C d g j j  g e e i'
        expected_list = _test_text.split()
        _tokens_list, _values = test_routine_basic(test_text_sv=_test_text)
        self.assertTrue(check_equal(expected_list, _values))
        self.assertEqual(11, count_tokens_type(_tokens_list, 'symbol'))

    def test_digit(self):
        _test_text = '0 1 2 3 4 5 6 7 8 9'
        expected_list = _test_text.split()
        _tokens_list, _values = test_routine_basic(test_text_sv=_test_text)
        self.assertTrue(check_equal(expected_list, _values))
        self.assertEqual(10, count_tokens_type(_tokens_list, 'digit'))


if __name__ == '__main__':
    unittest.main()
