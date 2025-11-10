--------------------------------------------------------------------------------
-- CITEC - Center of Excellence Cognitive Interaction Technology
-- Bielefeld University
-- Cognitronics & Sensor Systems
--
-- File Name   : mini_alu.vhd
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
entity mini_alu Is
port (
  SWT : in STD_LOGIC_VECTOR(15 downto 0);
  LED : out STD_LOGIC_VECTOR(11 downto 0)
);
end mini_alu;

--------------------
--  ARCHITECTURE  --
--------------------
architecture RTL of mini_alu is 

-----------------
--  CONSTANTS  --
-----------------
-- ALU Operation Codes
constant OP_A    : std_logic_vector(3 downto 0) := "0000";  -- Pass A
constant OP_B    : std_logic_vector(3 downto 0) := "0001";  -- Pass B
constant OP_ADD  : std_logic_vector(3 downto 0) := "0010";  -- A + B
constant OP_SUB  : std_logic_vector(3 downto 0) := "0011";  -- A - B
constant OP_MULT : std_logic_vector(3 downto 0) := "0100";  -- A * B
constant OP_AND  : std_logic_vector(3 downto 0) := "0101";  -- A and B
constant OP_OR   : std_logic_vector(3 downto 0) := "0110";  -- A or B

---------------------------
--  SIGNAL DECLARATIONS  --
---------------------------
signal alu_out_int : std_logic_vector(7 downto 0) := (others => '0');
signal a_in : std_logic_vector(3 downto 0);
signal b_in : std_logic_vector(3 downto 0);
signal ctrl_in : std_logic_vector(3 downto 0);

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

-- Assign ALU output to LED(7 downto 0), upper bits to 0
LED(7 downto 0) <= alu_out_int;
LED(11 downto 8) <= "0000";

-----------------
--  PROCESSES  --
-----------------  
alu_process: process(a_in, b_in, ctrl_in)
  variable a_unsigned : unsigned(7 downto 0);
  variable b_unsigned : unsigned(7 downto 0);
  variable temp_result : unsigned(7 downto 0);
  variable mult_result : unsigned(7 downto 0);
  variable sub_result : signed(8 downto 0);
begin
  -- Extend inputs to 8 bits (zero extend)
  a_unsigned := "0000" & unsigned(a_in);
  b_unsigned := "0000" & unsigned(b_in);
  
  -- Default output
  temp_result := (others => '0');
  
  -- Decode operation based on ctrl_in
  case ctrl_in is
    when OP_A =>
      -- Output A_IN
      temp_result := a_unsigned;
      
    when OP_B =>
      -- Output B_IN
      temp_result := b_unsigned;
      
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
      -- Multiplication: A * B (only lower 8 bits)
      mult_result := unsigned(a_in) * unsigned(b_in);
      temp_result := mult_result;
      
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
  alu_out_int <= std_logic_vector(temp_result);
  
end process alu_process;

end RTL;