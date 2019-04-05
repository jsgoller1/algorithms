PWD:= `pwd`
EXERCISE:= `basename $$PWD`

# Duplicated because GNU Make doesn't support mixing implicit and explicit rules, *eyeroll*
solution: reset clean setup
	$(COMPILE) $@.cpp -o $(BUILD_DIR)/$(EXERCISE)-$@
	$(ROOT_DIR)/execs/$(EXERCISE)-$@

alternate-%: reset clean setup
	$(COMPILE) $@.cpp -o $(BUILD_DIR)/$(EXERCISE)-$@
	$(BUILD_DIR)/$(EXERCISE)-$@

python:
	python solution.py
