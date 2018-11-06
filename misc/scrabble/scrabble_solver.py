#!/bin/python

import itertools
import collections
import copy

"""
1 - Given a dictionary of scrabble words, check if a word is in it.
2 - Given a set of letters, determine all valid words that can be created with that set (not necessarily all letters)
3 - Validate a Scrabble board:
    - Centered
    - Valid words
    - No islands
"""


def in_dictionary(word, dictionary):
    return word.upper() in dictionary


def generate_dictionary(path):
    dictionary_f = open(path, "r")
    dictionary = dictionary_f.read().splitlines()
    return dictionary


def check_letter_set():
    """
    check_letter_set(): Check how many words we can make
    with a set of scrabble letters.
    """
    character_set = raw_input("Enter a character set: ")

    for i in range(1, len(character_set) + 1):
        perms = list(itertools.permutations(character_set, i))
        for perm in perms:
            perm_string = ''.join(perm)
            if in_dictionary(perm_string, dictionary):
                solutions[perm_string] = True

    print solutions.keys()


def generate_board(path):
    board_f = open(path, "r")
    board = [row.replace(' ', '') for row in board_f.read().splitlines()]
    # dictionary = dictionary_f.read().splitlines()
    return board


def validate_center(board):
    center = len(board) / 2
    row = board[center]
    return row[center] != '0'


def validate_column_words(board, dictionary):
    columns = []
    for column in range(len(board)):
        columns.append(''.join([row[column] for row in board]))
    return validate_row_words(columns, dictionary)


def validate_row_words(board, dictonary):
    for row in board:
        words = [string for string in row.split("0") if (len(string) > 1)]
        for word in words:
            if not in_dictionary(word, dictionary):
                print("{0} is not valid".format(word))
                return False
    return True


def validate_all_words(board, dictionary):
    return validate_row_words(board, dictionary) and validate_column_words(board, dictionary)


def count_letters(board):
    counts = collections.defaultdict(int)
    for row in board:
        for letter in row.replace("0", ""):
            counts[letter] += 1
    return counts


def count_contiguous_letters(viewed_letters, row, column, board, visited):
    if row < 0 or len(board) - 1 < row:
        return

    if column < 0 or len(board) - 1 < column:
        return

    if board[row][column] == '0':
        return

    if (row, column) in visited:
        return

    letter = board[row][column]
    viewed_letters[letter] -= 1

    visited.add((row, column))

    count_contiguous_letters(viewed_letters, row+1, column, board, visited)
    count_contiguous_letters(viewed_letters, row-1, column, board, visited)
    count_contiguous_letters(viewed_letters, row, column+1, board, visited)
    count_contiguous_letters(viewed_letters, row, column-1, board, visited)


def determine_disjoint(board):
    visited = set()
    center = len(board) / 2
    letter_count = count_letters(board)
    print letter_count
    count_contiguous_letters(letter_count, center, center, board, visited)
    print letter_count

    return all(count == 0 for count in letter_count.values())


if __name__ == '__main__':
    solutions = {}
    dictionary = generate_dictionary("dictionary.txt")
    board = generate_board("scrabble_board.txt")
    # print board
    # print validate_center(board)
    # print validate_all_words(board, dictionary)
    print(determine_disjoint(board))
