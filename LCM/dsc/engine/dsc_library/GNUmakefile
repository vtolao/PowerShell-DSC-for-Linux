DSCTOP = ../..
TOP = ../../..
include $(TOP)/config.mak

LIBRARY = dsc_library

SOURCES = \
        dsc_library.c 

INCLUDES = \
        $(OMI) \
        $(OMI)/common \
        $(DSCTOP)/common/inc \
        $(DSCTOP)/engine/EngineHelper \
        $(DSCTOP)/engine \
        $(DSCTOP)/engine/ca/CAInfrastructure \
        $(DSCTOP)/engine/ModuleLoader/ModuleLibrary \
        $(TOP)/codec/common \
        $(OMI)/nits/base \
        $(TOP)/json_parson \
        $(DSCTOP)/engine/ConfigurationManager 

DEFINES = MI_CONST= HOOK_BUILD $(BUILD_OMS)

include $(OMI)/mak/rules.mak
