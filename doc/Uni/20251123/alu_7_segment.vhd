--------------------------------------------------------------------------------
-- CITEC - Center of Excellence Cognitive Interaction Technology
-- Bielefeld University
-- Cognitronics & Sensor Systems
--
-- File Name   : alu_7_segment.vhd
-- Author      : Martin Kaiser and Sarah Pilz
-- Description : File for Lab2 
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
entity alu_7_segment Is
port (
  CLK : in STD_LOGIC;                       -- Clock input (100MHz)
  SWT : in STD_LOGIC_VECTOR(15 downto 0);
  SEG : out STD_LOGIC_VECTOR(6 downto 0);   -- 7-segment display segments
  AN  : out STD_LOGIC_VECTOR(3 downto 0)    -- 7-segment display anodes
);
end alu_7_segment;

--------------------
--  ARCHITECTURE  --
--------------------
architecture RTL of alu_7_segment is 

-----------------
--  CONSTANTS  --
-----------------
-- ALU Operation Codes
constant OP_ADD  : std_logic_vector(3 downto 0) := "0000";  -- A + B
constant OP_SUB  : std_logic_vector(3 downto 0) := "0001";  -- A - B
constant OP_MULT : std_logic_vector(3 downto 0) := "0010";  -- A * B
constant OP_DIV  : std_logic_vector(3 downto 0) := "0011";  -- A / B
constant OP_AND  : std_logic_vector(3 downto 0) := "0100";  -- A and B
constant OP_OR   : std_logic_vector(3 downto 0) := "0101";  -- A or B

-- Clock divider constant for 7-segment multiplexing
-- 100MHz / 100000 = 1kHz refresh rate (250Hz per digit)
constant REFRESH_COUNT : integer := 100000;

---------------------------
--  SIGNAL DECLARATIONS  --
---------------------------
signal a_in : std_logic_vector(3 downto 0);
signal b_in : std_logic_vector(3 downto 0);
signal ctrl_in : std_logic_vector(3 downto 0);
signal alu_result : std_logic_vector(7 downto 0);

-- Signals for 7-segment display
signal digit_0 : std_logic_vector(3 downto 0);  -- B_IN lower nibble
signal digit_1 : std_logic_vector(3 downto 0);  -- A_IN lower nibble
signal digit_2 : std_logic_vector(3 downto 0);  -- Result lower nibble
signal digit_3 : std_logic_vector(3 downto 0);  -- Result upper nibble

-- Multiplexing signals
signal refresh_counter : integer range 0 to REFRESH_COUNT := 0;
signal digit_select : std_logic_vector(1 downto 0) := "00";
signal current_digit : std_logic_vector(3 downto 0);

---------
begin  --
---------

--------------------------------
--  INPUT/OUTPUT ASSIGNMENTS  --
--------------------------------
-- Map switches to internal signals
a_in <= SWT(7 downto 4);      -- A_IN from SWT 7 to 4
b_in <= SWT(3 downto 0);      -- B_IN from SWT 3 to 0
ctrl_in <= SWT(15 downto 12); -- CTRL_IN from SWT 15 to 12

-- Assign digits for 7-segment display
digit_0 <= b_in;                          -- LED-0: B_IN
digit_1 <= a_in;                          -- LED-1: A_IN
digit_2 <= alu_result(3 downto 0);        -- LED-2: Result lower nibble
digit_3 <= alu_result(7 downto 4);        -- LED-3: Result upper nibble

-----------------
--  PROCESSES  --
-----------------  

-- ALU Process
alu_process: process(a_in, b_in, ctrl_in)
  variable a_unsigned : unsigned(7 downto 0);
  variable b_unsigned : unsigned(7 downto 0);
  variable temp_result : unsigned(7 downto 0);
  variable mult_result : unsigned(7 downto 0);
  variable sub_result : signed(8 downto 0);
  variable div_result : unsigned(7 downto 0);
