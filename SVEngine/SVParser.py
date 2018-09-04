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


import logging
import os
import sys
import re


from SVUtils import *
from SVModule import *
from SVInterface import *


class SVParser:

    def __init__(self):
        self.text = ''
        self.module = SVModule()
        self.interface = SVInterface()

    def debug_display(self):
        class_name = str(self.__class__.__name__)
        logging.debug(class_name + ': Lines : ' + str(self.join_lines))
        self.module.debug_display()
        self.interface.debug_display()

    def parse_file(self, file_path):
        lines_raw = read_lines_from_file(file_path)
        lines_no_empty = remove_lines_empty(lines_raw)
        lines_no_comment_slash = remove_comments_double_slash(lines_no_empty)
        lines_join = join_lines(lines_no_comment_slash)
        text_no_comment = remove_comments_slash_star(lines_join)
        text_no_module_body = remove_module_body(text_no_comment)
        self.text = text_no_module_body
        self.module = SVModule()
        self.interface = SVInterface()
