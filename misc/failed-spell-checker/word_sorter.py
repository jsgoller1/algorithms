#!/bin/python
import collections


in_words = open('word_list.txt', 'r')
out_words = open('sorted_word_list.txt', 'w')

out_word_list = collections.deque()
for i, word in enumerate(in_words.readlines()):
    out_word_list.append("%s %i\n" % (word[:-1], i+1))

out_words.writelines(sorted(out_word_list))