begin
  -- Extend inputs to 8 bits (zero extend)
  a_unsigned := "0000" & unsigned(a_in);
  b_unsigned := "0000" & unsigned(b_in);
  
  -- Default output
  temp_result := (others => '0');
  
  -- Decode operation based on ctrl_in
  case ctrl_in is
    when OP_ADD =>
      -- Addition: A + B
      temp_result := a_unsigned + b_unsigned;
      
    when OP_SUB =>
      -- Subtraction: A - B (clamp to 0 if negative)
      sub_result := signed('0' & a_unsigned) - signed('0' & b_unsigned);
      if sub_result < 0 then
        temp_result := (others => '0');
      else
        temp_result := unsigned(sub_result(7 downto 0));
      end if;
      
    when OP_MULT =>
      -- Multiplication: A * B
      mult_result := unsigned(a_in) * unsigned(b_in);
      temp_result := mult_result;
      
    when OP_DIV =>
      -- Division: A / B (integer division)
      if b_unsigned = 0 then
        temp_result := (others => '1');  -- Error: division by zero (show FF)
      else
        div_result := a_unsigned / b_unsigned;
        temp_result := div_result;
      end if;
      
    when OP_AND =>
      -- Bitwise AND
      temp_result := a_unsigned and b_unsigned;
      
    when OP_OR =>
      -- Bitwise OR
      temp_result := a_unsigned or b_unsigned;
      
    when others =>
      -- Undefined operations output 0
      temp_result := (others => '0');
      
  end case;
  
  -- Assign to output signal
  alu_result <= std_logic_vector(temp_result);
  
end process alu_process;

-- Display Multiplexing Process
-- Cycles through 4 digits to create persistence of vision
multiplex_process: process(CLK)
begin
  if rising_edge(CLK) then
    if refresh_counter = REFRESH_COUNT - 1 then
      refresh_counter <= 0;
      -- Move to next digit
      digit_select <= std_logic_vector(unsigned(digit_select) + 1);
    else
      refresh_counter <= refresh_counter + 1;
    end if;
  end if;
end process multiplex_process;

-- Digit Selection Process
-- Selects which digit to display based on counter
digit_mux: process(digit_select, digit_0, digit_1, digit_2, digit_3)
begin
  case digit_select is
    when "00" =>
      AN <= "1110";  -- Enable digit 0 (rightmost, B_IN)
      current_digit <= digit_0;
    when "01" =>
      AN <= "1101";  -- Enable digit 1 (A_IN)
      current_digit <= digit_1;
    when "10" =>
      AN <= "1011";  -- Enable digit 2 (Result lower)
      current_digit <= digit_2;
    when "11" =>
      AN <= "0111";  -- Enable digit 3 (Result upper)
      current_digit <= digit_3;
    when others =>
      AN <= "1111";  -- All off
      current_digit <= "0000";
  end case;
end process digit_mux;

-- 7-Segment Decoder Process
-- Converts 4-bit binary to 7-segment display
-- Segments: SEG(6 downto 0) = CA (cathode segments, bit 6 = g, bit 0 = a)
-- Segment layout:
--     aaa
--    f   b
--     ggg
--    e   c
--     ddd
-- For Basys 3 common anode display, segments are ACTIVE LOW (0 = ON, 1 = OFF)
seg_decoder: process(current_digit)
begin
  -- Decode hex digit to 7-segment (active low for common anode)
  -- Format: gfedcba (SEG(6) to SEG(0))
  case current_digit is
    when "0000" => SEG <= "1000000"; -- 0
    when "0001" => SEG <= "1111001"; -- 1
    when "0010" => SEG <= "0100100"; -- 2
    when "0011" => SEG <= "0110000"; -- 3
    when "0100" => SEG <= "0011001"; -- 4
    when "0101" => SEG <= "0010010"; -- 5
    when "0110" => SEG <= "0000010"; -- 6
    when "0111" => SEG <= "1111000"; -- 7
    when "1000" => SEG <= "0000000"; -- 8
    when "1001" => SEG <= "0010000"; -- 9
    when "1010" => SEG <= "0001000"; -- A
    when "1011" => SEG <= "0000011"; -- b
    when "1100" => SEG <= "1000110"; -- C
    when "1101" => SEG <= "0100001"; -- d
    when "1110" => SEG <= "0000110"; -- E
    when "1111" => SEG <= "0001110"; -- F
    when others => SEG <= "1111111"; -- blank (all off)
  end case;
end process seg_decoder;

end RTL;
