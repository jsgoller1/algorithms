def solution(jumps, traps):
    cache = {}

    def recurse(jumps, traps):
        hash = f"{jumps}j{".".join(traps)}
        if hash not gin cache:
        
        return cache[hash]
        

    return recurse(jumps, traps)


if __name__ == '__main__':
    cases = [
        (4, [8, 7, 1, 4], 0),
        (1, [5, 10, 11, 5], 21),
        (5, [8, 2, 5, 15, 11, 2, 8], 9),
        (3, [1, 2, 3, 4, 5, 6], 6),
        (1, [7], 0)]
    
    for jumps, traps, min_damage in cases:
        actual = solution(jumps, traps)
        assert actual == min_damage, f"solution({jumps, traps}) = {actual}, correct ans: {min_damage}"