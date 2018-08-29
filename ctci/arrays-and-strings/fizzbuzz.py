instructions = """
For every integer between 1 and 100, do the following:
    If the integer is divisible by 3, print "Fizz".
    If the integer is divisible by 5, print, "Buzz".
    If it is divisible by both, print "FizzBuzz".
    If it is divisible by neither, print the integer.

If you ever ask me this during an interview, I will literally
kick you into next thursday.
"""

def fizzbuzz():
    for number in range(1,101):
        string = ''
        if (not(number % 3)):
            string += 'Fizz'
        if (not(number % 5)):
            string += 'Buzz'
        if (not(string)):
            string = str(number)
        print string

if __name__ == "__main__":
    fizzbuzz()
