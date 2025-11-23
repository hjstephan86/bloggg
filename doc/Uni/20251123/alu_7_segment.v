//------------------------------------------------------------------------------
// CITEC - Center of Excellence Cognitive Interaction Technology
// Bielefeld University
// Cognitronics & Sensor Systems
//
// File Name   : alu_7_segment.v
// Author      : Martin Kaiser and Sarah Pilz
// Description : File for Lab2 (translated from VHDL to Verilog)
//
// Revision History:
//------------------------------------------------------------------------------
//
// Version | Author                   | Date       | Changes
//---------+--------------------------+------------+----------------------------
// 1.0     | Martin Kaiser            | 25.09.2017 | - initial release
//         | Sarah Pilz               |            |  
// 2.0     | Translation to Verilog   | 2025       | - VHDL to Verilog conversion
//---------+--------------------------+------------+----------------------------

module alu_7_segment (
  input wire CLK,                    // Clock input (100MHz)
  input wire [15:0] SWT,             // Switch inputs
  output reg [6:0] SEG,              // 7-segment display segments
  output reg [3:0] AN                // 7-segment display anodes
);

//---------------
//  PARAMETERS  //
//---------------
// ALU Operation Codes
localparam OP_ADD  = 4'b0000;  // A + B
localparam OP_SUB  = 4'b0001;  // A - B
localparam OP_MULT = 4'b0010;  // A * B
localparam OP_DIV  = 4'b0011;  // A / B
localparam OP_AND  = 4'b0100;  // A and B
localparam OP_OR   = 4'b0101;  // A or B

// Clock divider constant for 7-segment multiplexing
// 100MHz / 100000 = 1kHz refresh rate (250Hz per digit)
localparam REFRESH_COUNT = 100000;

//-----------------------
//  SIGNAL DECLARATIONS //
//-----------------------
wire [3:0] a_in;
wire [3:0] b_in;
wire [3:0] ctrl_in;
reg [7:0] alu_result;

// Signals for 7-segment display
wire [3:0] digit_0;  // B_IN lower nibble
wire [3:0] digit_1;  // A_IN lower nibble
wire [3:0] digit_2;  // Result lower nibble
wire [3:0] digit_3;  // Result upper nibble

// Multiplexing signals
reg [16:0] refresh_counter;
reg [1:0] digit_select;
reg [3:0] current_digit;

// ALU internal signals
reg [7:0] a_unsigned;
reg [7:0] b_unsigned;
reg [7:0] temp_result;
reg [8:0] sub_result;
//------------------------------
//  INPUT/OUTPUT ASSIGNMENTS  //
//------------------------------
// Map switches to internal signals
assign a_in = SWT[7:4];       // A_IN from SWT 7 to 4
assign b_in = SWT[3:0];       // B_IN from SWT 3 to 0
assign ctrl_in = SWT[15:12];  // CTRL_IN from SWT 15 to 12

// Assign digits for 7-segment display
assign digit_0 = b_in;             // LED-0: B_IN
assign digit_1 = a_in;             // LED-1: A_IN
assign digit_2 = alu_result[3:0];  // LED-2: Result lower nibble
assign digit_3 = alu_result[7:4];  // LED-3: Result upper nibble

//---------------
//  ALU PROCESS //
//---------------
always @(*) begin 
  // Extend inputs to 8 bits (zero extend)
  a_unsigned = {4'b0000, a_in};
  b_unsigned = {4'b0000, b_in};
 
  // Default output
  temp_result = 8'b0;
 
  // Decode operation based on ctrl_in
  case (ctrl_in)
    OP_ADD: begin
      // Addition: A + B
      temp_result = a_unsigned + b_unsigned;
  
    end
   
    OP_SUB: begin
      // Subtraction: A - B (clamp to 0 if negative)
      sub_result = {1'b0, a_unsigned} - {1'b0, b_unsigned};
      if (sub_result[8]) begin  // Check sign bit
        temp_result = 8'b0;
      end else begin
        temp_result = sub_result[7:0];
      end
    end
   
    OP_MULT: begin
      // Multiplication: A * B
      temp_result = a_in * b_in;
    end
   
    OP_DIV: begin
      // Division: A / B (integer division)
      if (b_unsigned == 0) begin
        temp_result = 8'hFF;  // Error: division by zero (show FF)
      end else begin
        temp_result = a_unsigned / b_unsigned;
      end
    end
   
    OP_AND: begin
      // Bitwise AND
      temp_result = a_unsigned & b_unsigned;
    end
   
    OP_OR: begin
      // Bitwise OR
      temp_result = a_unsigned | b_unsigned;
    end
   
    default: begin
      // Undefined operations output 0
      temp_result = 8'b0;
    end
  endcase
 
  // Assign to output signal
  alu_result = temp_result;
end

//-------------------------------
//  DISPLAY MULTIPLEXING PROCESS //
//-------------------------------
// Cycles through 4 digits to create persistence of vision
always @(posedge CLK) begin
  if (refresh_counter == REFRESH_COUNT - 1) begin
    refresh_counter <= 0;
    // Move to next digit
    digit_select <= digit_select + 1;
  end else begin
    refresh_counter <= refresh_counter + 1;
  end
end

//---------------------------
//  DIGIT SELECTION PROCESS //
//---------------------------
// Selects which digit to display based on counter
always @(*) begin
  case (digit_select)
    2'b00: begin
      AN = 4'b1110;  // Enable digit 0 (rightmost, B_IN)
      current_digit = digit_0;
    end
    2'b01: begin
      AN = 4'b1101;  // Enable digit 1 (A_IN)
      current_digit = digit_1;
    end
    2'b10: begin
      AN = 4'b1011;  // Enable digit 2 (Result lower)
      current_digit = digit_2;
    end
    2'b11: begin
      AN = 4'b0111;  // Enable digit 3 (Result upper)
      current_digit = digit_3;
    end
    default: begin
      AN = 4'b1111;  // All off
      current_digit = 4'b0000;
    end
  endcase
end

//----------------------------
//  7-SEGMENT DECODER PROCESS //
//----------------------------
// Converts 4-bit binary to 7-segment display
// Segments: SEG[6:0] = CA (cathode segments, bit 6 = g, bit 0 = a)
// Segment layout:
//     aaa
//    f   b
//     ggg
//    e   c
//     ddd
// For Basys 3 common anode display, segments are ACTIVE LOW (0 = ON, 1 = OFF)
always @(*) begin
  // Decode hex digit to 7-segment (active low for common anode)
  // Format: gfedcba (SEG[6] to SEG[0])
  case (current_digit)
    4'h0: SEG = 7'b1000000; // 0
    4'h1: SEG = 7'b1111001; // 1
    4'h2: SEG = 7'b0100100; // 2
    4'h3: SEG = 7'b0110000; // 3
    4'h4: SEG = 7'b0011001; // 4
    4'h5: SEG = 7'b0010010; // 5
    4'h6: SEG = 7'b0000010; // 6
    4'h7: SEG = 7'b1111000; // 7
    4'h8: SEG = 7'b0000000; // 8
    4'h9: SEG = 7'b0010000; // 9
    4'hA: SEG = 7'b0001000; // A
    4'hB: SEG = 7'b0000011; // b
    4'hC: SEG = 7'b1000110; // C
    4'hD: SEG = 7'b0100001; // d
    4'hE: SEG = 7'b0000110; // E
    4'hF: SEG = 7'b0001110; // F
    default: SEG = 7'b1111111; // blank (all off)
  endcase
end

endmodule
