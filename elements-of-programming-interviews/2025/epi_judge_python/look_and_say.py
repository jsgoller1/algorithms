from test_framework import generic_test


def next_element(string):
    new_string = []
    i, curr, count = 0, string[0], 0
    while i < len(string):
        if string[i] == curr:
            count += 1 
        else: 
            new_string.append(str(count) + curr)
            curr = string[i]
            count = 1
        i += 1
    return ''.join(new_string + [str(count) + curr])

def look_and_say(n: int) -> str:
    count = 1
    string = '1'
    while count < n: 
        string = next_element(string)
        count += 1 
    return string 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
