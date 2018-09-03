# sv-tools

Tools for SystemVerilog HDL development.

# Setup

Requires no installation. Python 2.7. Tested on CENTOS.

Run setup.py to update credentials: full name of the author and author's company.

# Usage

All scripts accept -h and --help for help messages constructed with argparse package.

Scripts are supposed to accept a subset of SystemVerilog (most commonly used structures for synthesizable RTL):

    new_mod.py - generate new empty .sv file from template.
    gen_inst.py - generate instantiation .sv file. (Append to end of file in VIM?) 
    gen_top.py - generate top file: top, instantiate submodules, connect them via interfaces.
    gen_tb.py - generate empty test file.
 
Debug scripts:
  -> _util.py - utility for debugging
  -> self_test.py - tests for scripts, which are very simple and will not be extended.
