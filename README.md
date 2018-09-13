# Status: do not ever, ever, ever, ever or ever use it on your design files.

First release expected Oct 2018.

# sv-tools

Tools for SystemVerilog HDL development.

## Dependencies
Python 3.6.5.

ply-3.11  - Can be obtained via python3-pip or from https://github.com/dabeaz/ply

Only for documentation : LaTeX, latexmk. 

## Setup
 
Tested on:

    [ ] Windows 10
    [*] Windows Subsystem for Linux - Ubuntu 18.04.
    [ ] Centos
    [ ] Fedora
    
    Legend:
        completed x
        in progress *
        in planning ' '

TODO: Run setup.py to update credentials: full name of the author and author's company for licensing templates.

## Usage

##### Documentation

All documentation can be found under docs/doc.tex Run this command to build a pdf.

    latexmk -pdf doc.tex

NOTE : doc.pdf should be available with all releases.

All scripts accept -h and --help for help messages. Scripts are supposed to accept a 
subset of SystemVerilog (most commonly used structures for synthesizable RTL):

    gen_mod.py  - Generates new empty file from template.
    gen_inst.py - Generates instantiation file. 
    gen_top.py  - Generates top file.
    gen_tb.py   - Generates empty testbench file.
 
    setup.py    - Update your credential for license. 
                  Select desired license from templates.
                  Register new template.
                  Choose preffered style.
    
## SVEngine

Engine is composed of following modules:

    SVLexer     - Extension of ply.lexer. Supports tokens described in doc.pdf.
    SVParser    - Extension of ply.parser. Supports re-written SV described in doc.pdf.

Unit tests were created with unittests module.

    UtSVLexer   - Unit test of SVLexer.
    UtSVParser  - Unit test of SVParser.
    
As part of development, a simple evaluation of ply is constructed.

    EvalLexer   - Extension of ply.lexer. Very simple lexer.
    EvalParser   - Extension of ply.parser. Supports multiple grammars for testing.

## TODO
    [*] Rewrite syntax from standard to unambiguous form.
    [*] Evalute ply and test for required rules.
    [*] Develop SVLexer.
    [*] Test SVLexer.
    [*] Develop SVParser.
    [*] Test SVParser.
    [ ] Develop SVEmitter.
    [ ] Test SVEmitter.
    [ ] Develop templates.
    [ ] Develop scripts based on SVEmitter.
    [ ] Test scripts.
    [ ] Develop setup script.
    
    Legend:
        completed x
        in progress *
        in planning ' '
