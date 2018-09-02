`define DEFINED_IN_A_MACRO 8
`define DEFINED_IN_ANOTHER_MACRO 16

module sample#(
    // parameters
    parameter paramOne = 8,
    parameter paramTwo = `DEFINED_IN_A_MACRO,
    parameter paramThree = paramOne * paramTwo 
    )(
    // IN
    input clk,
    input arst,
    input [7:0] d1,
    // INOUT
    inout [paramOne:0] d2,
    // OUT
    output [0:`DEFINED_IN_ANOTHER_MACRO] d3,
    // Interface style of connection.
    clk_if.sink clkif
    );

/*
 * Module body.
 *
*/

endmodule
