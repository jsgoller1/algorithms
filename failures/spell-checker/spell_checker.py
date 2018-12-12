#!/bin/python3

import heapq
import collections
import time

"""
Given a list of valid words (sorted) and their associated frequencies, write a spell-checker
program that will determine if a word is correctly spelled, or give the "top n" suggestions
for words that the user might be trying to spell.
----
Understand

In: a list of legal words with frequencies and a possibly-legal word.
Output: A list of words; if the possibly-legal word is in fact legal, it is returned in a singleton list. Otherwise, the list contains n words.

A spell checker somehow says "we have word X, and could go to words Y or Z"; e.g. entering "poerty" into a spell checker might suggest we
go to "pottery" or "poetry".

What are some possible corrections we could need to make?
"catx" -> "cat" (remove a letter)
"transfor" -> "transform" (add a letter)
"cxt" -> "cat" (swap a letter)

So for a k-letter word, we can:
- delete one of k letters
- add k*26 possible letters
- swap a letter in k*26 different possible ways.
or (k + 2*(k*26)) or (k+52k) different possible strings.

----
Plan

This feels like a graph search problem - the vertices are words and the edges are single-letter modifications.
The starting vertex is our possibly legal word, and there are numerous goal states, each of which is a word in the word list.

With our starting string, we can generate each of the possible k+52k different strings, and test them to see if they are valid words.
If they are valid, we add them to a valid word list. Then, check if we've seen the string. If not, add it to a list of already visited words
and enqueue it. If we have seen the string before, skip it.

When the valid word list has n many entries in it, we should remove them in order of lowest to highest; treating the list
as a priority queue will make this easy.

This problem is high-risk for exploding in terms of complexity, so we will want to use efficent data structures (but not prematurely optimize)!

----
Execute

See below.

----
Review

...it worked on the first try (minus little syntax errors). 0.o

Well, sort of. Checking "therm" worked quickly and correctly. However, "encapsulate" isn't in the word list, and
it failed to complete in a reasonable amount of time when asked to find it. Same thing for "referrral". Hmmm....

On further examination, it appears that for "cbnnon", "cannon" is added quickly, but "canon" isn't. Perhaps we
should check word validity sooner?

The BFS prioritizes all possible strings of edit distance 1 from the current string, and this is no good
because valid strings and nearly-valid strings should be examined sooner than very-invalid ones. We
need some kind of heuristic for this search.

Is there some kind of data structure where we can take a string and efficiently get
an answer back as to "is this 1-away from anything in the structure?" For the "word ladders"
problem, there's some way to use word buckets (i.e. for "date": "_ate", "d_te", etc.)

Adding a timeout seems to give slightly better performance, but not by much. Some obvious words still go missing.
"referencx" takes until the timeout and doesn't return "referenced".

What if we could design something that would go through every item in a list, check its edit distance from
those items, and then return an "average edit distance" from words in that list. This could then be used as
a priority rating, e.g. "cxt" would have a very high priority since it's close to "cat", "cut", "cot", and so on
but "xadf" would have a lower score.
"""


def assemble_valid_dict():
    """
    Read sorted_word_list.txt and construct a dictionary mapping the words
    to their frequencies.
    """
    word_dict = {}
    with open('sorted_word_list.txt', 'r') as word_list:
        for wordline in word_list.readlines():
            word, score = wordline[:-1].split()
            word_dict[word] = int(score)
    return word_dict


def generate_swap(word):
    """
    Given "food", generate "jood", "fjod", "fooj", and so on.
    """
    strings = collections.deque()
    for i in range(len(word)):
        for j in range(ord('a'), ord('z') + 1):
            if chr(j) != word[i]:
                strings.append(word[:i] + chr(j) + word[i+1:])
    return strings


def generate_deletions(word):
    """
    Given "food", generate "ood", "fod", "fod", and "foo"
    """
    strings = collections.deque()
    for i in range(len(word)):
        strings.append(word[:i] + word[i+1:])
    return strings


def generate_insertions(word):
    """
    Given "food", generate "fbood", "fojod", "fooxd", and so on.
    """
    strings = collections.deque()
    for i in range(len(word)+1):
        for j in range(ord('a'), ord('z') + 1):
            strings.append(word[:i] + chr(j) + word[i:])
    return strings


def spell_checker(in_word, n=5, timeout=4):
    """
    Execute spell-checking with a timeout. BFS through all possible word mutations,
    and quit if we find enough possible corrections, or if we exceed a timeout.
    """
    if not in_word.isalpha():
        raise ValueError("Word must consist of only alphabetical characters.")

    # Read in word list file
    valid_words = assemble_valid_dict()
    if (in_word in valid_words):
        return [(0, in_word)]

    # Setup
    visited_words = set()
    corrected_words = []
    q = collections.deque([in_word])

    # BFS until we find enough possible words the user could mean
    start = time.time()
    current = start
    while q and len(corrected_words) < n and (current - start < timeout):
        current = q.pop()
        strings = generate_swap(
            current) + generate_deletions(current) + generate_insertions(current)
        for string in strings:
            if string not in visited_words:
                if string in valid_words and len(corrected_words) < n:
                    corrected_words.append((valid_words[string], string))
                    #print("Added valid words: %s" % string)
                visited_words.add(string)
                q.append(string)
        current = time.time()
    return corrected_words


if __name__ == '__main__':
    in_word = input("Enter a word: ")
    spelled_words = spell_checker(in_word.lower())
    if spelled_words:
        if spelled_words[0][1] == in_word:
            print("%s is a valid word." % in_word)
        else:
            print("Did you mean...")
            for word in spelled_words:
                print("{0}".format(word[1]))
    else:
        print("Couldn't find any corrected spellings")
