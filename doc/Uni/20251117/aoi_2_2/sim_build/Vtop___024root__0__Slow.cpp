// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop.h for the primary calling header

#include "Vtop__pch.h"

VL_ATTR_COLD void Vtop___024root___eval_static(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_static\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
}

VL_ATTR_COLD void Vtop___024root___eval_initial__TOP(Vtop___024root* vlSelf);

VL_ATTR_COLD void Vtop___024root___eval_initial(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_initial\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    Vtop___024root___eval_initial__TOP(vlSelf);
}

VL_ATTR_COLD void Vtop___024root___eval_initial__TOP(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_initial__TOP\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.aoi_2_2__DOT__AN = 0x0eU;
}

VL_ATTR_COLD void Vtop___024root___eval_final(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_final\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__stl(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag);
#endif  // VL_DEBUG
VL_ATTR_COLD bool Vtop___024root___eval_phase__stl(Vtop___024root* vlSelf);

VL_ATTR_COLD void Vtop___024root___eval_settle(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_settle\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    IData/*31:0*/ __VstlIterCount;
    // Body
    __VstlIterCount = 0U;
    vlSelfRef.__VstlFirstIteration = 1U;
    do {
        if (VL_UNLIKELY(((0x00000064U < __VstlIterCount)))) {
#ifdef VL_DEBUG
            Vtop___024root___dump_triggers__stl(vlSelfRef.__VstlTriggered, "stl"s);
#endif
            VL_FATAL_MT("/home/stephan/Git/pyuvm/examples/aoi_2_2/hdl/verilog/aoi_2_2.v", 6, "", "Settle region did not converge after 100 tries");
        }
        __VstlIterCount = ((IData)(1U) + __VstlIterCount);
    } while (Vtop___024root___eval_phase__stl(vlSelf));
}

VL_ATTR_COLD void Vtop___024root___eval_triggers__stl(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_triggers__stl\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__VstlTriggered[0U] = ((0xfffffffffffffffeULL 
                                      & vlSelfRef.__VstlTriggered
                                      [0U]) | (IData)((IData)(vlSelfRef.__VstlFirstIteration)));
    vlSelfRef.__VstlFirstIteration = 0U;
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vtop___024root___dump_triggers__stl(vlSelfRef.__VstlTriggered, "stl"s);
    }
#endif
}

VL_ATTR_COLD bool Vtop___024root___trigger_anySet__stl(const VlUnpacked<QData/*63:0*/, 1> &in);

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__stl(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__stl\n"); );
    // Body
    if ((1U & (~ (IData)(Vtop___024root___trigger_anySet__stl(triggers))))) {
        VL_DBG_MSGS("         No '" + tag + "' region triggers active\n");
    }
    if ((1U & (IData)(triggers[0U]))) {
        VL_DBG_MSGS("         '" + tag + "' region trigger index 0 is active: Internal 'stl' trigger - first iteration\n");
    }
}
#endif  // VL_DEBUG

VL_ATTR_COLD bool Vtop___024root___trigger_anySet__stl(const VlUnpacked<QData/*63:0*/, 1> &in) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___trigger_anySet__stl\n"); );
    // Locals
    IData/*31:0*/ n;
    // Body
    n = 0U;
    do {
        if (in[n]) {
            return (1U);
        }
        n = ((IData)(1U) + n);
    } while ((1U > n));
    return (0U);
}

void Vtop___024root___ico_sequent__TOP__0(Vtop___024root* vlSelf);

VL_ATTR_COLD void Vtop___024root___eval_stl(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_stl\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1ULL & vlSelfRef.__VstlTriggered[0U])) {
        Vtop___024root___ico_sequent__TOP__0(vlSelf);
    }
}

VL_ATTR_COLD bool Vtop___024root___eval_phase__stl(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__stl\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    CData/*0:0*/ __VstlExecute;
    // Body
    Vtop___024root___eval_triggers__stl(vlSelf);
    __VstlExecute = Vtop___024root___trigger_anySet__stl(vlSelfRef.__VstlTriggered);
    if (__VstlExecute) {
        Vtop___024root___eval_stl(vlSelf);
    }
    return (__VstlExecute);
}

bool Vtop___024root___trigger_anySet__ico(const VlUnpacked<QData/*63:0*/, 1> &in);

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__ico(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__ico\n"); );
    // Body
    if ((1U & (~ (IData)(Vtop___024root___trigger_anySet__ico(triggers))))) {
        VL_DBG_MSGS("         No '" + tag + "' region triggers active\n");
    }
    if ((1U & (IData)(triggers[0U]))) {
        VL_DBG_MSGS("         '" + tag + "' region trigger index 0 is active: Internal 'ico' trigger - first iteration\n");
    }
}
#endif  // VL_DEBUG

