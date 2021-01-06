import collections
"""
Suppose we wanted to design a hashtable that could keep track of key-value pairs
that might change over time. The hashtable should support the following operations:

set(key, value, timestamp)
get(key, timestamp)

get() and set() should be have as expected, but also enforce the idea that "the key is set to the
value at the given time". We should be able to execute get() on a given key and get the most recently
set value for the given timestamp, or None if the key hadn't been set before that time.

set(k1,v1, 0)
set(k2, v2, 3)
set(k1, v2, 4)
get(k1, 0) # returns v1
get(k1, 4) # returns v2
get(k1, 3) # gets most recently set value before or equal to this time; returns 0
get(k2, 1) # returns None, as k2 had not been set at time 1
"""


class time_travel_hashmap():
    def __init__(self):
        self.hashmap = collections.defaultdict(dict)

    def get(self, key, timestamp):
        timestamps = sorted(self.hashmap[key].keys())
        val = None
        for ts in timestamps:
            if ts <= timestamp:
                val = self.hashmap[key][ts]
            else:
                break
        return val

    def put(self, key, value, timestamp):
        self.hashmap[key][timestamp] = value


if __name__ == "__main__":
    tsh = time_travel_hashmap()
    tsh.put('k1', 'v1', 1)
    print(tsh.get('k1', 1))
    tsh.put('k1', 'v2', 6)
    print(tsh.get('k1', 6))
    print(tsh.get('k1', 4))
    print(tsh.get('k1', 0))
    tsh.put('k1', 'v3', 6)
    print(tsh.get('k1', 6))
    print(tsh.get('k1', 4))
    print(tsh.get('k1', 0))
