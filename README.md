# Status: do not ever, ever, ever, ever or ever use it on your design files.

First release expected Oct 2018.

# sv-tools

Tools for SystemVerilog HDL development.

## Dependencies
Python 3.6.5.

ply-3.11  - Can be obtained via python3-pip.

## Setup
 
Tested on Windows Subsystem for Linux - Ubuntu 18.04.

TODO: Run setup.py to update credentials: full name of the author and author's company for licensing templates.

## Usage

All scripts accept -h and --help for help messages constructed with argparse package.

Scripts are supposed to accept a subset of SystemVerilog (most commonly used structures for synthesizable RTL):

    gen_mod.py  - generate new empty file from template.
    gen_inst.py - generate instantiation file. 
    gen_top.py  - generate top file.
    gen_tb.py   - generate empty testbench file.
 
## SVEngine

Engine is composed of following modules:

    SVLexer     - extension of ply.lexer
    SVParser    - extension of ply.parser

Unit tests were created with unittests module.