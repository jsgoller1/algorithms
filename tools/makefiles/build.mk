### Run Clang's static analyzer while building; this makes the build slower.
ANALYZER:=scan-build --status-bugs

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

good: reset clean setup
	$(ANALYZER) $(COMPILE) solution.cpp -o $(BUILD_DIR)/$(EXERCISE)-$@
	$(VALGRIND) $(BUILD_DIR)/$(EXERCISE)-$@

solution fast: reset clean setup
	$(COMPILE) solution.cpp -o $(BUILD_DIR)/$(EXERCISE)-$@
	$(BUILD_DIR)/$(EXERCISE)-$@

# Duplicated because GNU Make doesn't support mixing implicit and explicit rules, *eyeroll*
alternate-%: reset clean setup
	$(ANALYZER) $(COMPILE) $@.cpp -o $(BUILD_DIR)/$(EXERCISE)-$@
	$(VALGRIND) $(BUILD_DIR)/$(EXERCISE)-$@

# There may not be a Python solution, but if there is, this runs it.
python:
	python3 solution.py
