"""
See README.md for problem description.
---
Understand - We have to handle both decoding and encoding.

We will get a string like "2A3B" and need to return
"AABBB", or "AABBB" and need to return "2A3B". RLE is
described in the README. The tests will call our decode()/encode()
methods with a string of either.

Encoding an encoded string should cause an exception.

Decoding a decoded string should return the input unchanged.
-----
Plan:

Encoding: This is the easier of the two tasks; we need only
loop through the string and keep count of how many of the same
characters we see. Once we see a different character, we flush
the count (as a string) and the character to the encoded string (if
we only saw the character, just flush the character and no count).

Decoding: To get the number, read character by character from
the string, testing with str.isdigit(); once this is
false, we've read all the number-characters and can get the alpha
character. Cast the count characters to an actual number, repeat
the alpha character that many times, and flush it to the decoded string.

-----
Execute - see below.
-----
Review - My initial stab at the code followed the above, but was not particularly clean, so I played with
several approaches. For decoding, the shortest / cleanest one I came up with
involved only checking if the character in question was a digit. If not, it meant
we hit the alphanumeric character that needed to be expanded (the assumptions
in the README allow for this), and could append the expansion. A special edge case had to
be created for single-characters with no expansion.

The current algorithm's time complexity is O(N) a string of length N; it must parse the entire string,
but the expansions should be O(1), so even huge strings can be decoded easily. Its space complexity
is dependent on how large the expansions are - a string like "100k250z3000j" will be very large despite
the input being very short. I am not perfectly sure what the right big-oh class is, but my gut says
O(K), where K is the largest integer in the encoding.

For encoding, I tried 2 or 3 different approaches. The trickiest part was cleanly handling both
the last stretch of characters in the input, and cases where only one character was present (i.e.
trying not to allow "1A" to wind up in the final encoding). I eventually decided on a "worse is better"
approach using lists and allowing "1A" to be appended, but then stripped out at the end.

Encoding is O(N) for time and space - every character in the string must be examined, and at worst
every character must be stored.

"""


def decode(string):
    decoded = ''
    num_string = ''

    for char in string:
        if char.isdigit():
            num_string += char
        else:
            if num_string == '':  # we only saw a single char and no number
                decoded += char
            else:
                decoded += char * int(num_string)
            num_string = ''

    return decoded


def encode(string):
    encoded = []
    count = 1

    for i, char in enumerate(string):
        try:
            if char == string[i + 1]:
                count += 1
            else:
                encoded.append(str(count))
                encoded.append(char)
                count = 1
        except IndexError:
            encoded.append(str(count))
            encoded.append(char)

    return ''.join([x for x in encoded if x != '1'])


if __name__ == '__main__':
    print(decode("2A3B"))
    print(decode("2A3B15C"))
    print(decode("ABC"))
    print(decode(""))

    print(encode("AABBB"))
    print(encode("AABBBCCCCCCCCCCCCCCC"))
    print(encode("ABC"))
    print(encode(""))
