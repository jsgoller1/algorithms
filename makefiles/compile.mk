#################################################################
### Compiler flags and settings; this Makefile is included by ###
### others and not used directly.															###
#################################################################

### Uncomment this to run Clang's static analyzer while building; this makes the build slower.
ANALYZER:=scan-build --status-bugs

### Compiler settings
CC:=clang++
CFLAGS :=-std=c++17 -g -lm -Wno-c++98-compat
WARNINGS :=-Weverything -Werror
COMPILE:=$(ANALYZER) $(CC) $(CFLAGS) $(WARNINGS)

### Valgrind target for memory analysis
VALGRIND := valgrind -q --leak-check=full --show-leak-kinds=all --track-origins=yes --error-exitcode=42

### Binary cleanup
setup:
	-mkdir $(BUILD_DIR)

# Note: the folder is called /execs so you don't accidentally
# run $rm -r against your system's /bin directory.
clean:
	-rm -r $(BUILD_DIR)/*

reset:
	reset
