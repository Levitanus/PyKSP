from k_built_ins import message
from k_built_ins import exit
from k_built_ins import reset_ksp_timer
from k_built_ins import ignore_controller
from k_built_ins import exp
from k_built_ins import log
from k_built_ins import kpow
from k_built_ins import sqrt
from k_built_ins import ceil
from k_built_ins import floor
from k_built_ins import kround
from k_built_ins import cos
from k_built_ins import sin
from k_built_ins import tan
from k_built_ins import acos
from k_built_ins import asin
from k_built_ins import atan
from k_built_ins import NI_CALLBACK_ID
from k_built_ins import NI_CALLBACK_TYPE
from k_built_ins import NI_CB_TYPE_ASYNC_OUT
from k_built_ins import NI_CB_TYPE_CONTROLLER
from k_built_ins import NI_CB_TYPE_INIT
from k_built_ins import NI_CB_TYPE_LISTENER
from k_built_ins import NI_CB_TYPE_NOTE
from k_built_ins import NI_CB_TYPE_PERSISTENCE_CHANGED
from k_built_ins import NI_CB_TYPE_PGS
from k_built_ins import NI_CB_TYPE_POLY_AT
from k_built_ins import NI_CB_TYPE_RELEASE
from k_built_ins import NI_CB_TYPE_RPN
from k_built_ins import NI_CB_TYPE_NRPN
from k_built_ins import NI_CB_TYPE_UI_CONTROL
from k_built_ins import NI_CB_TYPE_UI_UPDATE
from k_built_ins import NI_CB_TYPE_MIDI_IN
from k_built_ins import CURRENT_SCRIPT_SLOT
from k_built_ins import GROUPS_SELECTED
from k_built_ins import NI_ASYNC_EXIT_STATUS
from k_built_ins import NI_ASYNC_ID
from k_built_ins import NI_BUS_OFFSET
from k_built_ins import NUM_GROUPS
from k_built_ins import NUM_OUTPUT_CHANNELS
from k_built_ins import NUM_ZONES
from k_built_ins import PLAYED_VOICES_INST
from k_built_ins import PLAYED_VOICES_TOTAL
from k_built_ins import GET_FOLDER_LIBRARY_DIR
from k_built_ins import GET_FOLDER_FACTORY_DIR
from k_built_ins import GET_FOLDER_PATCH_DIR
from k_built_ins import NI_VL_TMPRO_STANDARD
from k_built_ins import NI_VL_TMRPO_HQ
from k_built_ins import REF_GROUP_IDX
from k_built_ins import ALL_GROUPS
from k_built_ins import ALL_EVENTS
from k_built_ins import KEY_DOWN
from k_built_ins import KEY_DOWN_OCT
from k_built_ins import DISTANCE_BAR_START
from k_built_ins import DURATION_BAR
from k_built_ins import DURATION_QUARTER
from k_built_ins import DURATION_EIGHTH
from k_built_ins import DURATION_SIXTEENTH
from k_built_ins import DURATION_QUARTER_TRIPLET
from k_built_ins import DURATION_EIGHTH_TRIPLET
from k_built_ins import DURATION_SIXTEENTH_TRIPLET
from k_built_ins import ENGINE_UPTIME
from k_built_ins import KSP_TIMER
from k_built_ins import NI_SONG_POSITION
from k_built_ins import NI_TRANSPORT_RUNNING
from k_built_ins import SIGNATURE_NUM
from k_built_ins import SIGNATURE_DENOM
from k_built_ins import NI_SYNC_UNIT_ABS
from k_built_ins import NI_SYNC_UNIT_WHOLE
from k_built_ins import NI_SYNC_UNIT_WHOLE_TRIPLET
from k_built_ins import NI_SYNC_UNIT_HALF
from k_built_ins import NI_SYNC_UNIT_HALF_TRIPLET
from k_built_ins import NI_SYNC_UNIT_QUARTER
from k_built_ins import NI_SYNC_UNIT_QUARTER_TRIPLET
from k_built_ins import NI_SYNC_UNIT_8TH
from k_built_ins import NI_SYNC_UNIT_8TH_TRIPLET
from k_built_ins import NI_SYNC_UNIT_16TH
from k_built_ins import NI_SYNC_UNIT_16TH_TRIPLET
from k_built_ins import NI_SYNC_UNIT_32ND
from k_built_ins import NI_SYNC_UNIT_32ND_TRIPLET
from k_built_ins import NI_SYNC_UNIT_64TH
from k_built_ins import NI_SYNC_UNIT_64TH_TRIPLET
from k_built_ins import NI_SYNC_UNIT_256TH
from k_built_ins import NI_SYNC_UNIT_ZONE
from k_built_ins import NOTE_DURATION
from k_built_ins import NI_SIGNAL_TRANSP_STOP
from k_built_ins import NI_SIGNAL_TRANSP_START
from k_built_ins import NI_SIGNAL_TIMER_MS
from k_built_ins import NI_SIGNAL_TIMER_BEAT
from k_built_ins import NI_SIGNAL_TYPE
from k_built_ins import NI_MATH_PI
from k_built_ins import NI_MATH_E
from bi_engine_par import ENGINE_PAR_VOLUME
from bi_engine_par import ENGINE_PAR_PAN
from bi_engine_par import ENGINE_PAR_TUNE
from bi_engine_par import ENGINE_PAR_SMOOTH
from bi_engine_par import ENGINE_PAR_FORMANT
from bi_engine_par import ENGINE_PAR_SPEED
from bi_engine_par import ENGINE_PAR_GRAIN_LENGTH
from bi_engine_par import ENGINE_PAR_SLICE_ATTACK
from bi_engine_par import ENGINE_PAR_SLICE_RELEASE
from bi_engine_par import ENGINE_PAR_TRANSIENT_SIZE
from bi_engine_par import ENGINE_PAR_ENVELOPE_ORDER
from bi_engine_par import ENGINE_PAR_FORMANT_SHIFT
from bi_engine_par import ENGINE_PAR_SPEED_UNIT
from bi_engine_par import ENGINE_PAR_OUTPUT_CHANNEL
from bi_engine_par import NI_BUS_OFFSET
from bi_engine_par import ENGINE_PAR_EFFECT_BYPASS
from bi_engine_par import ENGINE_PAR_INSERT_EFFECT_OUTPUT_GAIN
from bi_engine_par import ENGINE_PAR_RELEASE_TRIGGER
from bi_engine_par import ENGINE_PAR_THRESHOLD
from bi_engine_par import ENGINE_PAR_RATIO
from bi_engine_par import ENGINE_PAR_COMP_ATTACK
from bi_engine_par import ENGINE_PAR_COMP_DECAY
from bi_engine_par import ENGINE_PAR_LIM_IN_GAIN
from bi_engine_par import ENGINE_PAR_LIM_RELEASE
from bi_engine_par import ENGINE_PAR_SP_OFFSET_DISTANCE
from bi_engine_par import ENGINE_PAR_SP_OFFSET_AZIMUTH
from bi_engine_par import ENGINE_PAR_SP_OFFSET_X
from bi_engine_par import ENGINE_PAR_SP_OFFSET_Y
from bi_engine_par import ENGINE_PAR_SP_LFE_VOLUME
from bi_engine_par import ENGINE_PAR_SP_SIZE
from bi_engine_par import ENGINE_PAR_SP_DIVERGENCE
from bi_engine_par import ENGINE_PAR_SHAPE
from bi_engine_par import ENGINE_PAR_BITS
from bi_engine_par import ENGINE_PAR_FREQUENCY
from bi_engine_par import ENGINE_PAR_NOISELEVEL
from bi_engine_par import ENGINE_PAR_NOISECOLOR
from bi_engine_par import ENGINE_PAR_STEREO
from bi_engine_par import ENGINE_PAR_STEREO_PAN
from bi_engine_par import ENGINE_PAR_DRIVE
from bi_engine_par import ENGINE_PAR_DAMPING
from bi_engine_par import ENGINE_PAR_SENDLEVEL_0
from bi_engine_par import ENGINE_PAR_SENDLEVEL_1
from bi_engine_par import ENGINE_PAR_SENDLEVEL_2
from bi_engine_par import ENGINE_PAR_SENDLEVEL_3
from bi_engine_par import ENGINE_PAR_SENDLEVEL_4
from bi_engine_par import ENGINE_PAR_SENDLEVEL_5
from bi_engine_par import ENGINE_PAR_SENDLEVEL_6
from bi_engine_par import ENGINE_PAR_SENDLEVEL_7
from bi_engine_par import ENGINE_PAR_SK_TONE
from bi_engine_par import ENGINE_PAR_SK_DRIVE
from bi_engine_par import ENGINE_PAR_SK_BASS
from bi_engine_par import ENGINE_PAR_SK_BRIGHT
from bi_engine_par import ENGINE_PAR_SK_MIX
from bi_engine_par import ENGINE_PAR_RT_SPEED
from bi_engine_par import ENGINE_PAR_RT_BALANCE
from bi_engine_par import ENGINE_PAR_RT_ACCEL_HI
from bi_engine_par import ENGINE_PAR_RT_ACCEL_LO
from bi_engine_par import ENGINE_PAR_RT_DISTANCE
from bi_engine_par import ENGINE_PAR_RT_MIX
from bi_engine_par import ENGINE_PAR_TW_VOLUME
from bi_engine_par import ENGINE_PAR_TW_TREBLE
from bi_engine_par import ENGINE_PAR_TW_MID
from bi_engine_par import ENGINE_PAR_TW_BASS
from bi_engine_par import ENGINE_PAR_TW_BRIGHT
from bi_engine_par import ENGINE_PAR_TW_MONO
from bi_engine_par import ENGINE_PAR_CB_SIZE
from bi_engine_par import ENGINE_PAR_CB_AIR
from bi_engine_par import ENGINE_PAR_CB_TREBLE
from bi_engine_par import ENGINE_PAR_CB_BASS
from bi_engine_par import ENGINE_PAR_CABINET_TYPE
from bi_engine_par import ENGINE_PAR_EXP_FILTER_MORPH
from bi_engine_par import ENGINE_PAR_EXP_FILTER_AMOUNT
from bi_engine_par import ENGINE_PAR_TP_GAIN
from bi_engine_par import ENGINE_PAR_TP_WARMTH
from bi_engine_par import ENGINE_PAR_TP_HF_ROLLOFF
from bi_engine_par import ENGINE_PAR_TP_QUALITY
from bi_engine_par import ENGINE_PAR_TR_INPUT
from bi_engine_par import ENGINE_PAR_TR_ATTACK
from bi_engine_par import ENGINE_PAR_TR_SUSTAIN
from bi_engine_par import ENGINE_PAR_TR_SMOOTH
from bi_engine_par import ENGINE_PAR_SCOMP_THRESHOLD
from bi_engine_par import ENGINE_PAR_SCOMP_RATIO
from bi_engine_par import ENGINE_PAR_SCOMP_ATTACK
from bi_engine_par import ENGINE_PAR_SCOMP_RELEASE
from bi_engine_par import ENGINE_PAR_SCOMP_MAKEUP
from bi_engine_par import ENGINE_PAR_SCOMP_MIX
from bi_engine_par import ENGINE_PAR_JMP_PREAMP
from bi_engine_par import ENGINE_PAR_JMP_BASS
from bi_engine_par import ENGINE_PAR_JMP_MID
from bi_engine_par import ENGINE_PAR_JMP_TREBLE
from bi_engine_par import ENGINE_PAR_JMP_MASTER
from bi_engine_par import ENGINE_PAR_JMP_PRESENCE
from bi_engine_par import ENGINE_PAR_JMP_HIGAIN
from bi_engine_par import ENGINE_PAR_JMP_MONO
from bi_engine_par import ENGINE_PAR_FCOMP_INPUT
from bi_engine_par import ENGINE_PAR_FCOMP_RATIO
from bi_engine_par import ENGINE_PAR_FCOMP_ATTACK
from bi_engine_par import ENGINE_PAR_FCOMP_RELEASE
from bi_engine_par import ENGINE_PAR_FCOMP_MAKEUP
from bi_engine_par import ENGINE_PAR_FCOMP_MIX
from bi_engine_par import ENGINE_PAR_FCOMP_HQ_MODE
from bi_engine_par import ENGINE_PAR_FCOMP_LINK
from bi_engine_par import ENGINE_PAR_AC_NORMALVOLUME
from bi_engine_par import ENGINE_PAR_AC_BRILLIANTVOLUME
from bi_engine_par import ENGINE_PAR_AC_BASS
from bi_engine_par import ENGINE_PAR_AC_TREBLE
from bi_engine_par import ENGINE_PAR_AC_TONECUT
from bi_engine_par import ENGINE_PAR_AC_TREMOLOSPEED
from bi_engine_par import ENGINE_PAR_AC_TREMOLODEPTH
from bi_engine_par import ENGINE_PAR_AC_MONO
from bi_engine_par import ENGINE_PAR_CT_VOLUME
from bi_engine_par import ENGINE_PAR_CT_DISTORTION
from bi_engine_par import ENGINE_PAR_CT_FILTER
from bi_engine_par import ENGINE_PAR_CT_BASS
from bi_engine_par import ENGINE_PAR_CT_BALLS
from bi_engine_par import ENGINE_PAR_CT_TREBLE
from bi_engine_par import ENGINE_PAR_CT_TONE
from bi_engine_par import ENGINE_PAR_CT_MONO
from bi_engine_par import ENGINE_PAR_DS_VOLUME
from bi_engine_par import ENGINE_PAR_DS_TONE
from bi_engine_par import ENGINE_PAR_DS_DRIVE
from bi_engine_par import ENGINE_PAR_DS_BASS
from bi_engine_par import ENGINE_PAR_DS_MID
from bi_engine_par import ENGINE_PAR_DS_TREBLE
from bi_engine_par import ENGINE_PAR_DS_MONO
from bi_engine_par import ENGINE_PAR_HS_PRENORMAL
from bi_engine_par import ENGINE_PAR_HS_PREOVERDRIVE
from bi_engine_par import ENGINE_PAR_HS_BASS
from bi_engine_par import ENGINE_PAR_HS_MID
from bi_engine_par import ENGINE_PAR_HS_TREBLE
from bi_engine_par import ENGINE_PAR_HS_MASTER
from bi_engine_par import ENGINE_PAR_HS_PRESENCE
from bi_engine_par import ENGINE_PAR_HS_DEPTH
from bi_engine_par import ENGINE_PAR_HS_OVERDRIVE
from bi_engine_par import ENGINE_PAR_HS_MONO
from bi_engine_par import ENGINE_PAR_V5_PREGAINRHYTHM
from bi_engine_par import ENGINE_PAR_V5_PREGAINLEAD
from bi_engine_par import ENGINE_PAR_V5_BASS
from bi_engine_par import ENGINE_PAR_V5_MID
from bi_engine_par import ENGINE_PAR_V5_TREBLE
from bi_engine_par import ENGINE_PAR_V5_POSTGAIN
from bi_engine_par import ENGINE_PAR_V5_RESONANCE
from bi_engine_par import ENGINE_PAR_V5_PRESENCE
from bi_engine_par import ENGINE_PAR_V5_LEADCHANNEL
from bi_engine_par import ENGINE_PAR_V5_HIGAIN
from bi_engine_par import ENGINE_PAR_V5_BRIGHT
from bi_engine_par import ENGINE_PAR_V5_CRUNCH
from bi_engine_par import ENGINE_PAR_V5_MONO
from bi_engine_par import ENGINE_PAR_CUTOFF
from bi_engine_par import ENGINE_PAR_RESONANCE
from bi_engine_par import ENGINE_PAR_EFFECT_BYPASS
from bi_engine_par import ENGINE_PAR_GAIN
from bi_engine_par import ENGINE_PAR_FILTER_LADDER_HQ
from bi_engine_par import ENGINE_PAR_BANDWIDTH
from bi_engine_par import ENGINE_PAR_FILTER_SHIFTB
from bi_engine_par import ENGINE_PAR_FILTER_SHIFTC
from bi_engine_par import ENGINE_PAR_FILTER_RESB
from bi_engine_par import ENGINE_PAR_FILTER_RESC
from bi_engine_par import ENGINE_PAR_FILTER_TYPEA
from bi_engine_par import ENGINE_PAR_FILTER_TYPEB
from bi_engine_par import ENGINE_PAR_FILTER_TYPEC
from bi_engine_par import ENGINE_PAR_FILTER_BYPA
from bi_engine_par import ENGINE_PAR_FILTER_BYPB
from bi_engine_par import ENGINE_PAR_FILTER_BYPC
from bi_engine_par import ENGINE_PAR_FILTER_GAIN
from bi_engine_par import ENGINE_PAR_FORMANT_TALK
from bi_engine_par import ENGINE_PAR_FORMANT_SHARP
from bi_engine_par import ENGINE_PAR_FORMANT_SIZE
from bi_engine_par import ENGINE_PAR_LP_CUTOFF
from bi_engine_par import ENGINE_PAR_HP_CUTOFF
from bi_engine_par import ENGINE_PAR_FREQ1
from bi_engine_par import ENGINE_PAR_BW1
from bi_engine_par import ENGINE_PAR_GAIN1
from bi_engine_par import ENGINE_PAR_FREQ2
from bi_engine_par import ENGINE_PAR_BW2
from bi_engine_par import ENGINE_PAR_GAIN2
from bi_engine_par import ENGINE_PAR_FREQ3
from bi_engine_par import ENGINE_PAR_BW3
from bi_engine_par import ENGINE_PAR_GAIN3
from bi_engine_par import ENGINE_PAR_SEQ_LF_GAIN
from bi_engine_par import ENGINE_PAR_SEQ_LF_FREQ
from bi_engine_par import ENGINE_PAR_SEQ_LF_BELL
from bi_engine_par import ENGINE_PAR_SEQ_LMF_GAIN
from bi_engine_par import ENGINE_PAR_SEQ_LMF_FREQ
from bi_engine_par import ENGINE_PAR_SEQ_LMF_Q
from bi_engine_par import ENGINE_PAR_SEQ_HMF_GAIN
from bi_engine_par import ENGINE_PAR_SEQ_HMF_FREQ
from bi_engine_par import ENGINE_PAR_SEQ_HMF_Q
from bi_engine_par import ENGINE_PAR_SEQ_HF_GAIN
from bi_engine_par import ENGINE_PAR_SEQ_HF_FREQ
from bi_engine_par import ENGINE_PAR_SEQ_HF_BELL
from bi_engine_par import ENGINE_PAR_SEND_EFFECT_BYPASS
from bi_engine_par import ENGINE_PAR_SEND_EFFECT_DRY_LEVEL
from bi_engine_par import ENGINE_PAR_SEND_EFFECT_OUTPUT_GAIN
from bi_engine_par import ENGINE_PAR_PH_DEPTH
from bi_engine_par import ENGINE_PAR_PH_SPEED
from bi_engine_par import ENGINE_PAR_PH_SPEED_UNIT
from bi_engine_par import ENGINE_PAR_PH_PHASE
from bi_engine_par import ENGINE_PAR_PH_FEEDBACK
from bi_engine_par import ENGINE_PAR_FL_DEPTH
from bi_engine_par import ENGINE_PAR_FL_SPEED
from bi_engine_par import ENGINE_PAR_FL_SPEED_UNIT
from bi_engine_par import ENGINE_PAR_FL_PHASE
from bi_engine_par import ENGINE_PAR_FL_FEEDBACK
from bi_engine_par import ENGINE_PAR_FL_COLOR
from bi_engine_par import ENGINE_PAR_CH_DEPTH
from bi_engine_par import ENGINE_PAR_CH_SPEED
from bi_engine_par import ENGINE_PAR_CH_SPEED_UNIT
from bi_engine_par import ENGINE_PAR_CH_PHASE
from bi_engine_par import ENGINE_PAR_RV_PREDELAY
from bi_engine_par import ENGINE_PAR_RV_SIZE
from bi_engine_par import ENGINE_PAR_RV_COLOUR
from bi_engine_par import ENGINE_PAR_RV_STEREO
from bi_engine_par import ENGINE_PAR_RV_DAMPING
from bi_engine_par import ENGINE_PAR_DL_TIME
from bi_engine_par import ENGINE_PAR_DL_TIME_UNIT
from bi_engine_par import ENGINE_PAR_DL_DAMPING
from bi_engine_par import ENGINE_PAR_DL_PAN
from bi_engine_par import ENGINE_PAR_DL_FEEDBACK
from bi_engine_par import ENGINE_PAR_IRC_PREDELAY
from bi_engine_par import ENGINE_PAR_IRC_LENGTH_RATIO_ER
from bi_engine_par import ENGINE_PAR_IRC_FREQ_LOWPASS_ER
from bi_engine_par import ENGINE_PAR_IRC_FREQ_HIGHPASS_ER
from bi_engine_par import ENGINE_PAR_IRC_LENGTH_RATIO_LR
from bi_engine_par import ENGINE_PAR_IRC_FREQ_LOWPASS_LR
from bi_engine_par import ENGINE_PAR_IRC_FREQ_HIGHPASS_LR
from bi_engine_par import ENGINE_PAR_GN_GAIN
from bi_engine_par import ENGINE_PAR_MOD_TARGET_INTENSITY
from bi_engine_par import MOD_TARGET_INVERT_SOURCE
from bi_engine_par import ENGINE_PAR_INTMOD_BYPASS
from bi_engine_par import ENGINE_PAR_ATK_CURVE
from bi_engine_par import ENGINE_PAR_ATTACK
from bi_engine_par import ENGINE_PAR_ATTACK_UNIT
from bi_engine_par import ENGINE_PAR_HOLD
from bi_engine_par import ENGINE_PAR_HOLD_UNIT
from bi_engine_par import ENGINE_PAR_DECAY
from bi_engine_par import ENGINE_PAR_DECAY_UNIT
from bi_engine_par import ENGINE_PAR_SUSTAIN
from bi_engine_par import ENGINE_PAR_RELEASE
from bi_engine_par import ENGINE_PAR_RELEASE_UNIT
from bi_engine_par import ENGINE_PAR_DECAY1
from bi_engine_par import ENGINE_PAR_DECAY1_UNIT
from bi_engine_par import ENGINE_PAR_BREAK
from bi_engine_par import ENGINE_PAR_DECAY2
from bi_engine_par import ENGINE_PAR_DECAY2_UNIT
from bi_engine_par import ENGINE_PAR_INTMOD_FREQUENCY
from bi_engine_par import ENGINE_PAR_INTMOD_FREQUENCY_UNIT
from bi_engine_par import ENGINE_PAR_LFO_DELAY
from bi_engine_par import ENGINE_PAR_LFO_DELAY_UNIT
from bi_engine_par import ENGINE_PAR_INTMOD_PULSEWIDTH
from bi_engine_par import ENGINE_PAR_LFO_SINE
from bi_engine_par import ENGINE_PAR_LFO_RECT
from bi_engine_par import ENGINE_PAR_LFO_TRI
from bi_engine_par import ENGINE_PAR_LFO_SAW
from bi_engine_par import ENGINE_PAR_LFO_RAND
from bi_engine_par import ENGINE_PAR_GLIDE_COEF
from bi_engine_par import ENGINE_PAR_GLIDE_COEF_UNIT
from bi_engine_par import ENGINE_PAR_EFFECT_TYPE
from bi_engine_par import ENGINE_PAR_SEND_EFFECT_TYPE
from bi_engine_par import EFFECT_TYPE_FILTER
from bi_engine_par import EFFECT_TYPE_COMPRESSOR
from bi_engine_par import EFFECT_TYPE_LIMITER
from bi_engine_par import EFFECT_TYPE_INVERTER
from bi_engine_par import EFFECT_TYPE_SURROUND_PANNER
from bi_engine_par import EFFECT_TYPE_SHAPER
from bi_engine_par import EFFECT_TYPE_LOFI
from bi_engine_par import EFFECT_TYPE_STEREO
from bi_engine_par import EFFECT_TYPE_DISTORTION
from bi_engine_par import EFFECT_TYPE_SEND_LEVELS
from bi_engine_par import EFFECT_TYPE_PHASER
from bi_engine_par import EFFECT_TYPE_CHORUS
from bi_engine_par import EFFECT_TYPE_FLANGER
from bi_engine_par import EFFECT_TYPE_REVERB
from bi_engine_par import EFFECT_TYPE_DELAY
from bi_engine_par import EFFECT_TYPE_IRC
from bi_engine_par import EFFECT_TYPE_GAINER
from bi_engine_par import EFFECT_TYPE_SKREAMER
from bi_engine_par import EFFECT_TYPE_ROTATOR
from bi_engine_par import EFFECT_TYPE_TWANG
from bi_engine_par import EFFECT_TYPE_CABINET
from bi_engine_par import EFFECT_TYPE_AET_FILTER
from bi_engine_par import EFFECT_TYPE_TRANS_MASTER
from bi_engine_par import EFFECT_TYPE_BUS_COMP
from bi_engine_par import EFFECT_TYPE_TAPE_SAT
from bi_engine_par import EFFECT_TYPE_SOLID_GEQ
from bi_engine_par import EFFECT_TYPE_JUMP
from bi_engine_par import EFFECT_TYPE_FB_COMP
from bi_engine_par import EFFECT_TYPE_ACBOX
from bi_engine_par import EFFECT_TYPE_CAT
from bi_engine_par import EFFECT_TYPE_DSTORTION
from bi_engine_par import EFFECT_TYPE_HOTSOLO
from bi_engine_par import EFFECT_TYPE_VAN51
from bi_engine_par import EFFECT_TYPE_NONE
from bi_engine_par import EFFECT_TYPE_PHASER
from bi_engine_par import EFFECT_TYPE_CHORUS
from bi_engine_par import EFFECT_TYPE_FLANGER
from bi_engine_par import EFFECT_TYPE_REVERB
from bi_engine_par import EFFECT_TYPE_DELAY
from bi_engine_par import EFFECT_TYPE_IRC
from bi_engine_par import EFFECT_TYPE_GAINER
from bi_engine_par import ENGINE_PAR_EFFECT_SUBTYPE
from bi_engine_par import FILTER_TYPE_LP1POLE
from bi_engine_par import FILTER_TYPE_HP1POLE
from bi_engine_par import FILTER_TYPE_BP2POLE
from bi_engine_par import FILTER_TYPE_LP2POLE
from bi_engine_par import FILTER_TYPE_HP2POLE
from bi_engine_par import FILTER_TYPE_LP4POLE
from bi_engine_par import FILTER_TYPE_HP4POLE
from bi_engine_par import FILTER_TYPE_BP4POLE
from bi_engine_par import FILTER_TYPE_BR4POLE
from bi_engine_par import FILTER_TYPE_LP6POLE
from bi_engine_par import FILTER_TYPE_PHASER
from bi_engine_par import FILTER_TYPE_VOWELA
from bi_engine_par import FILTER_TYPE_VOWELB
from bi_engine_par import FILTER_TYPE_PRO52
from bi_engine_par import FILTER_TYPE_LADDER
from bi_engine_par import FILTER_TYPE_VERSATILE
from bi_engine_par import FILTER_TYPE_EQ1BAND
from bi_engine_par import FILTER_TYPE_EQ2BAND
from bi_engine_par import FILTER_TYPE_EQ3BAND
from bi_engine_par import FILTER_TYPE_DAFT_LP
from bi_engine_par import FILTER_TYPE_SV_LP1
from bi_engine_par import FILTER_TYPE_SV_LP2
from bi_engine_par import FILTER_TYPE_SV_LP4
from bi_engine_par import FILTER_TYPE_LDR_LP1
from bi_engine_par import FILTER_TYPE_LDR_LP2
from bi_engine_par import FILTER_TYPE_LDR_LP3
from bi_engine_par import FILTER_TYPE_LDR_LP4
from bi_engine_par import FILTER_TYPE_AR_LP2
from bi_engine_par import FILTER_TYPE_AR_LP4
from bi_engine_par import FILTER_TYPE_AR_LP24
from bi_engine_par import FILTER_TYPE_SV_HP1
from bi_engine_par import FILTER_TYPE_SV_HP2
from bi_engine_par import FILTER_TYPE_SV_HP4
from bi_engine_par import FILTER_TYPE_LDR_HP1
from bi_engine_par import FILTER_TYPE_LDR_HP2
from bi_engine_par import FILTER_TYPE_LDR_HP3
from bi_engine_par import FILTER_TYPE_LDR_HP4
from bi_engine_par import FILTER_TYPE_AR_HP2
from bi_engine_par import FILTER_TYPE_AR_HP4
from bi_engine_par import FILTER_TYPE_AR_HP24
from bi_engine_par import FILTER_TYPE_DAFT_HP
from bi_engine_par import FILTER_TYPE_SV_BP2
from bi_engine_par import FILTER_TYPE_SV_BP4
from bi_engine_par import FILTER_TYPE_LDR_BP2
from bi_engine_par import FILTER_TYPE_LDR_BP4
from bi_engine_par import FILTER_TYPE_AR_BP2
from bi_engine_par import FILTER_TYPE_AR_BP4
from bi_engine_par import FILTER_TYPE_AR_BP24
from bi_engine_par import FILTER_TYPE_SV_NOTCH4
from bi_engine_par import FILTER_TYPE_LDR_PEAK
from bi_engine_par import FILTER_TYPE_LDR_NOTCH
from bi_engine_par import FILTER_TYPE_SV_PAR_LPHP
from bi_engine_par import FILTER_TYPE_SV_PAR_BPBP
from bi_engine_par import FILTER_TYPE_SV_SER_LPHP
from bi_engine_par import FILTER_TYPE_FORMANT_1
from bi_engine_par import FILTER_TYPE_FORMANT_2
from bi_engine_par import FILTER_TYPE_SIMPLE_LPHP
from bi_engine_par import ENGINE_PAR_INTMOD_TYPE
from bi_engine_par import INTMOD_TYPE_NONE
from bi_engine_par import INTMOD_TYPE_LFO
from bi_engine_par import INTMOD_TYPE_ENVELOPE
from bi_engine_par import INTMOD_TYPE_STEPMOD
from bi_engine_par import INTMOD_TYPE_ENV_FOLLOW
from bi_engine_par import INTMOD_TYPE_GLIDE
from bi_engine_par import ENGINE_PAR_INTMOD_SUBTYPE
from bi_engine_par import ENV_TYPE_AHDSR
from bi_engine_par import ENV_TYPE_FLEX
from bi_engine_par import ENV_TYPE_DBD
from bi_engine_par import LFO_TYPE_RECTANGLE
from bi_engine_par import LFO_TYPE_TRIANGLE
from bi_engine_par import LFO_TYPE_SAWTOOTH
from bi_engine_par import LFO_TYPE_RANDO
from bi_engine_par import LFO_TYPE_MULTI
from bi_engine_par import ENGINE_PAR_DISTORTION_TYPE
from bi_engine_par import NI_DISTORTION_TYPE_TUBE
from bi_engine_par import NI_DISTORTION_TYPE_TRANS
from bi_engine_par import ENGINE_PAR_SHAPE_TYPE
from bi_engine_par import NI_SHAPE_TYPE_CLASSIC
from bi_engine_par import NI_SHAPE_TYPE_ENHANCED
from bi_engine_par import NI_SHAPE_TYPE_DRUMS
from bi_engine_par import ENGINE_PAR_START_CRITERIA_MODE
from bi_engine_par import ENGINE_PAR_START_CRITERIA_KEY_MIN
from bi_engine_par import ENGINE_PAR_START_CRITERIA_KEY_MAX
from bi_engine_par import ENGINE_PAR_START_CRITERIA_CONTROLLER
from bi_engine_par import ENGINE_PAR_START_CRITERIA_CC_MIN
from bi_engine_par import ENGINE_PAR_START_CRITERIA_CC_MAX
from bi_engine_par import ENGINE_PAR_START_CRITERIA_CYCLE_CLASS
from bi_engine_par import ENGINE_PAR_START_CRITERIA_ZONE_IDX
from bi_engine_par import ENGINE_PAR_START_CRITERIA_SLICE_IDX
from bi_engine_par import ENGINE_PAR_START_CRITERIA_SEQ_ONLY
from bi_engine_par import ENGINE_PAR_START_CRITERIA_NEXT_CRIT
from bi_engine_par import ENGINE_PAR_START_CRITERIA_MODE
from bi_engine_par import ENGINE_PAR_START_CRITERIA_NEXT_CRIT
from bi_engine_par import START_CRITERIA_NONE
from bi_engine_par import START_CRITERIA_ON_KEY
from bi_engine_par import START_CRITERIA_ON_CONTROLLER
from bi_engine_par import START_CRITERIA_CYCLE_ROUND_ROBIN
from bi_engine_par import START_CRITERIA_CYCLE_RANDOM
from bi_engine_par import START_CRITERIA_SLICE_TRIGGER
from bi_engine_par import START_CRITERIA_AND_NEXT
from bi_engine_par import START_CRITERIA_AND_NOT_NEXT
from bi_engine_par import START_CRITERIA_OR_NEXT
from bi_engine_par import find_mod
from bi_engine_par import find_target
from bi_engine_par import get_engine_par
from bi_engine_par import get_engine_par_disp
from bi_engine_par import get_voice_limit
from bi_engine_par import set_voice_limit
from bi_engine_par import output_channel_name
from bi_engine_par import set_engine_par
from bi_load_save import get_folder
from bi_load_save import load_array
from bi_load_save import load_array_str
from bi_load_save import load_ir_sample
from bi_load_save import save_array
from bi_load_save import save_array_str
from bi_load_save import save_midi_file
from bi_midi import MIDI_COMMAND_NOTE_ON
from bi_midi import MIDI_COMMAND_POLY_AT
from bi_midi import MIDI_COMMAND_CC
from bi_midi import MIDI_COMMAND_PROGRAM_CHANGE
from bi_midi import MIDI_COMMAND_MONO_AT
from bi_midi import MIDI_COMMAND_PITCH_BEND
from bi_midi import MIDI_COMMAND_RPN
from bi_midi import MIDI_COMMAND_NRPN
from bi_midi import MIDI_BYTE_1
from bi_midi import MIDI_BYTE_2
from bi_midi import MIDI_COMMAND
from bi_midi import mf_insert_file
from bi_midi import mf_set_export_area
from bi_midi import mf_set_buffer_size
from bi_midi import mf_set_buffer_size
from bi_midi import mf_get_buffer_size
from bi_midi import mf_reset
from bi_midi import mf_insert_event
from bi_midi import mf_remove_event
from bi_midi import mf_set_event_par
from bi_midi import mf_get_event_par
from bi_midi import mf_get_id
from bi_midi import mf_set_mark
from bi_midi import mf_get_mark
from bi_midi import by_track
from bi_midi import mf_get_first
from bi_midi import mf_get_last
from bi_midi import mf_get_next
from bi_midi import mf_get_prev
from bi_midi import mf_get_next_at
from bi_midi import mf_get_prev_at
from bi_midi import mf_get_num_tracks
from bi_midi import set_midi
from bi_misc import array_equal
from bi_misc import num_elements
from bi_misc import search
from bi_misc import sort
from bi_misc import allow_group
from bi_misc import disallow_group
from bi_misc import find_group
from bi_misc import get_purge_state
from bi_misc import group_name
from bi_misc import purge_group
from bi_misc import change_listener_par
from bi_misc import ms_to_ticks
from bi_misc import ticks_to_ms
from bi_misc import set_listener
from bi_misc import stop_wait
from bi_misc import wait
from bi_misc import wait_ticks
from bi_misc import in_range
from bi_misc import NI_KEY_TYPE_DEFAULT
from bi_misc import NI_KEY_TYPE_CONTROL
from bi_misc import NI_KEY_TYPE_NONE
from bi_misc import KEY_COLOR_RED
from bi_misc import KEY_COLOR_ORANGE
from bi_misc import KEY_COLOR_LIGHT_ORANGE
from bi_misc import KEY_COLOR_WARM_YELLOW
from bi_misc import KEY_COLOR_YELLOW
from bi_misc import KEY_COLOR_LIME
from bi_misc import KEY_COLOR_GREEN
from bi_misc import KEY_COLOR_MINT
from bi_misc import KEY_COLOR_CYAN
from bi_misc import KEY_COLOR_TURQUOISE
from bi_misc import KEY_COLOR_BLUE
from bi_misc import KEY_COLOR_PLUM
from bi_misc import KEY_COLOR_VIOLET
from bi_misc import KEY_COLOR_PURPLE
from bi_misc import KEY_COLOR_MAGENTA
from bi_misc import KEY_COLOR_FUCHSIA
from bi_misc import KEY_COLOR_DEFAULT
from bi_misc import KEY_COLOR_INACTIVE
from bi_misc import KEY_COLOR_NONE
from bi_misc import get_key_color
from bi_misc import set_key_color
from bi_misc import get_key_name
from bi_misc import set_key_name
from bi_misc import get_key_triggerstate
from bi_misc import get_key_type
from bi_misc import get_keyrange_min_note
from bi_misc import get_keyrange_max_note
from bi_misc import get_keyrange_name
from bi_misc import set_key_pressed
from bi_misc import set_key_pressed_support
from bi_misc import set_key_type
from bi_misc import set_keyrange
from bi_misc import remove_keyrange
from bi_misc import NO_SYS_SCRIPT_GROUP_START
from bi_misc import NO_SYS_SCRIPT_PEDAL
from bi_misc import NO_SYS_SCRIPT_RLS_TRIG
from bi_misc import SET_CONDITION
from bi_misc import RESET_CONDITION
from bi_misc import find_zone
from bi_misc import get_sample_length
from bi_misc import num_slices_zone
from bi_misc import zone_slice_length
from bi_misc import zone_slice_start
from bi_misc import zone_slice_idx_loop_start
from bi_misc import zone_slice_idx_loop_end
from bi_misc import zone_slice_loop_count
from bi_misc import dont_use_machine_mode
from bi_misc import pgs_create_key
from bi_misc import pgs_create_str_key
from bi_misc import pgs_key_exists
from bi_misc import pgs_str_key_exists
from bi_misc import pgs_set_key_val
from bi_misc import pgs_set_str_key_val
from bi_misc import pgs_get_key_val
from bi_misc import pgs_get_str_key_val
from bi_notes_events import MARK_1
from bi_notes_events import MARK_2
from bi_notes_events import MARK_3
from bi_notes_events import MARK_4
from bi_notes_events import MARK_5
from bi_notes_events import MARK_6
from bi_notes_events import MARK_7
from bi_notes_events import MARK_8
from bi_notes_events import MARK_9
from bi_notes_events import MARK_10
from bi_notes_events import MARK_11
from bi_notes_events import MARK_12
from bi_notes_events import MARK_13
from bi_notes_events import MARK_14
from bi_notes_events import MARK_15
from bi_notes_events import MARK_16
from bi_notes_events import MARK_17
from bi_notes_events import MARK_18
from bi_notes_events import MARK_19
from bi_notes_events import MARK_20
from bi_notes_events import MARK_21
from bi_notes_events import MARK_22
from bi_notes_events import MARK_23
from bi_notes_events import MARK_24
from bi_notes_events import MARK_25
from bi_notes_events import MARK_26
from bi_notes_events import MARK_27
from bi_notes_events import MARK_28
from bi_notes_events import CC
from bi_notes_events import CC_TOUCHED
from bi_notes_events import CC_NUM
from bi_notes_events import EVENT_ID
from bi_notes_events import EVENT_NOTE
from bi_notes_events import EVENT_VELOCITY
from bi_notes_events import CURRENT_EVENT
from bi_notes_events import EVENT_PAR_0
from bi_notes_events import EVENT_PAR_1
from bi_notes_events import EVENT_PAR_2
from bi_notes_events import EVENT_PAR_3
from bi_notes_events import EVENT_PAR_VOLUME
from bi_notes_events import EVENT_PAR_PAN
from bi_notes_events import EVENT_PAR_TUNE
from bi_notes_events import EVENT_PAR_NOTE
from bi_notes_events import EVENT_PAR_VELOCITY
from bi_notes_events import EVENT_PAR_ALLOW_GROUP
from bi_notes_events import EVENT_PAR_SOURCE
from bi_notes_events import EVENT_PAR_PLAY_POS
from bi_notes_events import EVENT_PAR_ZONE_ID
from bi_notes_events import EVENT_PAR_MIDI_CHANNEL
from bi_notes_events import EVENT_PAR_MIDI_COMMAND
from bi_notes_events import EVENT_PAR_MIDI_BYTE_1
from bi_notes_events import EVENT_PAR_MIDI_BYTE_2
from bi_notes_events import EVENT_PAR_POS
from bi_notes_events import EVENT_PAR_NOTE_LENGTH
from bi_notes_events import EVENT_PAR_ID
from bi_notes_events import EVENT_PAR_TRACK_NR
from bi_notes_events import EVENT_STATUS_INACTIVE
from bi_notes_events import EVENT_STATUS_NOTE_QUEUE
from bi_notes_events import EVENT_STATUS_MIDI_QUEUE
from bi_notes_events import GROUPS_AFFECTED
from bi_notes_events import NOTE_HELD
from bi_notes_events import POLY_AT
from bi_notes_events import POLY_AT_NUM
from bi_notes_events import RPN_ADDRESS
from bi_notes_events import RPN_VALUE
from bi_notes_events import VCC_MONO_AT
from bi_notes_events import VCC_PITCH_BEND
from bi_notes_events import note_off
from bi_notes_events import play_note
from bi_notes_events import set_controller
from bi_notes_events import set_rpn
from bi_notes_events import set_nrpn
from bi_notes_events import set_snapshot_type
from bi_notes_events import by_marks
from bi_notes_events import change_note
from bi_notes_events import change_velo
from bi_notes_events import change_pan
from bi_notes_events import change_tune
from bi_notes_events import change_vol
from bi_notes_events import delete_event_mark
from bi_notes_events import event_status
from bi_notes_events import fade_in
from bi_notes_events import fade_out
from bi_notes_events import get_event_ids
from bi_notes_events import get_event_par
from bi_notes_events import get_event_par_arr
from bi_notes_events import set_event_par
from bi_notes_events import set_event_par_arr
from bi_notes_events import ignore_event
from bi_notes_events import set_event_mark
from bi_notes_events import reset_rls_trig_counter
from bi_notes_events import will_never_terminate
from bi_ui_controls import KNOB_UNIT_NONE
from bi_ui_controls import KNOB_UNIT_DB
from bi_ui_controls import KNOB_UNIT_HZ
from bi_ui_controls import KNOB_UNIT_PERCENT
from bi_ui_controls import KNOB_UNIT_MS
from bi_ui_controls import KNOB_UNIT_ST
from bi_ui_controls import KNOB_UNIT_OCT
from bi_ui_controls import CONTROL_PAR_NONE
from bi_ui_controls import CONTROL_PAR_HELP
from bi_ui_controls import CONTROL_PAR_POS_X
from bi_ui_controls import CONTROL_PAR_POS_Y
from bi_ui_controls import CONTROL_PAR_GRID_X
from bi_ui_controls import CONTROL_PAR_GRID_Y
from bi_ui_controls import CONTROL_PAR_WIDTH
from bi_ui_controls import CONTROL_PAR_HEIGHT
from bi_ui_controls import CONTROL_PAR_GRID_WIDTH
from bi_ui_controls import CONTROL_PAR_GRID_HEIGHT
from bi_ui_controls import CONTROL_PAR_HIDE
from bi_ui_controls import CONTROL_PAR_BG_COLOR
from bi_ui_controls import HIDE_PART_BG
from bi_ui_controls import HIDE_PART_VALUE
from bi_ui_controls import HIDE_PART_TITLE
from bi_ui_controls import HIDE_PART_MOD_LIGHT
from bi_ui_controls import HIDE_PART_NOTHING
from bi_ui_controls import HIDE_WHOLE_CONTROL
from bi_ui_controls import HIDE_PART_CURSOR
from bi_ui_controls import HIDE_PART_BG
from bi_ui_controls import HIDE_PART_VALUE
from bi_ui_controls import HIDE_PART_TITLE
from bi_ui_controls import HIDE_PART_MOD_LIGHT
from bi_ui_controls import HIDE_PART_NOTHING
from bi_ui_controls import HIDE_WHOLE_CONTROL
from bi_ui_controls import HIDE_PART_CURSOR
from bi_ui_controls import CONTROL_PAR_PICTURE
from bi_ui_controls import CONTROL_PAR_PICTURE_STATE
from bi_ui_controls import CONTROL_PAR_Z_LAYER
from bi_ui_controls import CONTROL_PAR_VALUE
from bi_ui_controls import CONTROL_PAR_DEFAULT_VALUE
from bi_ui_controls import CONTROL_PAR_TEXT
from bi_ui_controls import CONTROL_PAR_TEXTLINE
from bi_ui_controls import CONTROL_PAR_LABEL
from bi_ui_controls import CONTROL_PAR_UNIT
from bi_ui_controls import CONTROL_PAR_FONT_TYPE
from bi_ui_controls import font
from bi_ui_controls import CONTROL_PAR_TEXTPOS_Y
from bi_ui_controls import CONTROL_PAR_TEXT_ALIGNMENT
from bi_ui_controls import text_alignment
from bi_ui_controls import CONTROL_PAR_AUTOMATION_NAME
from bi_ui_controls import CONTROL_PAR_ALLOW_AUTOMATION
from bi_ui_controls import CONTROL_PAR_AUTOMATION_ID
from bi_ui_controls import NI_CONTROL_PAR_IDX
from bi_ui_controls import CONTROL_PAR_KEY_SHIFT
from bi_ui_controls import CONTROL_PAR_KEY_ALT
from bi_ui_controls import CONTROL_PAR_KEY_CONTROL
from bi_ui_controls import CONTROL_PAR_BAR_COLOR
from bi_ui_controls import CONTROL_PAR_ZERO_LINE_COLOR
from bi_ui_controls import CONTROL_PAR_NUM_ITEMS
from bi_ui_controls import CONTROL_PAR_SELECTED_ITEM_IDX
from bi_ui_controls import CONTROL_PAR_DND_BEHAVIOUR
from bi_ui_controls import CONTROL_PAR_SHOW_ARROWS
from bi_ui_controls import CONTROL_PAR_OFF_COLOR
from bi_ui_controls import CONTROL_PAR_ON_COLOR
from bi_ui_controls import CONTROL_PAR_OVERLOAD_COLOR
from bi_ui_controls import CONTROL_PAR_PEAK_COLOR
from bi_ui_controls import CONTROL_PAR_VERTICAL
from bi_ui_controls import CONTROL_PAR_BASEPATH
from bi_ui_controls import CONTROL_PAR_FILEPATH
from bi_ui_controls import CONTROL_PAR_COLUMN_WIDTH
from bi_ui_controls import CONTROL_PAR_FILE_TYPE
from bi_ui_controls import NI_FILE_TYPE_MIDI
from bi_ui_controls import NI_FILE_TYPE_AUDIO
from bi_ui_controls import NI_FILE_TYPE_ARRAY
from bi_ui_controls import VALUE_EDIT_MODE_NOTE_NAMES
from bi_ui_controls import UI_WAVEFORM_USE_SLICES
from bi_ui_controls import UI_WAVEFORM_USE_TABLE
from bi_ui_controls import UI_WAVEFORM_TABLE_IS_BIPOLAR
from bi_ui_controls import UI_WAVEFORM_USE_MIDI_DRAG
from bi_ui_controls import UI_WF_PROP_PLAY_CURSOR
from bi_ui_controls import UI_WF_PROP_FLAGS
from bi_ui_controls import UI_WF_PROP_TABLE_VAL
from bi_ui_controls import UI_WF_PROP_TABLE_IDX_HIGHLIGHT
from bi_ui_controls import UI_WF_PROP_MIDI_DRAG_START_NOTE
from bi_ui_controls import CONTROL_PAR_WAVE_COLOR
from bi_ui_controls import CONTROL_PAR_WAVE_CURSOR_COLOR
from bi_ui_controls import CONTROL_PAR_SLICEMARKERS_COLOR
from bi_ui_controls import CONTROL_PAR_BG_ALPHA
from bi_ui_controls import CONTROL_PAR_MOUSE_BEHAVIOUR
from bi_ui_controls import CONTROL_PAR_MOUSE_BEHAVIOUR_X
from bi_ui_controls import CONTROL_PAR_MOUSE_BEHAVIOUR_Y
from bi_ui_controls import CONTROL_PAR_MOUSE_MODE
from bi_ui_controls import CONTROL_PAR_ACTIVE_INDEX
from bi_ui_controls import CONTROL_PAR_CURSOR_PICTURE
from bi_ui_controls import set_control_par
from bi_ui_controls import get_control_par
from bi_ui_controls import set_control_par_str
from bi_ui_controls import get_control_par_str
from bi_ui_controls import set_control_par_arr
from bi_ui_controls import get_control_par_arr
from bi_ui_controls import set_control_par_str_arr
from bi_ui_controls import get_control_par_str_arr
from bi_ui_controls import get_menu_item_str
from bi_ui_controls import get_menu_item_value
from bi_ui_controls import get_menu_item_visibility
from bi_ui_controls import set_menu_item_str
from bi_ui_controls import set_menu_item_value
from bi_ui_controls import set_menu_item_visibility
from bi_ui_controls import get_ui_wf_property
from bi_ui_controls import set_ui_wf_property
from bi_ui_controls import set_ui_color
