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

class SVObject(object):
    def __init__(self):
        pass

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return str(self)

    def __nonzero__(self):
        return False

class SourceText(SVObject):
    def __init__(self,  descriptions, timeunits_declaration = None):
        self.timeunits_declaration = timeunits_declaration
        self.descriptions = descriptions

    def __str__(self):
        return super().__str__() + ' ' + str(self.timeunits_declaration) + ' ' + str(self.descriptions)

    def __nonzero__(self):
        return True

class Description(SVObject):
    def __init__(self, *args):
        for i in range(len(args)):
            setattr(self,'atr_'+type(args[i]).__name__,args[i])

    def __str__(self):
        atr_list = dir(self)
        val_list = []
        for atr in atr_list:
            if 'atr_' in atr:
                val_list.append(getattr(self, atr))
        return super().__str__() + str(val_list)

    def __nonzero__(self):
        return True