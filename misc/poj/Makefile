VENV:=algos-venv
BUILD_DIR:=bin/

### Uncomment this to run Clang's static analyzer while building; this makes the build slower.
ANALYZER:=scan-build --status-bugs

### Valgrind target for memory analysis
VALGRIND := valgrind -q --leak-check=full --show-leak-kinds=all --track-origins=yes --error-exitcode=42

### C compilation flags
C_COMPILER:=clang
C_FLAGS :=-std=gnu11 -g -lm -pthread
C_WARNINGS :=-Weverything -Werror
C_COMPILE:=$(ANALYZER) $(CC) $(CFLAGS) $(WARNINGS) $(EXTRA_FLAGS)

### C++ compilation flags for different scenarios
CC_COMPILE:=g++ -x c++ -O2 -std=c++17 -Wall

1004-financial-management:
	$(CC_COMPILE) $@.cc -o /tmp/$@
