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

import os
import logging

class SVSearcher:

    def __init__( self ):
        self.SVFiles = []

    def debugDisplay( self ):
        className = str( self.__class__.__name__ )
        logging.debug( className + ': SV files : ' + str( self.SVFiles ))
        logging.debug( className + ': Number of SV files : ' + str( len( self.SVFiles )))

    def discoverSVFiles( self, projectDir ):
        if not os.path.isdir( projectDir ):
            raise Exception('Provided location is not a directory.')
        for root, dirs, files in os.walk( projectDir ):
            for name in files:
                logging.debug( 'Discovered file: ' + name )
                pathToFile = os.path.join( root, name )
                logging.debug( 'Path to the file is : ' + pathToFile )
                splitName = name.rpartition('.')
                logging.debug( 'Last element of split tuple : ' + splitName[-1] )
                if splitName[-1] == 'sv':
                    logging.debug( 'SV File found.')
                    self.SVFiles.append( pathToFile )
            #for name in dirs:
            #    logging.debug( 'Discovered dirs: ' + name )
            #    logging.debug( 'Relative path to the dir is : ' + os.path.join( root, name ))
