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
import sys
import os.path
import json
import datetime

import self_test

def updatePersonalInfo(configFile, licenseText):
    configText = ''
    with open(configFile) as f:
        configText = json.load(f)
    today=str(datetime.datetime.now())
    licenseText.replace(':xxx',today,1)
    licenseText.replace(':xxx',str(configText['Author']),1)
    licenseText.replace(':xxx',str(configText['Company']),1)
    logging.debug(licenseText)
    return licenseText

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(description = '''Python script for generating
         empty SystemVerilog modules.''')
parser.add_argument('-i', '--interface', action='store_true', help='''Interface
       style connection.''')
parser.add_argument('-o', '--output',nargs='?', default='new_mod.sv',
       action='store', help='''Specify output file.''')
parser.add_argument('-t', '--template',nargs='?', default='new_mod.svt',
       action='store', help='''Specify template file.''')
parser.add_argument('-m', '--module',nargs='?', default='module_one',
       action='store', help='''Specify moudle name.''')
parser.add_argument('-v','--verbose', action='store_true',help='''Set verbosity
       level to debug.''')
args = parser.parse_args()

if ( args.verbose ):
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

newFile = args.output
if os.path.isfile( newFile ):
    raise Exception('The file '+ newFile + ' already exists here!')

if ( args.interface ):
    logging.debug('I will produce interface style.')
else:
    logging.debug('I will use legacy verilog style.')

try:
    licenseText = ''
    moduleText = ''
    with open('../templates/license.lic','r') as licenseFile:
        licenseText = licenseFile.read()
        logging.debug(licenseText)
        licenseText = updatePersonalInfo('../.svt_config',licenseText)
    if( args.interface ):
        with open('../templates/new_mod_i.svt','r') as templateFile:
            moduleText = templateFile.read()
    else:
        with open('../templates/new_mod.svt','r') as templateFile:
            moduleText = templateFile.read()
    logging.debug(licenseText)
    logging.debug(moduleText)
    with open( newFile, 'w' ) as f:
        f.write(licenseText)
        f.write(moduleText)
except:
    raise Exception('Wrong.')
