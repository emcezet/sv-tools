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

def checkRepoDirStruct():
    logging.info('Starting self test.')
    os.chdir('..')
    cwd = os.getcwd()
    splitCwd = cwd.split('/')
    if not (splitCwd[-1] == 'sv-tools'):
        logging.fatal('Repo name should be sv-tools')
        raise Exception('Wrong repo name!')
    dirs = os.listdir(cwd)
    logging.debug("Files" + str(dirs))
    expectedDirs=['scripts','templates']
    for expectedDir in expectedDirs:
        if not any ( d == expectedDir for d in dirs):
            logging.fatal('Missed dir is'+ str(d))
            raise Exception('Missing dir!')
    logging.info('Directory structure is ok.')
    os.chdir('scripts')
    return True

def discoverTemplates():
    if not checkRepoDirStruct():
        raise Exception('Directory structure was corrupted!')
    templates=[]
    os.chdir('../templates/')
    cwd = os.getcwd()
    for file in os.listdir(cwd):
        if file.endswith(".svt"):
            logging.debug('Template: ' + str(file) +' was found!' )
            templates.append(file)
    logging.debug('Templates list:' + str(templates) )
    if not len(templates):
        logging.fatal('No templates. There should be at least two.')
        raise Exception('No templates found.')
    os.chdir('../scripts/')
    return templates

def checkDefaultTemplate():
    templates = discoverTemplates()
    expectedTemplates=['new_mod.svt','new_mod_i.svt']
    for expectedTemplate in expectedTemplates:
        if not any ( t == expectedTemplate for t in templates):
            logging.fatal('Missing template is'+ str(t))
            raise Exception('Missing template!')
    logging.info('Templates are there.')
    return True

