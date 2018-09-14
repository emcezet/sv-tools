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

from SVClasses import *

logging.basicConfig(level=logging.DEBUG)


class UtSVClasses(unittest.TestCase):

    def test_source_text(self):
        desc1 = Description([1,2,3,4],{'1':1,'2':2},'stringgg')
        desc2 = Description({'1':1,'2':2})
        # descriptions = [desc1, desc2]
        # src_text = SourceText(descriptions)
        # src_text2 = SourceText(descriptions, timeunits_declaration='some time')
        # print(str(src_text))
        # print(str(src_text2))
        print(dir(desc1))
        print('blah')
        print(dir(type))
        print(type([1,2,3,4]))
        print(desc1.atr_dict)
        print(str(desc1))
if __name__ == '__main__':
    unittest.main()
