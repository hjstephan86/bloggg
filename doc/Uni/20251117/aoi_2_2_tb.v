// AOI Testbench for Basys3 Board - Simulation File
// Filename: aoi_2_2_tb.v

`timescale 1ns / 1ps

module aoi_2_2_tb;
    reg [3:0] SWT;
    wire [6:0] SEG;
    wire [3:0] AN;
    
    // Internal signals for monitoring
    wire a, b, c, d, y;
    
    // Extract internal signals for display
    assign a = SWT[0];
    assign b = SWT[1];
    assign c = SWT[2];
    assign d = SWT[3];
    assign y = ~((a & b) | (c & d));  // Expected AOI output
    
    // Instantiate the AOI module
    aoi_2_2 dut (
        .SWT(SWT),
        .SEG(SEG),
        .AN(AN)
    );
    
    initial begin
        $display("Starting AOI Basys3 testbench simulation...");
        $display("Time\t SWT[3:0] | a b c d | y | SEG      | AN   | Display");
        $display("-----------------------------------------------------------");
        
        // Test all input combinations
        SWT = 4'b0000; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b0001; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b0010; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b0011; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b0100; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b0101; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b0110; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b0111; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b1000; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b1001; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b1010; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b1011; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b1100; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b1101; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b1110; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        SWT = 4'b1111; #10;
        $display("%0t\t %b     | %b %b %b %b | %b | %b | %b | %s", 
                 $time, SWT, a, b, c, d, y, SEG, AN, (SEG == 7'b1111001) ? "1" : "0");
        
        $display("\nSimulation completed successfully!");
        $display("\nKey test cases:");
        $display("- When a=1,b=1 OR c=1,d=1 -> Output should be 0 (Display '0')");
        $display("- Otherwise -> Output should be 1 (Display '1')");
        $finish;
    end
endmodule