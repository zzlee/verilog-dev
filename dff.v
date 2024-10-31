// File: dff.v
// Generated by MyHDL 0.11.49
// Date: Thu Oct 31 10:01:29 2024


`timescale 1ns/10ps

module dff (
    q,
    d,
    clk
);


output q;
reg q;
input d;
input clk;




always @(posedge clk) begin: DFF_LOGIC
    q <= d;
end

endmodule