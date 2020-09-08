###########################################################################
### Compiler flags and settings for working on quality / noncompetitive ###
### code; this Makefile is included by others and not used directly.		###
###########################################################################
CC:=clang++
CFLAGS :=-std=c++17 -g -lm -Wno-c++98-compat -fstandalone-debug
WARNINGS :=-Weverything -Werror
COMPILE:= $(CC) $(CFLAGS) $(WARNINGS)
