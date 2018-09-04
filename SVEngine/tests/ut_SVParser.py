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
import argparse
import logging
import os
import sys ; sys.path.insert( 0, "../" )
from SVParser import SVParser
from SVSearcher import SVSearcher

parser = argparse.ArgumentParser( description = '''Python script for generating
         empty SystemVerilog modules.''' )
parser.add_argument( '-a', '--all', action='store_true', help='''Run tests with
       all SVExamples.''' )
parser.add_argument( '-v','--verbose', action='store_true',help='''Set verbosity
       level to debug.''' )
args = parser.parse_args()

if( args.verbose ):
    logging.basicConfig( level = logging.DEBUG )
else:
    logging.basicConfig( level = logging.INFO )

# Create object of class under test (CUT).
searcher = SVSearcher()
searcher.debugDisplay()
dirUnderTest = os.path.join( os.getcwd() , '../SVExamples/')
searcher.discoverSVFiles( dirUnderTest )

if( args.all ):
    logging.debug( 'Testing against all files in SVExamples' )
    for file in searcher.SVFiles:
        logging.debug( 'File : ' + str ( file ))
        # Create object of class under test (CUT).
        parser = SVParser()
        parser.parseFile( file )
        parser.debugDisplay()
else:
    logging.debug( 'Testing against first discovered file in SVExamples' )
    file = searcher.SVFiles[0]
    logging.debug( 'File : ' + str ( file ))
    # Create object of class under test (CUT).
    parser = SVParser()
    parser.parseFile( file )
    parser.debugDisplay()
