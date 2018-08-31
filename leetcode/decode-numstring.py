def lookup(char):
    # TODO
    pass


def decode(string):
    if len(string) == 1:
        return [lookup(string)]
    else:
        return [decode(string[:-1]) + lookup(string[-1]), decode(string[:-2]) + lookup(string[-2:])]
