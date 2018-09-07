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
from SVLexer import *

logging.basicConfig(level=logging.DEBUG)

def check_equal(list_a, list_b):
    return len(list_a) == len(list_b) and sorted(list_a) == sorted(list_b)

def check_identifier_all(_tokens_list):
    for _token in _tokens_list:
        if _token.type != 'identifier':
            return False
    return True

class UtSVLexer(unittest.TestCase):

    def test_identifier(self):
        test_text_sv = '11A s22imple identifier shall be    any SEQUENCe of letters dig123its dollar signs$ und underscore_characters'
        expected_list = test_text_sv.split()
        SVLexer.input(test_text_sv)
        _tokens_list = get_tokens(SVLexer)
        logging.debug('\n_tokens_list = ' + str(_tokens_list))
        _values = [token.value for token in _tokens_list]
        self.assertTrue(check_identifier_all(_tokens_list))
        self.assertTrue(check_equal(expected_list, _values))

    def test_comment_one_line(self):
        test_text_sv = 'There are ids // This is a one line comment. We can use module keywords here. and or .'
        expected_result = '// This is a one line comment. We can use module keywords here. and or .'
        SVLexer.input(test_text_sv)
        _tokens_list = get_tokens(SVLexer)
        logging.debug('\n_tokens_list = ' + str(_tokens_list))
        _values = [token.value for token in _tokens_list]
        logging.debug('len(_values) = ' + str(len(_values)))
        self.assertEqual(expected_result, _values[-1])

    def test_comment_block(self):
        self.assertTrue(False)

    def test_unary_operator(self):
        test_text_sv = 'These are unary operators + - '
        expected_result = ''
        SVLexer.input(test_text_sv)
        _tokens_list = get_tokens(SVLexer)
        logging.debug('\n_tokens_list = ' + str(_tokens_list))
        _values = [token.value for token in _tokens_list]
        logging.debug('len(_values) = ' + str(len(_values)))
        self.assertEqual(expected_result, _values[-1])
        self.assertTrue(False)

    def test_newline(self):
        test_text_sv = 'these are ids \n these ids are on NEW line'
        expected_result = ''
        SVLexer.input(test_text_sv)
        _tokens_list = get_tokens(SVLexer)
        logging.debug('\n_tokens_list = ' + str(_tokens_list))
        _values = [token.value for token in _tokens_list]
        logging.debug('len(_values) = ' + str(len(_values)))
        self.assertTrue(False)

    def test_literal_string(self):
        test_text_sv = ' "This is a valid module string" '
        expected_result = 'This is a valid module string'
        SVLexer.input(test_text_sv)
        _tokens_list = get_tokens(SVLexer)
        logging.debug('\n_tokens_list = ' + str(_tokens_list))
        _values = [token.value for token in _tokens_list]
        logging.debug('len(_values) = ' + str(len(_values)))
        self.assertTrue(len(_values) == 1)
        self.assertEqual(_values[0],expected_result)

if __name__ == '__main__':

    unittest.main()
