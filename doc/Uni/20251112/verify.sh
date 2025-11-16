#!/bin/bash
# ==============================================================================
# Complete Verification Workflow
# Verifies that Amaranth-generated Verilog is equivalent to VHDL
# Generated with Claude AI
# ==============================================================================

echo "=========================================="
echo "Amaranth to VHDL Equivalence Verification"
echo "=========================================="
echo ""

# ==============================================================================
# Step 1: Generate Verilog from Amaranth (Python)
# ==============================================================================
echo ">>> Step 1: Generate Verilog from Amaranth..."
# python3 alu_7_segment.py

if [ $? -ne 0 ]; then
    echo "ERROR: Amaranth code generation failed!"
    exit 1
fi
echo "✓ Generated: alu_7_segment.v"
echo ""

# ==============================================================================
# Step 2: Generate Verilog from VHDL using GHDL
# ==============================================================================
echo ">>> Step 2: Generate Verilog from VHDL..."
ghdl --synth --std=08 --out=verilog alu_7_segment.vhd -e alu_7_segment > alu_7_segment_from_vhdl.v

if [ $? -ne 0 ]; then
    echo "ERROR: GHDL synthesis failed!"
    exit 1
fi
echo "✓ Generated: alu_7_segment_from_vhdl.v"
echo ""

# ==============================================================================
# Step 3: Formal Equivalence Check with Yosys
# ==============================================================================
echo ">>> Step 3: Running formal equivalence check..."
yosys -p "
    # Load Amaranth Verilog
    read_verilog alu_7_segment.v
    hierarchy -check -top alu_7_segment
    proc; opt; memory; opt
    flatten
    rename alu_7_segment alu_amaranth
    
    # Stash Amaranth design
    design -stash amaranth
    
    # Load VHDL-generated Verilog
    read_verilog alu_7_segment_from_vhdl.v
    hierarchy -check -top alu_7_segment
    proc; opt; memory; opt
    flatten
    rename alu_7_segment alu_vhdl
    
    # Stash VHDL design
    design -stash vhdl
    
    # Copy both designs into working design
    design -copy-from amaranth -as alu_amaranth alu_amaranth
    design -copy-from vhdl -as alu_vhdl alu_vhdl
    
    # Run equivalence check
    equiv_make alu_amaranth alu_vhdl equiv
    prep -top equiv
    equiv_simple -undef
    equiv_induct -undef
    equiv_status -assert
"

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✓ SUCCESS: Designs are equivalent!"
    echo "=========================================="
    echo ""
    echo "Amaranth-generated Verilog is functionally"
    echo "equivalent to the original VHDL design."
    exit 0
else
    echo ""
    echo "=========================================="
    echo "✗ FAILURE: Designs are NOT equivalent!"
    echo "=========================================="
    echo ""
    echo "There are differences between the Amaranth"
    echo "and VHDL implementations."
    exit 1
fi