VL_ATTR_COLD void Vtop___024root___ctor_var_reset(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___ctor_var_reset\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    const uint64_t __VscopeHash = VL_MURMUR64_HASH(vlSelf->name());
    vlSelf->SWT = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 16678451825093030839ull);
    vlSelf->SEG = VL_SCOPED_RAND_RESET_I(7, __VscopeHash, 2544303410019809036ull);
    vlSelf->AN = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 14238768244946913466ull);
    vlSelf->aoi_2_2__DOT__SWT = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 12113632791694450857ull);
    vlSelf->aoi_2_2__DOT__SEG = VL_SCOPED_RAND_RESET_I(7, __VscopeHash, 1288124393903389816ull);
    vlSelf->aoi_2_2__DOT__AN = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 6336851369041058640ull);
    vlSelf->aoi_2_2__DOT__a = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 519507504862108382ull);
    vlSelf->aoi_2_2__DOT__b = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 12808586680594682913ull);
    vlSelf->aoi_2_2__DOT__c = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 12450139974590320050ull);
    vlSelf->aoi_2_2__DOT__d = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 14895019667812905702ull);
    vlSelf->aoi_2_2__DOT__y = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 1945051175022035624ull);
    vlSelf->aoi_2_2__DOT____Vtogcov__SWT = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 15267302690535654743ull);
    vlSelf->aoi_2_2__DOT____Vtogcov__SEG = VL_SCOPED_RAND_RESET_I(7, __VscopeHash, 2924043641757549427ull);
    vlSelf->aoi_2_2__DOT____Vtogcov__AN = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 6627243854938772570ull);
    vlSelf->aoi_2_2__DOT____Vtogcov__a = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 5693154549955341958ull);
    vlSelf->aoi_2_2__DOT____Vtogcov__b = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 14173954129625884914ull);
    vlSelf->aoi_2_2__DOT____Vtogcov__c = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 10354509364715955832ull);
    vlSelf->aoi_2_2__DOT____Vtogcov__d = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 3741438965592067565ull);
    vlSelf->aoi_2_2__DOT____Vtogcov__y = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 16512668756572919506ull);
    for (int __Vi0 = 0; __Vi0 < 1; ++__Vi0) {
        vlSelf->__VstlTriggered[__Vi0] = 0;
    }
    for (int __Vi0 = 0; __Vi0 < 1; ++__Vi0) {
        vlSelf->__VicoTriggered[__Vi0] = 0;
    }
}

VL_ATTR_COLD void Vtop___024root___configure_coverage(Vtop___024root* vlSelf, bool first) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___configure_coverage\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    (void)first;  // Prevent unused variable warning
    vlSelf->__vlCoverToggleInsert(0, 3, 1, &(vlSymsp->__Vcoverage[0]), first, "/home/stephan/Git/pyuvm/examples/aoi_2_2/hdl/verilog/aoi_2_2.v", 7, 23, ".aoi_2_2", "v_toggle/aoi_2_2", "SWT");
    vlSelf->__vlCoverToggleInsert(0, 6, 1, &(vlSymsp->__Vcoverage[8]), first, "/home/stephan/Git/pyuvm/examples/aoi_2_2/hdl/verilog/aoi_2_2.v", 8, 23, ".aoi_2_2", "v_toggle/aoi_2_2", "SEG");
    vlSelf->__vlCoverToggleInsert(0, 3, 1, &(vlSymsp->__Vcoverage[22]), first, "/home/stephan/Git/pyuvm/examples/aoi_2_2/hdl/verilog/aoi_2_2.v", 9, 23, ".aoi_2_2", "v_toggle/aoi_2_2", "AN");
    vlSelf->__vlCoverToggleInsert(0, 0, 0, &(vlSymsp->__Vcoverage[30]), first, "/home/stephan/Git/pyuvm/examples/aoi_2_2/hdl/verilog/aoi_2_2.v", 13, 10, ".aoi_2_2", "v_toggle/aoi_2_2", "a");
    vlSelf->__vlCoverToggleInsert(0, 0, 0, &(vlSymsp->__Vcoverage[32]), first, "/home/stephan/Git/pyuvm/examples/aoi_2_2/hdl/verilog/aoi_2_2.v", 13, 13, ".aoi_2_2", "v_toggle/aoi_2_2", "b");
    vlSelf->__vlCoverToggleInsert(0, 0, 0, &(vlSymsp->__Vcoverage[34]), first, "/home/stephan/Git/pyuvm/examples/aoi_2_2/hdl/verilog/aoi_2_2.v", 13, 16, ".aoi_2_2", "v_toggle/aoi_2_2", "c");
    vlSelf->__vlCoverToggleInsert(0, 0, 0, &(vlSymsp->__Vcoverage[36]), first, "/home/stephan/Git/pyuvm/examples/aoi_2_2/hdl/verilog/aoi_2_2.v", 13, 19, ".aoi_2_2", "v_toggle/aoi_2_2", "d");
    vlSelf->__vlCoverToggleInsert(0, 0, 0, &(vlSymsp->__Vcoverage[38]), first, "/home/stephan/Git/pyuvm/examples/aoi_2_2/hdl/verilog/aoi_2_2.v", 14, 10, ".aoi_2_2", "v_toggle/aoi_2_2", "y");
    vlSelf->__vlCoverInsert(&(vlSymsp->__Vcoverage[40]), first, "/home/stephan/Git/pyuvm/examples/aoi_2_2/hdl/verilog/aoi_2_2.v", 32, 32, ".aoi_2_2", "v_branch/aoi_2_2", "cond_then", "32");
    vlSelf->__vlCoverInsert(&(vlSymsp->__Vcoverage[41]), first, "/home/stephan/Git/pyuvm/examples/aoi_2_2/hdl/verilog/aoi_2_2.v", 32, 33, ".aoi_2_2", "v_branch/aoi_2_2", "cond_else", "32");
}
