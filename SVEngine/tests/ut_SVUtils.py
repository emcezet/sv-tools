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
import inspect
import SVUtils as module

logging.basicConfig( level = logging.DEBUG )

def ut_extractModuleName():
    logging.debug( 'Called ut.' )
    return True

def ut_extractModuleName():
    logging.debug( 'Called ut.' )
    return True

def ut_extractParameter():
    logging.debug( 'Called ut.' )
    return True

def ut_extractParameterLineList():
    logging.debug( 'Called ut.' )
    return True

def ut_extractPort():
    logging.debug( 'Called ut.' )
    return True

def ut_extractPortLineList():
    logging.debug( 'Called ut.' )
    return True

def ut_findPosModuleBeginEnd():
    logging.debug( 'Called ut.' )
    return True

def ut_findPosParameterBeginEnd():
    logging.debug( 'Called ut.' )
    return True

def ut_findPosPortBeginEnd():
    logging.debug( 'Called ut.' )
    return True

def ut_joinLinesIntoText():
    logging.debug( 'Called ut.' )
    return True

def ut_readLinesFromFile():
    logging.debug( 'Called ut.' )
    return True

def ut_removeDoubleSlashComments():
    logging.debug( 'Called ut.' )
    return True

def ut_removeEmptyLines():
    logging.debug( 'Called ut.' )
    return True

def ut_removeModuleBody():
    logging.debug( 'Called ut.' )
    return True

def ut_removeSlashStarComments():
    logging.debug( 'Called ut.' )
    return True

def ut_stripLineListWhiteChars():
    logging.debug( 'Called ut.' )
    return True

def ut_stripLineWhiteChars():
    logging.debug( 'Called ut.' )
    return True

def scoreTests():
    functions = inspect.getmembers(module, inspect.isfunction)
    logging.debug( 'Functions found in module SVUtils' )
    testsPassed = 0
    testsFailed = 0
    numTests = len ( functions )
    testPass = False
    for function in functions:
        logging.debug( 'Running test for function:' + function[0] )
        try:
            exec( 'result = ' + 'ut_' + function[0] + '()' )
            logging.debug( 'Result is ' + str( result ))
            if( result ):
                testsPassed += 1
            else:
                testsFailed += 1
        except:
            logging.debug( 'Unit test was not implemented' )
            raise NotImplementedError( 'Unit test was not implemented for function.' + function[0] )
    if( testsPassed == numTests and testsFailed == 0 ):
        testPass = True
    else:
        testPass = False
    return testPass

testResult = scoreTests()
logging.debug( 'ut_SVUtils test result is : ' + str( testResult ))