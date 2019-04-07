PWD:= `pwd`
EXERCISE:= `basename $$PWD`


### Binary cleanup
setup:
	-mkdir $(BUILD_DIR)

# Note: the folder is called /execs so you don't accidentally
# run $rm -r against your system's /bin directory.
clean:
	-rm -r $(BUILD_DIR)/*

reset:
	reset

# Duplicated because GNU Make doesn't support mixing implicit and explicit rules, *eyeroll*
solution: reset clean setup
	$(COMPILE) $@.cpp -o $(BUILD_DIR)/$(EXERCISE)-$@
	$(VALGRIND) $(BUILD_DIR)/$(EXERCISE)-$@

alternate-%: reset clean setup
	$(COMPILE) $@.cpp -o $(BUILD_DIR)/$(EXERCISE)-$@
	$(VALGRIND) $(BUILD_DIR)/$(EXERCISE)-$@

# There may not be a Python solution, but if there is, you can $make python
python:
	python solution.py
