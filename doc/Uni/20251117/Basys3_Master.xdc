## AOI Module Constraints for Basys3 Board
## Filename: aoi_constraints.xdc

## Switches (Inputs a, b, c, d)
set_property PACKAGE_PIN V17 [get_ports {SWT[0]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[0]}]
set_property PACKAGE_PIN V16 [get_ports {SWT[1]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[1]}]
set_property PACKAGE_PIN W16 [get_ports {SWT[2]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[2]}]
set_property PACKAGE_PIN W17 [get_ports {SWT[3]}]
    set_property IOSTANDARD LVCMOS33 [get_ports {SWT[3]}]

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

## Configuration options
set_property CONFIG_VOLTAGE 3.3 [current_design]
set_property CFGBVS VCCO [current_design]