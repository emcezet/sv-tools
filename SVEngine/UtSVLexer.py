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


def test_routine_basic(test_text_sv = ''):
    SVLexer.input(test_text_sv)
    _tokens_list = get_tokens(SVLexer)
    logging.debug('\n_tokens_list = ' + str(_tokens_list))
    _values = [token.value for token in _tokens_list]
    return _tokens_list, _values


class UtSVLexer(unittest.TestCase):

    def test_identifier(self):
        _test_text_sv = 'A1 s22imple identifier shall be    any SEQUENCe of letters dig123its dollar ' \
                        'signs$ und underscore_characters'
        expected_list = _test_text_sv.split()
        _tokens_list, _values = test_routine_basic(test_text_sv=_test_text_sv)
        self.assertTrue(check_tokens_type_all(_tokens_list, 'identifier'))
        self.assertTrue(check_equal(expected_list, _values))

    def test_comment_one_line(self):
        _test_text_sv = 'There are ids // This is a one line comment. We can use module keywords here. and or .'
        expected_result = []
        expected_result.extend('There are ids'.split())
        expected_result.append('// This is a one line comment. We can use module keywords here. and or .')
        _tokens_list,_values = test_routine_basic(test_text_sv=_test_text_sv)
        self.assertEqual(expected_result, _values)
        self.assertEqual(3,count_tokens_type(_tokens_list, 'identifier'))
        self.assertEqual(1, count_tokens_type(_tokens_list, 'comment_one_line'))

    # Do not modify this formatting.
    def test_comment_block(self):
        file = open('SVExamples/comment_block.sv','r')
        _test_text_sv = file.read()
        file.close()
        expected_result = []
        expected_result.extend('these are valid ids'.split())
        expected_result.append('\
/* A block comment started,\n\
we can use any keywords here like and or module\n\
and the comment may be very very very very very\n\
very very very very very very very very very very\n\
very very very very very very very very very very\n\
very very very very very very very very very very\n\
very very very very very very very very very very\n\
very very very very very very very very very very\n\
very very very very very very very very very very\n\
very very very very very very very very very very\n\
long*/')
        expected_result.extend('again these are valid ids\n'.split())
        expected_result.append('\
/* Another block comment started,to check for\n\
non greedy regexps expansion */')
        logging.debug(str(expected_result))
        _tokens_list, _values = test_routine_basic(test_text_sv=_test_text_sv)
        self.assertEqual(expected_result, _values)
        self.assertEqual(2, count_tokens_type(_tokens_list, 'comment_block'))
        self.assertEqual(9, count_tokens_type(_tokens_list, 'identifier'))

    def test_operators(self):
        _test_text_sv = 'Valid Ops are + - ! ~ & ~& | ~| ^ ~^ * / % == != === =?= !?= && || **\
                        < <= > >= >> << >>> <<< -> <-> ++ --'
        expected_result = _test_text_sv.split()
        _tokens_list, _values = test_routine_basic(test_text_sv=_test_text_sv)
        self.assertEqual(expected_result, _values)
        self.assertEqual(3, count_tokens_type(_tokens_list, 'identifier'))

    def test_delimiters(self):
        _test_text_sv = 'Valid Delimiters are ( ) [ ] { } , . ; ` \''
        expected_result = _test_text_sv.split()
        _tokens_list, _values = test_routine_basic(test_text_sv=_test_text_sv)
        self.assertEqual(expected_result, _values)
        self.assertEqual(3, count_tokens_type(_tokens_list, 'identifier'))

    def test_zdigit(self):
        _test_text_sv = 'z Z ?'
        expected_result = _test_text_sv.split()
        _tokens_list, _values = test_routine_basic(test_text_sv=_test_text_sv)
        logging.debug(str(_tokens_list))
        self.assertEqual(expected_result, _values)
        self.assertEqual(3, count_tokens_type(_tokens_list, 'zdigit'))

    def test_number(self):
        _test_text_sv = '0 1 2 3 4 5 6 7 8 9'
        expected_result = _test_text_sv.split()
        _tokens_list, _values = test_routine_basic(test_text_sv=_test_text_sv)
        self.assertEqual(expected_result, _values)
        #self.assertEqual(10, count_tokens_type(_tokens_list, 'digit'))


    # def test_literal_string(self):
    #     _test_text_sv = ' "This is a valid module string" '
    #     expected_result = 'This is a valid module string'
    #     _tokens_list, _values = test_routine_basic(test_text_sv=_test_text_sv)
    #     self.assertTrue(len(_values) == 1)
    #     self.assertEqual(_values[0], expected_result)


if __name__ == '__main__':
    unittest.main()
