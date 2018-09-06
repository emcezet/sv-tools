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

    def __init__(self):
        self.sv_Files = []

    def debug_display(self):
        class_name = str(self.__class__.__name__)
        logging.debug(class_name + ': sv_ files : ' + str(self.sv_Files))
        logging.debug(class_name + ': Number of sv_ files : ' + str(len(self.sv_Files)))

    def discover_sv_files(self, proj_dir):
        for root, dirs, files in os.walk(proj_dir):
            for name in files:
                logging.debug('Discovered file: ' + name)
                path_to_file = os.path.join(root, name)
                logging.debug('Path to the file is : ' + path_to_file)
                split_name = name.rpartition('.')
                logging.debug('Last element of split tuple : ' + split_name[-1])
                if split_name[-1] == 'sv_':
                    logging.debug('sv_ File found.')
                    self.sv_Files.append(path_to_file)
            #for name in dirs:
            #    logging.debug('Discovered dirs: ' + name)
            #    logging.debug('Relative path to the dir is : ' + os.path.join(root, name))
