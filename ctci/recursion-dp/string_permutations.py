import sys
import ipdb

def get_permutations(string):
    if len(string) == 1:
        return [string]
    else:
        perms = []
        small_perms = get_permutations(string[:-1])
        for each in small_perms:
            perms += all_possible_inserts(each, string[-1])
        return perms


def all_possible_inserts(string, char):
    inserts = []
    for position in range(len(string)+1):
        inserts.append(string[0:position]+char+string[position:len(string)])
    return inserts

if __name__ == '__main__':
    print get_permutations(sys.argv[1])
