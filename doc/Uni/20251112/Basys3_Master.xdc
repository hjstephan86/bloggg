## This file is a constraints file for Basys 3 Rev B board
## To use it in a project:
## - uncomment the lines corresponding to used ports
## - rename the used ports (in each line, after get_ports) according to the top level signal names in the project

## Clock signal (100MHz)
set_property PACKAGE_PIN W5 [get_ports CLK]
    set_property IOSTANDARD LVCMOS33 [get_ports CLK]
    create_clock -add -name sys_clk_pin -period 10.00 -waveform {0 5} [get_ports CLK]

## Switches
set_property PACKAGE_PIN V17 [get_ports {SWT[0]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[0]}]
set_property PACKAGE_PIN V16 [get_ports {SWT[1]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[1]}]
set_property PACKAGE_PIN W16 [get_ports {SWT[2]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[2]}]
set_property PACKAGE_PIN W17 [get_ports {SWT[3]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[3]}]
set_property PACKAGE_PIN W15 [get_ports {SWT[4]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[4]}]
set_property PACKAGE_PIN V15 [get_ports {SWT[5]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[5]}]
set_property PACKAGE_PIN W14 [get_ports {SWT[6]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[6]}]
set_property PACKAGE_PIN W13 [get_ports {SWT[7]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[7]}]
set_property PACKAGE_PIN V2 [get_ports {SWT[8]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[8]}]
set_property PACKAGE_PIN T3 [get_ports {SWT[9]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[9]}]
set_property PACKAGE_PIN T2 [get_ports {SWT[10]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[10]}]
set_property PACKAGE_PIN R3 [get_ports {SWT[11]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[11]}]
set_property PACKAGE_PIN W2 [get_ports {SWT[12]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[12]}]
set_property PACKAGE_PIN U1 [get_ports {SWT[13]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[13]}]
set_property PACKAGE_PIN T1 [get_ports {SWT[14]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[14]}]
set_property PACKAGE_PIN R2 [get_ports {SWT[15]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[15]}]

## 7-Segment Display Segments
set_property PACKAGE_PIN W7 [get_ports {SEG[0]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SEG[0]}]
set_property PACKAGE_PIN W6 [get_ports {SEG[1]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SEG[1]}]
set_property PACKAGE_PIN U8 [get_ports {SEG[2]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SEG[2]}]
set_property PACKAGE_PIN V8 [get_ports {SEG[3]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SEG[3]}]
set_property PACKAGE_PIN U5 [get_ports {SEG[4]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SEG[4]}]
set_property PACKAGE_PIN V5 [get_ports {SEG[5]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SEG[5]}]
set_property PACKAGE_PIN U7 [get_ports {SEG[6]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SEG[6]}]

## 7-Segment Display Anodes (Digit Enable)
set_property PACKAGE_PIN U2 [get_ports {AN[0]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {AN[0]}]
set_property PACKAGE_PIN U4 [get_ports {AN[1]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {AN[1]}]
set_property PACKAGE_PIN V4 [get_ports {AN[2]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {AN[2]}]
set_property PACKAGE_PIN W4 [get_ports {AN[3]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {AN[3]}]

## Configuration options, can be used for all designs
set_property CONFIG_VOLTAGE 3.3 [current_design]
set_property CFGBVS VCCO [current_design]
