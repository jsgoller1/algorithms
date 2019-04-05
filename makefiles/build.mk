PWD:= `pwd`
EXERCISE:= `basename $$PWD`

# Duplicated because GNU Make doesn't support mixing implicit and explicit rules, *eyeroll*
solution: reset clean setup
	$(COMPILE) $@.cpp -o $(BUILD_DIR)/$(EXERCISE)-$@
	$(ROOT_DIR)/execs/$(EXERCISE)-$@

alternate-%: reset clean setup
	$(COMPILE) $@.cpp -o $(BUILD_DIR)/$(EXERCISE)-$@
	$(BUILD_DIR)/$(EXERCISE)-$@

# There may not be a Python solution, but if there is, you can $make python
python:
	python solution.py
