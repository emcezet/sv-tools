# MIT License
# 
# Copyright (c) 2018 Michał Czyż
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


#!/usr/bin/env python3

# All commented BNF Forms should be unchanged copies of Annex A of IEEE Standard.

# A.1.2 SystemVerilog source text
# source_text ::= [ timeunits_declaration ] { description }
def p_source_text(t):
    '''source_text : description
                    | source_text description'''


def p_source_text_2(t):
    '''source_text : timeunits_declaration source_text '''

# description ::=
#   module_declaration
#   | udp_declaration
#   | interface_declaration
#   | program_declaration
#   | package_declaration
#   | { attribute_instance } package_item
#   | { attribute_instance } bind_directive
#   | config_declaration
def p_description(t):
    '''description : module_declaration'''


#| interface_declaration'''
# module_nonansi_header ::=
#   { attribute_instance } module_keyword [ lifetime ] module_identifier
#       { package_import_declaration } [ parameter_port_list ] list_of_ports ;
# module_ansi_header ::=
#   { attribute_instance } module_keyword [ lifetime ] module_identifier
#       { package_import_declaration }1 [ parameter_port_list ] [ list_of_port_declarations ] ;


# module_declaration ::=
#   module_nonansi_header [ timeunits_declaration ] { module_item }
#       endmodule [ : module_identifier ]
#   | module_ansi_header [ timeunits_declaration ] { non_port_module_item }
#       endmodule [ : module_identifier ]
#   | { attribute_instance } module_keyword [ lifetime ] module_identifier ( .* ) ;
#       [ timeunits_declaration ] { module_item } endmodule [ : module_identifier ]
#   | extern module_nonansi_header
#   | extern module_ansi_header
def p_module_declaration(t):
    '''module_declaration : module_keyword module_identifier endmodule'''


# module_keyword ::= module | macromodule
def p_module_keyword(t):
    '''module_keyword : module
                        | macromodule'''
# interface_declaration ::=
#   interface_nonansi_header [ timeunits_declaration ] { interface_item }
#       endinterface [ : interface_identifier ]
#   | interface_ansi_header [ timeunits_declaration ] { non_port_interface_item }
#       endinterface [ : interface_identifier ]
#   | { attribute_instance } interface interface_identifier ( .* ) ;
#       [ timeunits_declaration ] { interface_item }
#       endinterface [ : interface_identifier ]
#   | extern interface_nonansi_header
#   | extern interface_ansi_header
# interface_nonansi_header ::=
#   { attribute_instance } interface [ lifetime ] interface_identifier
#       { package_import_declaration } [ parameter_port_list ] list_of_ports ;
# interface_ansi_header ::=
#   {attribute_instance } interface [ lifetime ] interface_identifier
#       { package_import_declaration }1 [ parameter_port_list ] [ list_of_port_declarations ] ;
# program_declaration ::=
#   program_nonansi_header [ timeunits_declaration ] { program_item }
#       endprogram [ : program_identifier ]
#   | program_ansi_header [ timeunits_declaration ] { non_port_program_item }
#       endprogram [ : program_identifier ]
#   | { attribute_instance } program program_identifier ( .* ) ;
#       [ timeunits_declaration ] { program_item }
#       endprogram [ : program_identifier ]
#   | extern program_nonansi_header
#   | extern program_ansi_header
# program_nonansi_header ::=
#   { attribute_instance } program [ lifetime ] program_identifier
#   { package_import_declaration } [ parameter_port_list ] list_of_ports ;
# program_ansi_header ::=
#   {attribute_instance } program [ lifetime ] program_identifier
#   { package_import_declaration }1 [ parameter_port_list ] [ list_of_port_declarations ] ;
# checker_declaration ::=
# checker checker_identifier [ ( [ checker_port_list ] ) ] ;
#   { { attribute_instance } checker_or_generate_item }
#   endchecker [ : checker_identifier ]
# class_declaration ::=
#   [ virtual ] class [ lifetime ] class_identifier [ parameter_port_list ]
#   [ extends class_type [ ( list_of_arguments ) ] ]
#   [ implements interface_class_type { , interface_class_type } ] ;
#   { class_item }
#   endclass [ : class_identifier]
# interface_class_type ::= ps_class_identifier [ parameter_value_assignment ]
# interface_class_declaration ::=
#   interface class class_identifier [ parameter_port_list ]
#   [ extends interface_class_type { , interface_class_type } ] ;
#   { interface_class_item }
#   endclass [ : class_identifier]
# interface_class_item ::=
#   type_declaration
#   | { attribute_instance } interface_class_method
#   | local_parameter_declaration ;
#   | parameter_declaration7 ;
#   | ;
# interface_class_method ::=
#   pure virtual method_prototype ;
# package_declaration ::=
#   { attribute_instance } package [ lifetime ] package_identifier ;
#   [ timeunits_declaration ] { { attribute_instance } package_item }
#   endpackage [ : package_identifier ]

