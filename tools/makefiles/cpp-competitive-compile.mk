##################################################################
### Compiler flags and settings for programming competitions;  ###
### this Makefile is included by others and not used directly. ###
##################################################################
CC:=g++
CFLAGS :=-std=c++11 -O2
WARNINGS :=-Wall -Wno-c++98-compat
COMPILE:= $(CC) $(CFLAGS) $(WARNINGS)
