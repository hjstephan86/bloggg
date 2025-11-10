--------------------------------------------------------------------------------
-- CITEC - Center of Excellence Cognitive Interaction Technology
-- Bielefeld University
-- Cognitronics & Sensor Systems
--
-- File Name   : lab2_mini_alu_tb.vhd
-- Author      : Martin Kaiser
-- Description : Repar Lab 2
--
-- Revision History:
--------------------------------------------------------------------------------
--
-- Version | Author                   | Date       | Changes
-----------+--------------------------+------------+----------------------------
-- 1.0     | Martin Kaiser            | 25.09.2017 | - initial release
--         | Sarah Pilz               |            |
-----------+--------------------------+------------+----------------------------


-----------------
--  LIBRARIES  --
-----------------
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;


--------------
--  ENTITY  --
--------------
entity lab2_mini_alu_tb is
end lab2_mini_alu_tb;


--------------------
--  ARCHITECTURE  --
--------------------
architecture BEH of lab2_mini_alu_tb is

  ------------------------------
  --  COMPONENT DECLARATIONS  --
  ------------------------------

  component mini_alu is
    port(
      SWT : in  std_logic_vector(15 downto 0);
      LED : out std_logic_vector(11 downto 0)
    );
  end component mini_alu;

  ---------------------------
  --  SIGNAL DECLARATIONS  --
  ---------------------------
  signal led         : std_logic_vector(11 downto 0);
  signal swt         : std_logic_vector(15 downto 0);

