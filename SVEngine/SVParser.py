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

from SVModule import SVModule

class SVParser:

    def __init__( self, filePath ):
        if not os.path.isfile( filePath ):
            raise Exception( 'Provided location is not a file.' )
        fileP = open( filePath, 'r')
        lines = fileP.readlines()
        stripLines = []
        for line in lines:
            line = line.rstrip('\n')
            line = line.rstrip('\r')
            line = line.rstrip(' ')
            line = line.strip(' ')
            if len( line ) > 1 :
                if line[0] == '/':
                    if line[1] == '/':
                        # It is a comment
                        continue
            if len( line ) == 0 :
                # Line is empty
                continue
            stripLines.append( line )
        self.striplines = stripLines
        self.module = SVModule()
        self.interface = SVInterface()

    def debug_display( self ):
        print 'Lines : ' + str( self.striplines )
