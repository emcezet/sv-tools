// MIT License
//
// Copyright (c)
// Date    :xxx
// Author  :xxx
// Company :xxx
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.


/*
 * Multi -line comment
 *
 *
 *
 */

module module_one#(
    // parameter
    )(
    // IN
    input clk, /* This is also a comment */
    input arst,
    input arst_n,
    input srst,
    input srst_n
    // INOUT

    // OUT

    );

///////////////////////////////////////////////////////////////////////////////
// Signal declarations.


///////////////////////////////////////////////////////////////////////////////

always_comb
begin : comb_process

end

// By default, it is assumed that an asynch high-level reset is used.
always_ff @ ( posedge clk or posedge arst )
begin : synch_process
    if ( arst )
        begin

        end
    else
        begin

        end
end

/*
 * Multi -line comment
 *
 *
 *
 */
endmodule

