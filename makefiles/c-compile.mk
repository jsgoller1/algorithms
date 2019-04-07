### Uncomment this to run Clang's static analyzer while building; this makes the build slower.
ANALYZER:=scan-build --status-bugs

### Compiler settings
CC:=clang
CFLAGS :=-std=gnu11 -g -lm -pthread
WARNINGS :=-Weverything -Werror
COMPILE:=$(ANALYZER) $(CC) $(CFLAGS) $(WARNINGS) $(EXTRA_FLAGS)
