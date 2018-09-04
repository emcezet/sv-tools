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

#
# Definitions:
#    line - One line string read from file being parsed.
#    lineList - A list of lines

def stripLineWhiteChars( line ):
    if not isinstance( line, basestring ):
        raise TypeError( 'String expected.' )
    logging.debug( 'Method:stripLineWhiteChars:BeforeStrip:Line = ' + line )
    line = line.strip( ' ' )
    logging.debug( 'Method:stripLineWhiteChars:AfterStrip:Line = ' + line )
    return line

def stripLineListWhiteChars( lineList ):
    if not type( lineList ) is list:
        raise TypeError( 'List expected.' )
    if len( lineList ) == 0:
        raise ValueError( 'Non-empty list expected.' )
    strippedList = []
    for line in lineList:
        line = stripLineWhiteChars( line )
        strippedList.append( line )
    if len( strippedList ) == 0:
        raise ValueError( 'File does not contain valid SV Code.' )
    return strippedList

def joinLinesIntoText( lineList ):
    if not type( lineList ) is list:
        raise TypeError('List expected.')
    if len( lineList ) == 0:
        raise ValueError('Non-empty list expected.')
    joinLines = ''
    for line in lineList:
        joinLines = joinLines + line
    return joinLines

def findPosModuleBeginEnd( text ):
    if not isinstance( text, basestring ):
        raise TypeError('String expected.')
    # It is assumed all comments were removed, therefore
    # word module will appear only once.
    posModuleBegin = text.find('module')
    posModuleEnd = text.find('endmodule', posModuleBegin )
    return ( posModuleBegin, posModuleEnd )

def findPosParameterBeginEnd( text ):
    if not isinstance( text, basestring ):
        raise TypeError('String expected.')
    ( posModuleBegin, posModuleEnd ) = findPosModuleBeginEnd( text )
    posParameterBegin = text.find('#', posModuleBegin, posModuleEnd )
    posParameterEnd = text.find(')', posParameterBegin, posModuleEnd )
    return ( posParameterBegin, posParameterEnd )

def findPosPortBeginEnd( text ):
    if not isinstance( text, basestring ):
        raise TypeError('String expected.')
    ( posModuleBegin, posModuleEnd ) = findPosModuleBeginEnd( text )
    ( posParameterBegin, posParameterEnd ) = findPosParameterBeginEnd( text )
    posPortBegin = text.find('(', posParameterEnd, posModuleEnd )
    posPortEnd = text.find(');', posPortBegin, posModuleEnd )
    return ( posPortBegin, posPortEnd )

def extractModuleName():
    return moduleName

def extractParameter():
    return ( parameterName, parameterValue )

def extractParameterLineList ( text ):
    return parameterLineList

def extractPort( portLine ):
    return ( portDirection, portWidth, portName )

def extractPortLineList( text ):
    return portLineList

def removeModuleBody( text ):
    if not isinstance( text, basestring ):
        raise TypeError('String expected.')
    ( posModuleBegin , posModuleEnd ) = findPosModuleBeginEnd(text)
    ( posPortBegin , posPortEnd ) = findPosPortBeginEnd(text)
    text = text[:posPortEnd+2] + text[posModuleEnd:]
    return text

def removeSlashStarComments( text ):
    if not isinstance( text, basestring ):
        raise TypeError('String expected.')
    logging.debug( 'Method:BeforeSub:removeSlashStarComments:text = ' + text)
    text = re.sub('/\*.*?\*/', '', text)
    logging.debug( 'Method:AfterSub:removeSlashStarComments:text = ' + text)
    return text

def readLinesFromFile( filePath ):
    fileP = open( filePath, 'r')
    lines = fileP.readlines()
    if len( lines ) == 0:
        raise ValueError('File does not contain valid SV Code.')
    return lines

def removeEmptyLines( lineList ):
    if not type( lineList ) is list:
        raise TypeError('List expected.')
    if len( lineList ) == 0:
        raise ValueError('Non-empty list expected.')
    newLineList = []
    for line in lineList:
        if len( line ) == 0:
            # Line is empty
            continue
        newLineList.append( line )
    return newLineList

def removeDoubleSlashComments( lineList ):
    if not type( lineList ) is list:
        raise TypeError('List expected.')
    if len( lineList ) == 0:
        raise ValueError('Non-empty list expected.')
    newLineList = []
    for line in lineList:
        if len( line ) < 2:
            # Can not be a comment
            continue
        if line[0] == '/' and line[1] == '/':
            # Whole line is a comment
            continue
        newLineList.append( line.rstrip('//') )
    return newLineList
