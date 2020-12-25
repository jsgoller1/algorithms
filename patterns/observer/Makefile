PATTERN:=observer

all: clean compile

clean:
	-rm -r $(PATTERN)
	reset 

compile: clean
	javac -d . *.java
	java $(PATTERN).Main