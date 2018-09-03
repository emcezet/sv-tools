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
import sys ; sys.path.insert(0,"../")
from SVParser import SVParser
from SVSearcher import SVSearcher

logging.basicConfig(level=logging.DEBUG)
# Create object of class under test (CUT).
searcher = SVSearcher()
searcher.debug_display()
dirUnderTest = os.path.join( os.getcwd() , '../SVExamples/')
searcher.discoverSVFiles( dirUnderTest )
exampleFile = searcher.SVFiles[0]
logging.debug( 'Example file : ' + str ( exampleFile ))
# Create object of class under test (CUT).
parser = SVParser( exampleFile )
parser.debug_display()

for file in searcher.SVFiles:
    logging.debug( 'File : ' + str ( file ))
    parser = SVParser( file )
    parser.debug_display()
    #input('Press ENTER')