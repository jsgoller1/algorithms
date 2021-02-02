VENV:=venv/algos
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
CC_QUALITY_COMPILER:=clang++
CC_QUALITY_FLAGS :=-std=c++17 -g -lm -Wno-c++98-compat -fstandalone-debug
CC_QUALITY_WARNINGS :=-Weverything -Werror
CC_QUALITY_COMPILE:= $(CC_QUALITY_COMPILER) $(CC_QUALITY_FLAGS) $(CC_QUALITY_WARNINGS)

CC_CONTEST_COMPILER:=g++
CC_CONTEST_FLAGS :=-std=c++11 -O2
CC_CONTEST_WARNINGS :=-Wall -Wno-c++98-compat
CONTEST_COMPILE:= $(CC_CONTEST_COMPILER) $(CC_CONTEST_FLAGS) $(CC_CONTEST_WARNINGS)

install:
	-rm -r $(VENV)
	python3 -m venv ./$(VENV)
	source $(VENV)/bin/activate; pip3 install requirements.txt

# Run this with $sudo
sudo-install:
	apt-get install clang valgrind	

notebooks:
	source $(VENV)/bin/activate; jupyter-notebook

clean:
	-rm -r $(BUILD_DR)
	-mkdir $(BUILD_DIR)