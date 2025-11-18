// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop.h for the primary calling header

#include "Vtop__pch.h"

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__ico(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag);
#endif  // VL_DEBUG

void Vtop___024root___eval_triggers__ico(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_triggers__ico\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__VicoTriggered[0U] = ((0xfffffffffffffffeULL 
                                      & vlSelfRef.__VicoTriggered
                                      [0U]) | (IData)((IData)(vlSelfRef.__VicoFirstIteration)));
    vlSelfRef.__VicoFirstIteration = 0U;
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vtop___024root___dump_triggers__ico(vlSelfRef.__VicoTriggered, "ico"s);
    }
#endif
}

bool Vtop___024root___trigger_anySet__ico(const VlUnpacked<QData/*63:0*/, 1> &in) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___trigger_anySet__ico\n"); );
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

void Vtop___024root___ico_sequent__TOP__0(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___ico_sequent__TOP__0\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if (((IData)(vlSelfRef.aoi_2_2__DOT__AN) ^ (IData)(vlSelfRef.aoi_2_2__DOT____Vtogcov__AN))) {
        VL_COV_TOGGLE_CHG_ST_I(4, vlSymsp->__Vcoverage + 22, vlSelfRef.aoi_2_2__DOT__AN, vlSelfRef.aoi_2_2__DOT____Vtogcov__AN);
        vlSelfRef.aoi_2_2__DOT____Vtogcov__AN = vlSelfRef.aoi_2_2__DOT__AN;
    }
    vlSelfRef.AN = vlSelfRef.aoi_2_2__DOT__AN;
    vlSelfRef.aoi_2_2__DOT__SWT = vlSelfRef.SWT;
    if (((IData)(vlSelfRef.aoi_2_2__DOT__SWT) ^ (IData)(vlSelfRef.aoi_2_2__DOT____Vtogcov__SWT))) {
        VL_COV_TOGGLE_CHG_ST_I(4, vlSymsp->__Vcoverage + 0, vlSelfRef.aoi_2_2__DOT__SWT, vlSelfRef.aoi_2_2__DOT____Vtogcov__SWT);
        vlSelfRef.aoi_2_2__DOT____Vtogcov__SWT = vlSelfRef.aoi_2_2__DOT__SWT;
    }
    vlSelfRef.aoi_2_2__DOT__a = (1U & (IData)(vlSelfRef.aoi_2_2__DOT__SWT));
    vlSelfRef.aoi_2_2__DOT__b = (1U & ((IData)(vlSelfRef.aoi_2_2__DOT__SWT) 
                                       >> 1U));
    vlSelfRef.aoi_2_2__DOT__c = (1U & ((IData)(vlSelfRef.aoi_2_2__DOT__SWT) 
                                       >> 2U));
    vlSelfRef.aoi_2_2__DOT__d = (1U & ((IData)(vlSelfRef.aoi_2_2__DOT__SWT) 
                                       >> 3U));
    if (((IData)(vlSelfRef.aoi_2_2__DOT__a) ^ (IData)(vlSelfRef.aoi_2_2__DOT____Vtogcov__a))) {
        VL_COV_TOGGLE_CHG_ST_I(1, vlSymsp->__Vcoverage + 30, vlSelfRef.aoi_2_2__DOT__a, vlSelfRef.aoi_2_2__DOT____Vtogcov__a);
        vlSelfRef.aoi_2_2__DOT____Vtogcov__a = vlSelfRef.aoi_2_2__DOT__a;
    }
    if (((IData)(vlSelfRef.aoi_2_2__DOT__b) ^ (IData)(vlSelfRef.aoi_2_2__DOT____Vtogcov__b))) {
        VL_COV_TOGGLE_CHG_ST_I(1, vlSymsp->__Vcoverage + 32, vlSelfRef.aoi_2_2__DOT__b, vlSelfRef.aoi_2_2__DOT____Vtogcov__b);
        vlSelfRef.aoi_2_2__DOT____Vtogcov__b = vlSelfRef.aoi_2_2__DOT__b;
    }
    if (((IData)(vlSelfRef.aoi_2_2__DOT__c) ^ (IData)(vlSelfRef.aoi_2_2__DOT____Vtogcov__c))) {
        VL_COV_TOGGLE_CHG_ST_I(1, vlSymsp->__Vcoverage + 34, vlSelfRef.aoi_2_2__DOT__c, vlSelfRef.aoi_2_2__DOT____Vtogcov__c);
        vlSelfRef.aoi_2_2__DOT____Vtogcov__c = vlSelfRef.aoi_2_2__DOT__c;
    }
    if (((IData)(vlSelfRef.aoi_2_2__DOT__d) ^ (IData)(vlSelfRef.aoi_2_2__DOT____Vtogcov__d))) {
        VL_COV_TOGGLE_CHG_ST_I(1, vlSymsp->__Vcoverage + 36, vlSelfRef.aoi_2_2__DOT__d, vlSelfRef.aoi_2_2__DOT____Vtogcov__d);
        vlSelfRef.aoi_2_2__DOT____Vtogcov__d = vlSelfRef.aoi_2_2__DOT__d;
    }
    vlSelfRef.aoi_2_2__DOT__y = (1U & (~ (((IData)(vlSelfRef.aoi_2_2__DOT__a) 
                                           & (IData)(vlSelfRef.aoi_2_2__DOT__b)) 
                                          | ((IData)(vlSelfRef.aoi_2_2__DOT__c) 
                                             & (IData)(vlSelfRef.aoi_2_2__DOT__d)))));
    if (((IData)(vlSelfRef.aoi_2_2__DOT__y) ^ (IData)(vlSelfRef.aoi_2_2__DOT____Vtogcov__y))) {
        VL_COV_TOGGLE_CHG_ST_I(1, vlSymsp->__Vcoverage + 38, vlSelfRef.aoi_2_2__DOT__y, vlSelfRef.aoi_2_2__DOT____Vtogcov__y);
        vlSelfRef.aoi_2_2__DOT____Vtogcov__y = vlSelfRef.aoi_2_2__DOT__y;
    }
    vlSelfRef.aoi_2_2__DOT__SEG = ((IData)(vlSelfRef.aoi_2_2__DOT__y)
                                    ? ([&]() {
                ++(vlSymsp->__Vcoverage[41]);
            }(), 0x79U) : ([&]() {
                ++(vlSymsp->__Vcoverage[40]);
            }(), 0x40U));
    if (((IData)(vlSelfRef.aoi_2_2__DOT__SEG) ^ (IData)(vlSelfRef.aoi_2_2__DOT____Vtogcov__SEG))) {
        VL_COV_TOGGLE_CHG_ST_I(7, vlSymsp->__Vcoverage + 8, vlSelfRef.aoi_2_2__DOT__SEG, vlSelfRef.aoi_2_2__DOT____Vtogcov__SEG);
        vlSelfRef.aoi_2_2__DOT____Vtogcov__SEG = vlSelfRef.aoi_2_2__DOT__SEG;
    }
    vlSelfRef.SEG = vlSelfRef.aoi_2_2__DOT__SEG;
}

