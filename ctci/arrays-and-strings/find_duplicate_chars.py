"""
Test if a string contains duplicates.
"""

def test_duplicates(string):
    if len(string) in [0, 1]:
        return False
    # the string necessarily has duplicates if it has more characters than the alphabet
    if len(string) > 26:
        return True
    string = string.upper()
    lookup = [False for x in range(26)] #array for all chars from A to Z
    try:
        for each in string:
            hash_key = ord(each)-65-1 # ord('A') is 65, correct for zero-indexed array
            if lookup[hash_key] == False:
                lookup[hash_key] = True
            elif lookup[hash_key] == True:
                return True
        return False
    except IndexError: #ord returns a value outside of the alphabet
        return -1

if __name__ == '__main__':
    tests = ['abracadabra', 'joshua', 'mergesort', 'metamorphosis', '', 'aaaaaaaaa', 'fobargiz']
    for each in tests:
        ret = test_duplicates(each)
        if ret == -1:
            print each+": contains unsupported characters"
        else:
            print each+": "+str(ret)
