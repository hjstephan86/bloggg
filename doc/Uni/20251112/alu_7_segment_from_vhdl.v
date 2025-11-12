module alu_7_segment
  (input  CLK,
   input  [15:0] SWT,
   output [6:0] SEG,
   output [3:0] AN);
  wire [3:0] a_in;
  wire [3:0] b_in;
  wire [3:0] ctrl_in;
  wire [7:0] alu_result;
  wire [3:0] digit_0;
  wire [3:0] digit_1;
  wire [3:0] digit_2;
  wire [3:0] digit_3;
  reg [16:0] refresh_counter;
  reg [1:0] digit_select;
  wire [3:0] current_digit;
  wire [3:0] n4_o;
  wire [3:0] n5_o;
  wire [3:0] n6_o;
  wire [3:0] n7_o;
  wire [3:0] n8_o;
  wire [7:0] n17_o;
  wire [7:0] n19_o;
  wire [7:0] n20_o;
  wire n22_o;
  wire [8:0] n24_o;
  wire [8:0] n26_o;
  wire [8:0] n27_o;
  wire n29_o;
  wire [7:0] n30_o;
  wire [7:0] n32_o;
  wire n34_o;
  wire [7:0] n35_o;
  wire [7:0] n36_o;
  wire [7:0] n37_o;
  wire n39_o;
  wire n41_o;
  wire [7:0] n42_o;
  wire [7:0] n44_o;
  wire n47_o;
  wire [7:0] n48_o;
  wire n50_o;
  wire [7:0] n51_o;
  wire n53_o;
  wire [5:0] n54_o;
  reg [7:0] n56_o;
  wire [31:0] n64_o;
  wire n66_o;
  wire [1:0] n68_o;
  wire [31:0] n69_o;
  wire [31:0] n71_o;
  wire [16:0] n72_o;
  wire [16:0] n74_o;
  wire n81_o;
  wire n83_o;
  wire n85_o;
  wire n87_o;
  wire [3:0] n88_o;
  reg [3:0] n94_o;
  reg [3:0] n96_o;
  wire n100_o;
  wire n102_o;
  wire n104_o;
  wire n106_o;
  wire n108_o;
  wire n110_o;
  wire n112_o;
  wire n114_o;
  wire n116_o;
  wire n118_o;
  wire n120_o;
  wire n122_o;
  wire n124_o;
  wire n126_o;
  wire n128_o;
  wire n130_o;
  wire [15:0] n131_o;
  reg [6:0] n149_o;
  reg [16:0] n151_q;
  wire [1:0] n152_o;
  reg [1:0] n153_q;
  assign SEG = n149_o;
  assign AN = n94_o;
  /* alu_7_segment.vhd:61:8  */
  assign a_in = n4_o; // (signal)
  /* alu_7_segment.vhd:62:8  */
  assign b_in = n5_o; // (signal)
  /* alu_7_segment.vhd:63:8  */
  assign ctrl_in = n6_o; // (signal)
  /* alu_7_segment.vhd:64:8  */
  assign alu_result = n56_o; // (signal)
  /* alu_7_segment.vhd:67:8  */
  assign digit_0 = b_in; // (signal)
  /* alu_7_segment.vhd:68:8  */
  assign digit_1 = a_in; // (signal)
  /* alu_7_segment.vhd:69:8  */
  assign digit_2 = n7_o; // (signal)
  /* alu_7_segment.vhd:70:8  */
  assign digit_3 = n8_o; // (signal)
  /* alu_7_segment.vhd:73:8  */
  always @*
    refresh_counter = n151_q; // (isignal)
  initial
    refresh_counter = 17'b00000000000000000;
  /* alu_7_segment.vhd:74:8  */
  always @*
    digit_select = n153_q; // (isignal)
  initial
    digit_select = 2'b00;
  /* alu_7_segment.vhd:75:8  */
  assign current_digit = n96_o; // (signal)
  /* alu_7_segment.vhd:85:12  */
  assign n4_o = SWT[7:4];
  /* alu_7_segment.vhd:86:12  */
  assign n5_o = SWT[3:0];
  /* alu_7_segment.vhd:87:15  */
  assign n6_o = SWT[15:12];
  /* alu_7_segment.vhd:92:22  */
  assign n7_o = alu_result[3:0];
  /* alu_7_segment.vhd:93:22  */
  assign n8_o = alu_result[7:4];
  /* alu_7_segment.vhd:109:24  */
  assign n17_o = {4'b0000, a_in};
  /* alu_7_segment.vhd:110:24  */
  assign n19_o = {4'b0000, b_in};
  /* alu_7_segment.vhd:119:33  */
  assign n20_o = n17_o + n19_o;
  /* alu_7_segment.vhd:117:5  */
  assign n22_o = ctrl_in == 4'b0000;
  /* alu_7_segment.vhd:123:32  */
  assign n24_o = {1'b0, n17_o};
  /* alu_7_segment.vhd:123:59  */
  assign n26_o = {1'b0, n19_o};
  /* alu_7_segment.vhd:123:46  */
  assign n27_o = n24_o - n26_o;
  /* alu_7_segment.vhd:124:21  */
  assign n29_o = $signed(n27_o) < $signed(9'b000000000);
  /* alu_7_segment.vhd:127:43  */
  assign n30_o = n27_o[7:0];
  /* alu_7_segment.vhd:124:7  */
  assign n32_o = n29_o ? 8'b00000000 : n30_o;
  /* alu_7_segment.vhd:121:5  */
  assign n34_o = ctrl_in == 4'b0001;
  /* alu_7_segment.vhd:132:37  */
  assign n35_o = {4'b0, a_in};  //  uext
  /* alu_7_segment.vhd:132:37  */
  assign n36_o = {4'b0, b_in};  //  uext
  /* alu_7_segment.vhd:132:37  */
  assign n37_o = n35_o * n36_o; // umul
  /* alu_7_segment.vhd:130:5  */
  assign n39_o = ctrl_in == 4'b0010;
  /* alu_7_segment.vhd:137:21  */
  assign n41_o = n19_o == 8'b00000000;
  /* alu_7_segment.vhd:140:34  */
  assign n42_o = n17_o / n19_o; // udiv
  /* alu_7_segment.vhd:137:7  */
  assign n44_o = n41_o ? 8'b11111111 : n42_o;
  /* alu_7_segment.vhd:135:5  */
  assign n47_o = ctrl_in == 4'b0011;
  /* alu_7_segment.vhd:146:33  */
  assign n48_o = n17_o & n19_o;
  /* alu_7_segment.vhd:144:5  */
  assign n50_o = ctrl_in == 4'b0100;
  /* alu_7_segment.vhd:150:33  */
  assign n51_o = n17_o | n19_o;
  /* alu_7_segment.vhd:148:5  */
  assign n53_o = ctrl_in == 4'b0101;
  assign n54_o = {n53_o, n50_o, n47_o, n39_o, n34_o, n22_o};
  /* alu_7_segment.vhd:116:3  */
  always @*
    case (n54_o)
      6'b100000: n56_o = n51_o;
      6'b010000: n56_o = n48_o;
      6'b001000: n56_o = n44_o;
      6'b000100: n56_o = n37_o;
      6'b000010: n56_o = n32_o;
      6'b000001: n56_o = n20_o;
      default: n56_o = 8'b00000000;
    endcase
  /* alu_7_segment.vhd:168:24  */
  assign n64_o = {15'b0, refresh_counter};  //  uext
  /* alu_7_segment.vhd:168:24  */
  assign n66_o = n64_o == 32'b00000000000000011000011010011111;
  /* alu_7_segment.vhd:171:63  */
  assign n68_o = digit_select + 2'b01;
  /* alu_7_segment.vhd:173:42  */
  assign n69_o = {15'b0, refresh_counter};  //  uext
  /* alu_7_segment.vhd:173:42  */
  assign n71_o = n69_o + 32'b00000000000000000000000000000001;
  /* alu_7_segment.vhd:173:26  */
  assign n72_o = n71_o[16:0];  // trunc
  /* alu_7_segment.vhd:168:5  */
  assign n74_o = n66_o ? 17'b00000000000000000 : n72_o;
  /* alu_7_segment.vhd:183:5  */
  assign n81_o = digit_select == 2'b00;
  /* alu_7_segment.vhd:186:5  */
  assign n83_o = digit_select == 2'b01;
  /* alu_7_segment.vhd:189:5  */
  assign n85_o = digit_select == 2'b10;
  /* alu_7_segment.vhd:192:5  */
  assign n87_o = digit_select == 2'b11;
  assign n88_o = {n87_o, n85_o, n83_o, n81_o};
  /* alu_7_segment.vhd:182:3  */
  always @*
    case (n88_o)
      4'b1000: n94_o = 4'b0111;
      4'b0100: n94_o = 4'b1011;
      4'b0010: n94_o = 4'b1101;
      4'b0001: n94_o = 4'b1110;
      default: n94_o = 4'b1111;
    endcase
  /* alu_7_segment.vhd:182:3  */
  always @*
    case (n88_o)
      4'b1000: n96_o = digit_3;
      4'b0100: n96_o = digit_2;
      4'b0010: n96_o = digit_1;
      4'b0001: n96_o = digit_0;
      default: n96_o = 4'b0000;
    endcase
  /* alu_7_segment.vhd:216:5  */
  assign n100_o = current_digit == 4'b0000;
  /* alu_7_segment.vhd:217:5  */
  assign n102_o = current_digit == 4'b0001;
  /* alu_7_segment.vhd:218:5  */
  assign n104_o = current_digit == 4'b0010;
  /* alu_7_segment.vhd:219:5  */
  assign n106_o = current_digit == 4'b0011;
  /* alu_7_segment.vhd:220:5  */
  assign n108_o = current_digit == 4'b0100;
  /* alu_7_segment.vhd:221:5  */
  assign n110_o = current_digit == 4'b0101;
  /* alu_7_segment.vhd:222:5  */
  assign n112_o = current_digit == 4'b0110;
  /* alu_7_segment.vhd:223:5  */
  assign n114_o = current_digit == 4'b0111;
  /* alu_7_segment.vhd:224:5  */
  assign n116_o = current_digit == 4'b1000;
  /* alu_7_segment.vhd:225:5  */
  assign n118_o = current_digit == 4'b1001;
  /* alu_7_segment.vhd:226:5  */
  assign n120_o = current_digit == 4'b1010;
  /* alu_7_segment.vhd:227:5  */
  assign n122_o = current_digit == 4'b1011;
  /* alu_7_segment.vhd:228:5  */
  assign n124_o = current_digit == 4'b1100;
  /* alu_7_segment.vhd:229:5  */
  assign n126_o = current_digit == 4'b1101;
  /* alu_7_segment.vhd:230:5  */
  assign n128_o = current_digit == 4'b1110;
  /* alu_7_segment.vhd:231:5  */
  assign n130_o = current_digit == 4'b1111;
  assign n131_o = {n130_o, n128_o, n126_o, n124_o, n122_o, n120_o, n118_o, n116_o, n114_o, n112_o, n110_o, n108_o, n106_o, n104_o, n102_o, n100_o};
  /* alu_7_segment.vhd:215:3  */
  always @*
    case (n131_o)
      16'b1000000000000000: n149_o = 7'b0001110;
      16'b0100000000000000: n149_o = 7'b0000110;
      16'b0010000000000000: n149_o = 7'b0100001;
      16'b0001000000000000: n149_o = 7'b1000110;
      16'b0000100000000000: n149_o = 7'b0000011;
      16'b0000010000000000: n149_o = 7'b0001000;
      16'b0000001000000000: n149_o = 7'b0010000;
      16'b0000000100000000: n149_o = 7'b0000000;
      16'b0000000010000000: n149_o = 7'b1111000;
      16'b0000000001000000: n149_o = 7'b0000010;
      16'b0000000000100000: n149_o = 7'b0010010;
      16'b0000000000010000: n149_o = 7'b0011001;
      16'b0000000000001000: n149_o = 7'b0110000;
      16'b0000000000000100: n149_o = 7'b0100100;
      16'b0000000000000010: n149_o = 7'b1111001;
      16'b0000000000000001: n149_o = 7'b1000000;
      default: n149_o = 7'b1111111;
    endcase
  /* alu_7_segment.vhd:167:3  */
  always @(posedge CLK)
    n151_q <= n74_o;
  initial
    n151_q = 17'b00000000000000000;
  /* alu_7_segment.vhd:167:3  */
  assign n152_o = n66_o ? n68_o : digit_select;
  /* alu_7_segment.vhd:167:3  */
  always @(posedge CLK)
    n153_q <= n152_o;
  initial
    n153_q = 2'b00;
endmodule