void Vtop___024root___eval_ico(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_ico\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1ULL & vlSelfRef.__VicoTriggered[0U])) {
        Vtop___024root___ico_sequent__TOP__0(vlSelf);
    }
}

bool Vtop___024root___eval_phase__ico(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__ico\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    CData/*0:0*/ __VicoExecute;
    // Body
    Vtop___024root___eval_triggers__ico(vlSelf);
    __VicoExecute = Vtop___024root___trigger_anySet__ico(vlSelfRef.__VicoTriggered);
    if (__VicoExecute) {
        Vtop___024root___eval_ico(vlSelf);
    }
    return (__VicoExecute);
}

void Vtop___024root___eval(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    IData/*31:0*/ __VicoIterCount;
    // Body
    __VicoIterCount = 0U;
    vlSelfRef.__VicoFirstIteration = 1U;
    do {
        if (VL_UNLIKELY(((0x00000064U < __VicoIterCount)))) {
#ifdef VL_DEBUG
            Vtop___024root___dump_triggers__ico(vlSelfRef.__VicoTriggered, "ico"s);
#endif
            VL_FATAL_MT("/home/stephan/Git/pyuvm/examples/aoi_2_2/hdl/verilog/aoi_2_2.v", 6, "", "Input combinational region did not converge after 100 tries");
        }
        __VicoIterCount = ((IData)(1U) + __VicoIterCount);
    } while (Vtop___024root___eval_phase__ico(vlSelf));
}

#ifdef VL_DEBUG
void Vtop___024root___eval_debug_assertions(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_debug_assertions\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if (VL_UNLIKELY(((vlSelfRef.SWT & 0xf0U)))) {
        Verilated::overWidthError("SWT");
    }
}
#endif  // VL_DEBUG
