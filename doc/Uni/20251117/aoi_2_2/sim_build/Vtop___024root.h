// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design internal header
// See Vtop.h for the primary calling header

#ifndef VERILATED_VTOP___024ROOT_H_
#define VERILATED_VTOP___024ROOT_H_  // guard

#include "verilated.h"
#include "verilated_cov.h"


class Vtop__Syms;

class alignas(VL_CACHE_LINE_BYTES) Vtop___024root final : public VerilatedModule {
  public:

    // DESIGN SPECIFIC STATE
    VL_IN8(SWT,3,0);
    VL_OUT8(SEG,6,0);
    VL_OUT8(AN,3,0);
    CData/*3:0*/ aoi_2_2__DOT__SWT;
    CData/*6:0*/ aoi_2_2__DOT__SEG;
    CData/*3:0*/ aoi_2_2__DOT__AN;
    CData/*0:0*/ aoi_2_2__DOT__a;
    CData/*0:0*/ aoi_2_2__DOT__b;
    CData/*0:0*/ aoi_2_2__DOT__c;
    CData/*0:0*/ aoi_2_2__DOT__d;
    CData/*0:0*/ aoi_2_2__DOT__y;
    CData/*3:0*/ aoi_2_2__DOT____Vtogcov__SWT;
    CData/*6:0*/ aoi_2_2__DOT____Vtogcov__SEG;
    CData/*3:0*/ aoi_2_2__DOT____Vtogcov__AN;
    CData/*0:0*/ aoi_2_2__DOT____Vtogcov__a;
    CData/*0:0*/ aoi_2_2__DOT____Vtogcov__b;
    CData/*0:0*/ aoi_2_2__DOT____Vtogcov__c;
    CData/*0:0*/ aoi_2_2__DOT____Vtogcov__d;
    CData/*0:0*/ aoi_2_2__DOT____Vtogcov__y;
    CData/*0:0*/ __VstlFirstIteration;
    CData/*0:0*/ __VicoFirstIteration;
    VlUnpacked<QData/*63:0*/, 1> __VstlTriggered;
    VlUnpacked<QData/*63:0*/, 1> __VicoTriggered;

    // INTERNAL VARIABLES
    Vtop__Syms* const vlSymsp;

    // CONSTRUCTORS
    Vtop___024root(Vtop__Syms* symsp, const char* v__name);
    ~Vtop___024root();
    VL_UNCOPYABLE(Vtop___024root);

    // INTERNAL METHODS
    void __Vconfigure(bool first);
    void __vlCoverInsert(uint32_t* countp, bool enable, const char* filenamep, int lineno, int column,
        const char* hierp, const char* pagep, const char* commentp, const char* linescovp);
    void __vlCoverToggleInsert(int begin, int end, bool ranged, uint32_t* countp, bool enable, const char* filenamep, int lineno, int column,
        const char* hierp, const char* pagep, const char* commentp);
};


#endif  // guard
