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
import re
#
# Definitions:
#    line - One line string read from file being parsed.
#    line_list - A list of lines


def read_lines_from_file(file_path):
    file_p = open(file_path, 'r')
    lines = file_p.readlines()
    if len(lines) == 0:
        raise ValueError(file_path+'File is empty.')
    return lines


def remove_comments_double_slash(line_list):
    if not type(line_list) is list:
        raise TypeError('List expected.')
    if len(line_list) == 0:
        raise ValueError('Non-empty list expected.')
    newline_list = []
    for line in line_list:
        if len(line) < 2:
            # Can not be a comment
            continue
        if line[0] == '/' and line[1] == '/':
            # Whole line is a comment
            continue
        newline_list.append(line.rstrip('//'))
    return newline_list


def join_lines(line_list):
    if not isinstance(line_list, list):
        raise TypeError('List expected.')
    lines = ''
    for line in line_list:
        lines = lines + line
    return lines


def remove_comments_slash_star(text):
    if not isinstance(text, str):
        raise TypeError('String expected.')
    logging.debug('Method:BeforeSub:remove_comments_slash_star:text =' + text)
    text = re.sub('/\*.*?\*/', '', text)
    logging.debug('Method:AfterSub:remove_comments_slash_star:text = ' + text)
    return text
# ''' This function takes parsed text as one string and returns positions of markers.
# There are markers for:
#     - module begin
#     - module end
#     - parameter list begin
#     - parameter list end
#     - ports list begin
#     - ports list end
#     '''


def get_pos_markers(text):
    if not isinstance(text, str):
        raise TypeError('String expected.')
    # It is assumed all comments were removed, therefore
    # word module will appear only once.
    pos_module_begin = text.find('module')
    pos_module_end = text.find('endmodule', pos_module_begin)
    pos_param_begin = text.find('#', pos_module_begin, pos_module_end)
    pos_param_end = text.find(')', pos_param_begin, pos_module_end)
    pos_port_begin = text.find('(', pos_param_end, pos_module_end)
    pos_port_end = text.find(');', pos_port_begin, pos_module_end)
    pos_markers = {'module_begin': pos_module_begin,
                   'module_end': pos_module_end,
                   'param_begin': pos_param_begin,
                   'param_end': pos_param_end,
                   'port_begin': pos_port_begin,
                   'port_end': pos_port_end
                   }
    return pos_markers


def get_module_name(pos_markers):
    return module_name


def get_params(pos_markers):
    return parameter_line_list


def get_ports(pos_markers):
    return port_direction, port_width, port_name


def remove_module_body(text, pos_markers):
    if not isinstance(text, str):
        raise TypeError('String expected.')
    text = text[:pos_port_end+2] + text[pos_module_end:]
    return text


def strip_white_chars(text):
    new_text = []
    for line in text:
        line = line.strip(' ')
        new_text.append(line)
    return new_text


def remove_lines_empty(line_list):
    if not type(line_list) is list:
        raise TypeError('List expected.')
    if len(line_list) == 0:
        raise ValueError('Non-empty list expected.')
    newline_list = []
    for line in line_list:
        if len(line) == 0:
            # Line is empty
            continue
        newline_list.append(line)
    return newline_list