# timeunits_declaration ::=
#   timeunit time_literal [ / time_literal ] ;
#   | timeprecision time_literal ;
#   | timeunit time_literal ; timeprecision time_literal ;
#   | timeprecision time_literal ; timeunit time_literal ;
def p_timeunits_declaration(t):
    ''' timeunits_declaration : time_identifier'''




# A.9.3 Identifiers
# array_identifier ::= identifier
# block_identifier ::= identifier
# bin_identifier ::= identifier
# c_identifier49 ::= [ a-zA-Z_ ] { [ a-zA-Z0-9_ ] }
# cell_identifier ::= identifier
# checker_identifier ::= identifier
# class_identifier ::= identifier
# class_variable_identifier ::= variable_identifier
# clocking_identifier ::= identifier
# config_identifier ::= identifier
# const_identifier ::= identifier
# constraint_identifier ::= identifier
# covergroup_identifier ::= identifier
# covergroup_variable_identifier ::= variable_identifier
# cover_point_identifier ::= identifier
# cross_identifier ::= identifier
# dynamic_array_variable_identifier ::= variable_identifier
# enum_identifier ::= identifier
# escaped_identifier ::= \ {any_printable_ASCII_character_except_white_space} white_space
# formal_identifier ::= identifier
# formal_port_identifier ::= identifier
# function_identifier ::= identifier
# generate_block_identifier ::= identifier
# genvar_identifier ::= identifier
# hierarchical_array_identifier ::= hierarchical_identifier
# hierarchical_block_identifier ::= hierarchical_identifier
# hierarchical_event_identifier ::= hierarchical_identifier
# hierarchical_identifier ::= [ $root . ] { identifier constant_bit_select . } identifier
# hierarchical_net_identifier ::= hierarchical_identifier
# hierarchical_parameter_identifier ::= hierarchical_identifier
# hierarchical_property_identifier ::= hierarchical_identifier
# hierarchical_sequence_identifier ::= hierarchical_identifier
# hierarchical_task_identifier ::= hierarchical_identifier
# hierarchical_tf_identifier ::= hierarchical_identifier
# hierarchical_variable_identifier ::= hierarchical_identifier


# identifier ::=
#   simple_identifier
#   | escaped_identifier
# index_variable_identifier ::= identifier
# interface_identifier ::= identifier
# interface_instance_identifier ::= identifier
# inout_port_identifier ::= identifier
# input_port_identifier ::= identifier
# instance_identifier ::= identifier
# library_identifier ::= identifier
# member_identifier ::= identifier
# method_identifier ::= identifier
# modport_identifier ::= identifier


# module_identifier ::= identifier
def p_module_identifier(t):
    '''module_identifier : identifier'''

# This is made up by me to test ply.
# time_identifier ::= identifier
def p_time_identifier(t):
    '''time_identifier : identifier'''

# net_identifier ::= identifier
# net_type_identifier ::= identifier
# output_port_identifier ::= identifier
# package_identifier ::= identifier
# package_scope ::=
#   package_identifier ::
#   | $unit ::
# parameter_identifier ::= identifier
# port_identifier ::= identifier
# production_identifier ::= identifier
# program_identifier ::= identifier
# property_identifier ::= identifier
# ps_class_identifier ::= [ package_scope ] class_identifier
# ps_covergroup_identifier ::= [ package_scope ] covergroup_identifier
# ps_checker_identifier ::= [ package_scope ] checker_identifier
# ps_identifier ::= [ package_scope ] identifier
# ps_or_hierarchical_array_identifier ::=
#   [ implicit_class_handle . | class_scope | package_scope ] hierarchical_array_identifier
# ps_or_hierarchical_net_identifier ::= [ package_scope ] net_identifier | hierarchical_net_identifier
# ps_or_hierarchical_property_identifier ::=
#   [ package_scope ] property_identifier
#   | hierarchical_property_identifier
# ps_or_hierarchical_sequence_identifier ::=
#   [ package_scope ] sequence_identifier
#   | hierarchical_sequence_identifier
# ps_or_hierarchical_tf_identifier ::=
#   [ package_scope ] tf_identifier
#   | hierarchical_tf_identifier
# ps_parameter_identifier ::=
#   [ package_scope | class_scope ] parameter_identifier
#   | { generate_block_identifier [ [ constant_expression ] ] . } parameter_identifier
# ps_type_identifier ::= [ local ::43 | package_scope | class_scope ] type_identifier
# sequence_identifier ::= identifier
# signal_identifier ::= identifier
# simple_identifier49 ::= [ a-zA-Z_ ] { [ a-zA-Z0-9_$ ] }
# specparam_identifier ::= identifier
# system_tf_identifier50 ::= $[ a-zA-Z0-9_$ ]{ [ a-zA-Z0-9_$ ] }
# task_identifier ::= identifier
# tf_identifier ::= identifier
# terminal_identifier ::= identifier
# topmodule_identifier ::= identifier
# type_identifier ::= identifier
# udp_identifier ::= identifier
# variable_identifier ::= identifier






def p_error(t):
    if not t:
        print("SYNTAX ERROR AT EOF")
