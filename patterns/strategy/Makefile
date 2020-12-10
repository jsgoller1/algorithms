all: clean compile

clean:
	-rm -r strategy
	reset 

compile: clean
	javac -d . *.java
	java strategy.DuckGame