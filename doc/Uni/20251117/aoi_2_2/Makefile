CWD=$(shell pwd)
export COCOTB_REDUCED_LOG_FMT = 1
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

ifeq ($(TOPLEVEL_LANG),verilog)
	# Check multiple possible locations for the Verilog file
	ifneq ("$(wildcard $(CWD)/hdl/verilog/aoi_2_2.v)","")
		VERILOG_SOURCES = $(CWD)/hdl/verilog/aoi_2_2.v
	else ifneq ("$(wildcard $(CWD)/aoi_2_2.v)","")
		VERILOG_SOURCES = $(CWD)/aoi_2_2.v
	else
		$(error "Cannot find aoi_2_2.v in $(CWD) or $(CWD)/hdl/verilog/")
	endif
else ifeq ($(TOPLEVEL_LANG),vhdl)
	# Check multiple possible locations for the VHDL file
	ifneq ("$(wildcard $(CWD)/hdl/vhdl/aoi_2_2.vhd)","")
		VHDL_SOURCES = $(CWD)/hdl/vhdl/aoi_2_2.vhd
	else ifneq ("$(wildcard $(CWD)/aoi_2_2.vhd)","")
		VHDL_SOURCES = $(CWD)/aoi_2_2.vhd
	else
		$(error "Cannot find aoi_2_2.vhd in $(CWD) or $(CWD)/hdl/vhdl/")
	endif
else
    $(error "A valid value (verilog or vhdl) was not provided for TOPLEVEL_LANG=$(TOPLEVEL_LANG)")
endif

ifeq ($(SIM), verilator)
    # Enable processing of #delay statements
    COMPILE_ARGS += --timing
endif

# Use COCOTB_TEST_MODULES instead of deprecated MODULE
COCOTB_TEST_MODULES := testbench
TOPLEVEL := aoi_2_2

# GHDL specific arguments (only used if SIM=ghdl)
GHDL_ARGS := --ieee=synopsys

# Time unit settings
COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

include $(shell cocotb-config --makefiles)/Makefile.sim

# Optional: include checkclean if it exists
-include ../../checkclean.mk
