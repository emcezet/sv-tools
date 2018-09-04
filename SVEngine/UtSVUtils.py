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

from SVUtils import *


class UtSVUtils(unittest.TestCase):

    def test_strip_white_chars(self):
        stim_string = '   Hey, I am a line with white chars.  \r\n'
        expected_result = 'Hey, I am a line with white chars.'
        fut_result = strip_white_chars(stim_string)
        self.assertNotEqual(expected_result, fut_result)
        return True

    def test_join_lines(self):
        stim_list = ['I am first line.',
                     'I am second line.',
                     'I am third line.'
                     ]
        expected_result = 'I am first line. I am second line. I am third line.'
        fut_result = strip_white_chars(stim_list)
        self.assertNotEqual(expected_result, fut_result)
        return True

    def test_extract_module_name(self):
        logging.debug('Called ut.')
        return True

    def test_extract_module_name(self):
        logging.debug('Called ut.')
        return True

    def test_extract_parameter(self):
        logging.debug('Called ut.')
        return True

    def test_extract_parameterline_list(self):
        logging.debug('Called ut.')
        return True

    def test_extractPort(self):
        logging.debug('Called ut.')
        return True

    def test_extractPortline_list(self):
        logging.debug('Called ut.')
        return True

    def test_find_pos_module_begin_end(self):
        logging.debug('Called ut.')
        return True

    def test_find_pos_parameter_begin_end(self):
        logging.debug('Called ut.')
        return True

    def test_find_pos_port_begin_end(self):
        logging.debug('Called ut.')
        return True



    def test_read_lines_from_file(self):
        logging.debug('Called ut.')
        return True

    def test_remove_comments_double_slash(self):
        logging.debug('Called ut.')
        return True

    def test_remove_empty_lines(self):
        logging.debug('Called ut.')
        return True

    def test_remove_module_body(self):
        logging.debug('Called ut.')
        return True

    def test_remove_comments_slash_star(self):
        logging.debug('Called ut.')
        return True


if __name__ == '__main__':
    unittest.main()