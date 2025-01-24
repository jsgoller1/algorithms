"""
This was a TPS question I got for implementing a k/v store
that supports lookups of historic key values. Part 1 was
just the basic implementation of a k/v store, part 2 was the historic lookup.
A followup question I got as "how would you insert at a particular time other than
the current" - this would involve using bisect_left() and inserting at that index 
or overwriting the entry there if it was the same timestamp. 

Part 1: 

Constraints:
    - Types: generic just hashables to values
    - Size: fits in memory; key size is not concern
    - Unbounded size of hashtable otherwise
"""
import copy

# TODO: Type hints
class KeyValueStore:
    def __init__(self):
        self._data = {}
    
    def add(self, key, value):
        self._data[key] = value
        
    def get(self, key):
        # TODO: use dict.get()?
        if key in self._data:
            return self._data[key]
        return None
        
    def delete(self, key):
        if key in self._data:
            del self._data[key]
        
    
# Test cases
# NOTE: normally do setup/teardown of individual KV stores for each test case; 
# reusing same one here for expediency
kvstore = KeyValueStore()
# Add nonexisting
kvstore.add("foo", "bar")
assert "foo" in kvstore._data and kvstore._data["foo"] == "bar"

# Add existing (update)
kvstore.add("foo", "bar")
kvstore.add("foo", "baz")
assert "foo" in kvstore._data and kvstore._data["foo"] == "baz"

# Get nonexisting
assert "nonexisting" not in kvstore._data and kvstore.get("nonexisting") is None

# Get existing
assert kvstore.get("foo") == "baz"

# Delete nonexisting
data_copy = copy.deepcopy(kvstore._data)
assert kvstore.delete("nonexisting") is None
assert kvstore._data == data_copy, f"Delete nonexisting mutated underlying store"

# Delete existing
assert kvstore.delete("foo") is None
assert "foo" not in kvstore._data

"""
Part 2:

Use map of key -> list of tuples [(timestamp, value)]
Use binary search on timestamp for historic values
Otherwise, add new timestamp/value pairs to array (add), get last from array (get most recent)
.delete() deletes entire array and key 
"""
from collections import defaultdict
from bisect import bisect_left
from time import time_ns


# TODO: used named tuples in lists for clarity 
class HistoricKVStore:
    def __init__(self):
        # key -> [(time1, value1), (time2, val2), ...]; val2 is more recent than val1
        self._data = defaultdict(list)
    
    def add(self, key, value):
        self._data[key].append((time.time_ns(), value))
        
    def get(self, key):
        if key in self._data:
            # Get last entry from historic data, then get value from tuple
            return self._data[key][-1][1]
        return None
        
    # NOTE: Assume no concurrent entries (i.e. two entries for same time)
    def get_at_effective_date(self, unix_timestamp: int, key):
        if key not in self._data:
            return None        
    
        arr = self._data[key]
        
        # Skip search for edge case on ts greater than last
        if unix_timestamp > arr[-1][0]:
            return arr[-1][1]
            
        idx = bisect_left(arr, unix_timestamp, key=lambda entry: entry[0])
        entry = arr[idx]                
        if idx == 0:
            # Special edge case for first item; if timestamp is before first entry,
            # return none 
            return None if unix_timestamp < arr[idx][1] else arr[idx][1]

        # Otherwise, return given entry on exact match or previous one if timestamp is before 
        return arr[idx-1][1] if unix_timestamp < arr[idx][1] else arr[idx][1]


    def delete(self, key):
        if key in self._data:
            del self._data[key]


# Test cases (skipping add/get/delete per prompting)
kvstore = HistoricKVStore()
kvstore._data["foo"] = [(2,2),(4,4), (5,5), (6,6)]
kvstore._data["bar"] = [(2,2)]

# Get effective date for nonexistent key
#assert kvstore.get_at_effective_date(1, "nonexistent") == None

# Get effective date for key, key existed at given time (time exact)
assert kvstore.get_at_effective_date(4, "foo") == 4
assert kvstore.get_at_effective_date(2, "bar") == 2, f"{kvstore.get_at_effective_date(2, 'bar')}"

# Get effective date for key, key existed at given time (time not exact match)
assert kvstore.get_at_effective_date(3, "foo") == 2,  f"{kvstore.get_at_effective_date(3, 'foo')}"
assert kvstore.get_at_effective_date(5, "bar") == 2

# Get effective date for key, key did not exist at time 
assert kvstore.get_at_effective_date(1, "foo") == None
assert kvstore.get_at_effective_date(1, "bar") == None