---------
begin                                   
  ---------

  -------------------------------
  --  COMPONENT INSTANTIAIONS  --
  -------------------------------
  mini_alu_inst : mini_alu
    port map(
      SWT => swt,
      LED => led
    );

  --------------------------------
  --  INPUT/OUTPUT ASSIGNMENTS  --
  --------------------------------


  -----------------------------
  --  CONCURRENT STATEMENTS  --
  -----------------------------

  -----------------
  --  PROCESSES  --
  -----------------

  testbench_p : process
  begin
    wait for 1 ns;
    -- set inputs to default values
    swt <= (others => '0');
    wait for 10 ns;

    ----------------------------------------------------------------------------
    -- CTRL CODE: 0000 - Pass A
    -- SWT(15:12) = CTRL, SWT(7:4) = A, SWT(3:0) = B
    ----------------------------------------------------------------------------
    report "Testing CTRL=0000 (Pass A)";
    
    -- Test 1: A=5, B=3 -> Output should be 5
    swt <= "0000" & "0000" & "0101" & "0011";  -- CTRL=0, unused, A=5, B=3
    wait for 10 ns;
    assert(led(7 downto 0) = "00000101") 
      report "CTRL=0000, Test 1 failed: Expected 00000101, got " & 
             integer'image(to_integer(unsigned(led(7 downto 0))))
      severity error;
    
    -- Test 2: A=15, B=0 -> Output should be 15
    swt <= "0000" & "0000" & "1111" & "0000";  -- CTRL=0, unused, A=15, B=0
    wait for 10 ns;
    assert(led(7 downto 0) = "00001111") 
      report "CTRL=0000, Test 2 failed: Expected 00001111" 
      severity error;

    ----------------------------------------------------------------------------
    -- CTRL CODE: 0001 - Pass B
    ----------------------------------------------------------------------------
    report "Testing CTRL=0001 (Pass B)";
    
    -- Test 3: A=5, B=7 -> Output should be 7
    swt <= "0001" & "0000" & "0101" & "0111";  -- CTRL=1, unused, A=5, B=7
    wait for 10 ns;
    assert(led(7 downto 0) = "00000111") 
      report "CTRL=0001, Test 3 failed: Expected 00000111" 
      severity error;
    
    -- Test 4: A=12, B=3 -> Output should be 3
    swt <= "0001" & "0000" & "1100" & "0011";  -- CTRL=1, unused, A=12, B=3
    wait for 10 ns;
    assert(led(7 downto 0) = "00000011") 
      report "CTRL=0001, Test 4 failed: Expected 00000011" 
      severity error;

    ----------------------------------------------------------------------------
    -- CTRL CODE: 0010 - Addition (A + B)
    ----------------------------------------------------------------------------
    report "Testing CTRL=0010 (Addition)";
    
    -- Test 5: 5 + 3 = 8
    swt <= "0010" & "0000" & "0101" & "0011";  -- CTRL=2, unused, A=5, B=3
    wait for 10 ns;
    assert(led(7 downto 0) = "00001000") 
      report "CTRL=0010, Test 5 failed: Expected 8, got " & 
             integer'image(to_integer(unsigned(led(7 downto 0))))
      severity error;
    
    -- Test 6: 15 + 15 = 30
    swt <= "0010" & "0000" & "1111" & "1111";  -- CTRL=2, unused, A=15, B=15
    wait for 10 ns;
    assert(led(7 downto 0) = "00011110") 
      report "CTRL=0010, Test 6 failed: Expected 30" 
      severity error;
    
    -- Test 7: 0 + 0 = 0
    swt <= "0010" & "0000" & "0000" & "0000";  -- CTRL=2, unused, A=0, B=0
    wait for 10 ns;
    assert(led(7 downto 0) = "00000000") 
      report "CTRL=0010, Test 7 failed: Expected 0" 
      severity error;

    ----------------------------------------------------------------------------
    -- CTRL CODE: 0011 - Subtraction (A - B)
    ----------------------------------------------------------------------------
    report "Testing CTRL=0011 (Subtraction)";
    
    -- Test 8: 10 - 3 = 7
    swt <= "0011" & "0000" & "1010" & "0011";  -- CTRL=3, unused, A=10, B=3
    wait for 10 ns;
    assert(led(7 downto 0) = "00000111") 
      report "CTRL=0011, Test 8 failed: Expected 7, got " & 
             integer'image(to_integer(unsigned(led(7 downto 0))))
      severity error;
    
    -- Test 9: 5 - 5 = 0
    swt <= "0011" & "0000" & "0101" & "0101";  -- CTRL=3, unused, A=5, B=5
    wait for 10 ns;
    assert(led(7 downto 0) = "00000000") 
      report "CTRL=0011, Test 9 failed: Expected 0" 
      severity error;
    
    -- Test 10: 3 - 10 = 0 (clamped to 0, no negative)
    swt <= "0011" & "0000" & "0011" & "1010";  -- CTRL=3, unused, A=3, B=10
    wait for 10 ns;
    assert(led(7 downto 0) = "00000000") 
      report "CTRL=0011, Test 10 failed: Expected 0 (clamped)" 
      severity error;

    ----------------------------------------------------------------------------
    -- CTRL CODE: 0100 - Multiplication (A * B)
    ----------------------------------------------------------------------------
    report "Testing CTRL=0100 (Multiplication)";
    
    -- Test 11: 5 * 3 = 15
    swt <= "0100" & "0000" & "0101" & "0011";  -- CTRL=4, unused, A=5, B=3
    wait for 10 ns;
    assert(led(7 downto 0) = "00001111") 
      report "CTRL=0100, Test 11 failed: Expected 15, got " & 
             integer'image(to_integer(unsigned(led(7 downto 0))))
      severity error;
    
    -- Test 12: 15 * 15 = 225
    swt <= "0100" & "0000" & "1111" & "1111";  -- CTRL=4, unused, A=15, B=15
    wait for 10 ns;
    assert(led(7 downto 0) = "11100001") 
      report "CTRL=0100, Test 12 failed: Expected 225" 
      severity error;
    
    -- Test 13: 7 * 0 = 0
    swt <= "0100" & "0000" & "0111" & "0000";  -- CTRL=4, unused, A=7, B=0
    wait for 10 ns;
    assert(led(7 downto 0) = "00000000") 
      report "CTRL=0100, Test 13 failed: Expected 0" 
      severity error;

    ----------------------------------------------------------------------------
    -- CTRL CODE: 0101 - Bitwise AND
    ----------------------------------------------------------------------------
    report "Testing CTRL=0101 (AND)";
    
    -- Test 14: 1111 AND 1010 = 1010
    swt <= "0101" & "0000" & "1111" & "1010";  -- CTRL=5, unused, A=15, B=10
    wait for 10 ns;
    assert(led(7 downto 0) = "00001010") 
      report "CTRL=0101, Test 14 failed: Expected 00001010" 
      severity error;
    
    -- Test 15: 1100 AND 0011 = 0000
    swt <= "0101" & "0000" & "1100" & "0011";  -- CTRL=5, unused, A=12, B=3
    wait for 10 ns;
    assert(led(7 downto 0) = "00000000") 
      report "CTRL=0101, Test 15 failed: Expected 00000000" 
      severity error;

    ----------------------------------------------------------------------------
    -- CTRL CODE: 0110 - Bitwise OR
    ----------------------------------------------------------------------------
    report "Testing CTRL=0110 (OR)";
    
    -- Test 16: 1100 OR 0011 = 1111
    swt <= "0110" & "0000" & "1100" & "0011";  -- CTRL=6, unused, A=12, B=3
    wait for 10 ns;
    assert(led(7 downto 0) = "00001111") 
      report "CTRL=0110, Test 16 failed: Expected 00001111" 
      severity error;
    
    -- Test 17: 1010 OR 0101 = 1111
    swt <= "0110" & "0000" & "1010" & "0101";  -- CTRL=6, unused, A=10, B=5
    wait for 10 ns;
    assert(led(7 downto 0) = "00001111") 
      report "CTRL=0110, Test 17 failed: Expected 00001111" 
      severity error;

    ----------------------------------------------------------------------------
    -- CTRL CODE: 1111 - Undefined operation (should output 0)
    ----------------------------------------------------------------------------
    report "Testing CTRL=1111 (Undefined)";
    
    -- Test 18: Undefined operation should output 0
    swt <= "1111" & "0000" & "1111" & "1111";  -- CTRL=15, unused, A=15, B=15
    wait for 10 ns;
    assert(led(7 downto 0) = "00000000") 
      report "CTRL=1111, Test 18 failed: Expected 00000000 for undefined" 
      severity error;

    ----------------------------------------------------------------------------
    -- Check upper LED bits are always 0
    ----------------------------------------------------------------------------
    report "Checking upper LED bits (11 downto 8) are always 0";
    assert(led(11 downto 8) = "0000") 
      report "Upper LED bits should be 0000" 
      severity error;

    ----------------------------------------------------------------------------
    -- End of tests
    ----------------------------------------------------------------------------
    report "All tests completed successfully!";
    wait for 10 ns;
     
    assert(1 = 0) report "Simulation complete. This is not an error :)"  severity FAILURE;      
    
  end process testbench_p;
end BEH;