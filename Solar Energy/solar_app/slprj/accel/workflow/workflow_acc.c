#include "__cf_workflow.h"
#include <math.h>
#include "workflow_acc.h"
#include "workflow_acc_private.h"
#include <stdio.h>
#include "simstruc.h"
#include "fixedpoint.h"
#define CodeFormat S-Function
#define AccDefine1 Accelerator_S-Function
static void mdlOutputs ( SimStruct * S , int_T tid ) { pj1hxgqr3r * _rtB ;
ct14qrwcfg * _rtP ; fe1tfeejxv * _rtDW ; _rtDW = ( ( fe1tfeejxv * )
ssGetRootDWork ( S ) ) ; _rtP = ( ( ct14qrwcfg * ) ssGetDefaultParam ( S ) )
; _rtB = ( ( pj1hxgqr3r * ) _ssGetBlockIO ( S ) ) ; ssCallAccelRunBlock ( S ,
10 , 0 , SS_CALL_MDL_OUTPUTS ) ; _rtB -> j0hwyzjrzn = ( ( pgg24noyu1 * )
ssGetContStates ( S ) ) -> mmmqjhroid ; ssCallAccelRunBlock ( S , 9 , 0 ,
SS_CALL_MDL_OUTPUTS ) ; _rtB -> iikz0nwncq = ( ( pgg24noyu1 * )
ssGetContStates ( S ) ) -> dzg3chnv54 ; ssCallAccelRunBlock ( S , 13 , 4 ,
SS_CALL_MDL_OUTPUTS ) ; ssCallAccelRunBlock ( S , 0 , 0 , SS_CALL_MDL_OUTPUTS
) ; ssCallAccelRunBlock ( S , 7 , 0 , SS_CALL_MDL_OUTPUTS ) ; if (
ssIsSampleHit ( S , 1 , 0 ) ) { memcpy ( & _rtB -> ew3ppaa3so [ 0 ] , & _rtP
-> P_2 [ 0 ] , 9U * sizeof ( real_T ) ) ; } ssCallAccelRunBlock ( S , 1 , 0 ,
SS_CALL_MDL_OUTPUTS ) ; _rtB -> ojqll2lge4 = ( ( pgg24noyu1 * )
ssGetContStates ( S ) ) -> o2zkh0bgb4 ; ssCallAccelRunBlock ( S , 5 , 0 ,
SS_CALL_MDL_OUTPUTS ) ; ssCallAccelRunBlock ( S , 8 , 0 , SS_CALL_MDL_OUTPUTS
) ; ssCallAccelRunBlock ( S , 3 , 0 , SS_CALL_MDL_OUTPUTS ) ;
ssCallAccelRunBlock ( S , 13 , 13 , SS_CALL_MDL_OUTPUTS ) ; if (
ssIsSampleHit ( S , 1 , 0 ) ) { ssCallAccelRunBlock ( S , 6 , 0 ,
SS_CALL_MDL_OUTPUTS ) ; } ssCallAccelRunBlock ( S , 12 , 0 ,
SS_CALL_MDL_OUTPUTS ) ; _rtB -> cg0jdqxzkr = _rtB -> fmaqezvviz + _rtB ->
ojqll2lge4 ; ssCallAccelRunBlock ( S , 13 , 17 , SS_CALL_MDL_OUTPUTS ) ; if (
ssIsSampleHit ( S , 1 , 0 ) ) { _rtB -> pcnrlbwlmq = _rtP -> P_4 ; _rtB ->
mumhp1sxph = _rtP -> P_5 ; } ssCallAccelRunBlock ( S , 4 , 0 ,
SS_CALL_MDL_OUTPUTS ) ; ssCallAccelRunBlock ( S , 2 , 0 , SS_CALL_MDL_OUTPUTS
) ; ssCallAccelRunBlock ( S , 11 , 0 , SS_CALL_MDL_OUTPUTS ) ;
UNUSED_PARAMETER ( tid ) ; }
#define MDL_UPDATE
static void mdlUpdate ( SimStruct * S , int_T tid ) { pj1hxgqr3r * _rtB ;
ct14qrwcfg * _rtP ; _rtP = ( ( ct14qrwcfg * ) ssGetDefaultParam ( S ) ) ;
_rtB = ( ( pj1hxgqr3r * ) _ssGetBlockIO ( S ) ) ; UNUSED_PARAMETER ( tid ) ;
}
#define MDL_DERIVATIVES
static void mdlDerivatives ( SimStruct * S ) { pj1hxgqr3r * _rtB ; ct14qrwcfg
* _rtP ; _rtP = ( ( ct14qrwcfg * ) ssGetDefaultParam ( S ) ) ; _rtB = ( (
pj1hxgqr3r * ) _ssGetBlockIO ( S ) ) ; { ( ( p5pqypeu0u * ) ssGetdX ( S ) )
-> mmmqjhroid = _rtB -> pcnrlbwlmq ; } { ( ( p5pqypeu0u * ) ssGetdX ( S ) )
-> dzg3chnv54 = _rtB -> p4yv2losp5 ; } { ( ( p5pqypeu0u * ) ssGetdX ( S ) )
-> o2zkh0bgb4 = _rtB -> mlktttvypj ; } } static void mdlInitializeSizes (
SimStruct * S ) { ssSetChecksumVal ( S , 0 , 1043118664U ) ; ssSetChecksumVal
( S , 1 , 1540327912U ) ; ssSetChecksumVal ( S , 2 , 3856585039U ) ;
ssSetChecksumVal ( S , 3 , 1863063196U ) ; { mxArray * slVerStructMat = NULL
; mxArray * slStrMat = mxCreateString ( "simulink" ) ; char slVerChar [ 10 ]
; int status = mexCallMATLAB ( 1 , & slVerStructMat , 1 , & slStrMat , "ver"
) ; if ( status == 0 ) { mxArray * slVerMat = mxGetField ( slVerStructMat , 0
, "Version" ) ; if ( slVerMat == NULL ) { status = 1 ; } else { status =
mxGetString ( slVerMat , slVerChar , 10 ) ; } } mxDestroyArray ( slStrMat ) ;
mxDestroyArray ( slVerStructMat ) ; if ( ( status == 1 ) || ( strcmp (
slVerChar , "8.5" ) != 0 ) ) { return ; } } ssSetOptions ( S ,
SS_OPTION_EXCEPTION_FREE_CODE ) ; if ( ssGetSizeofDWork ( S ) != sizeof (
fe1tfeejxv ) ) { ssSetErrorStatus ( S ,
"Unexpected error: Internal DWork sizes do "
"not match for accelerator mex file." ) ; } if ( ssGetSizeofGlobalBlockIO ( S
) != sizeof ( pj1hxgqr3r ) ) { ssSetErrorStatus ( S ,
"Unexpected error: Internal BlockIO sizes do "
"not match for accelerator mex file." ) ; } { int ssSizeofParams ;
ssGetSizeofParams ( S , & ssSizeofParams ) ; if ( ssSizeofParams != sizeof (
ct14qrwcfg ) ) { static char msg [ 256 ] ; sprintf ( msg ,
"Unexpected error: Internal Parameters sizes do "
"not match for accelerator mex file." ) ; } } _ssSetDefaultParam ( S , (
real_T * ) & i51duhx0p5 ) ; rt_InitInfAndNaN ( sizeof ( real_T ) ) ; } static
void mdlInitializeSampleTimes ( SimStruct * S ) { { SimStruct * childS ;
SysOutputFcn * callSysFcns ; childS = ssGetSFunction ( S , 0 ) ; callSysFcns
= ssGetCallSystemOutputFcnList ( childS ) ; callSysFcns [ 3 + 0 ] = (
SysOutputFcn ) ( NULL ) ; childS = ssGetSFunction ( S , 1 ) ; callSysFcns =
ssGetCallSystemOutputFcnList ( childS ) ; callSysFcns [ 3 + 0 ] = (
SysOutputFcn ) ( NULL ) ; childS = ssGetSFunction ( S , 2 ) ; callSysFcns =
ssGetCallSystemOutputFcnList ( childS ) ; callSysFcns [ 3 + 0 ] = (
SysOutputFcn ) ( NULL ) ; childS = ssGetSFunction ( S , 3 ) ; callSysFcns =
ssGetCallSystemOutputFcnList ( childS ) ; callSysFcns [ 3 + 0 ] = (
SysOutputFcn ) ( NULL ) ; childS = ssGetSFunction ( S , 4 ) ; callSysFcns =
ssGetCallSystemOutputFcnList ( childS ) ; callSysFcns [ 3 + 0 ] = (
SysOutputFcn ) ( NULL ) ; childS = ssGetSFunction ( S , 5 ) ; callSysFcns =
ssGetCallSystemOutputFcnList ( childS ) ; callSysFcns [ 3 + 0 ] = (
SysOutputFcn ) ( NULL ) ; childS = ssGetSFunction ( S , 6 ) ; callSysFcns =
ssGetCallSystemOutputFcnList ( childS ) ; callSysFcns [ 3 + 0 ] = (
SysOutputFcn ) ( NULL ) ; childS = ssGetSFunction ( S , 7 ) ; callSysFcns =
ssGetCallSystemOutputFcnList ( childS ) ; callSysFcns [ 3 + 0 ] = (
SysOutputFcn ) ( NULL ) ; childS = ssGetSFunction ( S , 8 ) ; callSysFcns =
ssGetCallSystemOutputFcnList ( childS ) ; callSysFcns [ 3 + 0 ] = (
SysOutputFcn ) ( NULL ) ; childS = ssGetSFunction ( S , 9 ) ; callSysFcns =
ssGetCallSystemOutputFcnList ( childS ) ; callSysFcns [ 3 + 0 ] = (
SysOutputFcn ) ( NULL ) ; childS = ssGetSFunction ( S , 10 ) ; callSysFcns =
ssGetCallSystemOutputFcnList ( childS ) ; callSysFcns [ 3 + 0 ] = (
SysOutputFcn ) ( NULL ) ; childS = ssGetSFunction ( S , 11 ) ; callSysFcns =
ssGetCallSystemOutputFcnList ( childS ) ; callSysFcns [ 3 + 0 ] = (
SysOutputFcn ) ( NULL ) ; childS = ssGetSFunction ( S , 12 ) ; callSysFcns =
ssGetCallSystemOutputFcnList ( childS ) ; callSysFcns [ 3 + 0 ] = (
SysOutputFcn ) ( NULL ) ; } } static void mdlTerminate ( SimStruct * S ) { }
#include "simulink.c"
