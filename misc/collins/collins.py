"""
This interview was a series of questions around writing a tool like
Collins: https://tumblr.github.io/collins/

Part 1:
Server IDs can be any value from 1 to 2**32. Given a list of allocated
server IDs, write a function that gets the lowest unused ID

In: list[int]
Out: int

Constraints:
  - IDs are always positive
  - IDs are between 1 and 2**32

Example:
In: [1,2,3,5,10,20]
Out: 4
Explanation: Server IDs 1,2,3 are allocated, but 4 is not, so it is the lowest available.
-----------------------------------------------
linear space approach:
- Cast ints to set
- set i to 0
- while i in set
    i++
- return i

constant space approach:
- In-place sort list
- set i to 0
- for each in list:
    - if i == each:
        i += 1
    - else:
        return i

Set: T: O(n), S: O(n)
Sorting: T: O(nlogn), S: O(c)

(Implemented in class below)
---------------------------------------------------------------------
Part 2:
Assume we are writing at Tracker() class to keep track
of server IDs and allocate / deallocate them. Additionally,
assume that we have multiple server types, each of which has
an independent list of IDs. Here's an average use story:
# >> tracker = Tracker()
# >> tracker.allocate('apibox')
# "apibox1"
# >> tracker.allocate('apibox')
# "apibox2"
# >> tracker.allocate('apibox')
# "apibox3"
# >> tracker.deallocate('apibox1')
# True
# >> tracker.deallocate('apibox')
# error/False/exception
# >> tracker.allocate('apibox')
# "apibox1"
# >> tracker.allocate('apibox')
# "apibox4"
# >> tracker.allocate('sitebox')
# "sitebox1"
# >> tracker.allocate('hello')
# "hello1"
# >> tracker.deallocate('helo2')
# Raise error
----------------------------------------------
"""

import collections

class Tracker:
    def __init__(self):
        self.servers = collections.defaultdict(list)

    def get_lowest_unused_id(self, server_ids):
        used_ids = set(server_ids) # TODO: store sets instead?
        lowest = 1
        while lowest in used_ids:
            lowest += 1
        return lowest

    def allocate(self, server_type):
        for char in sever_type:
            if char.isdigit():
                raise ValueError("Type cannot contain ints")

        lowest = self.get_lowest_unused_id(self.servers[server_type])
        self.servers[server_type].append(lowest)
        return server_type + str(lowest)


    def deallocate(self, server_name):
        server_type = []
        i = 0
        while servername[i].isalpha()
            server_type.append(char)
            i += 1
        server_type = ''.join(server_type)
        server_id = int(server_name[i:]) # this works, lalalalala

        if server_type not in self.servers:
            raise ValueError("Unknown server type.")
        if server_id not in self.servers[server_type]:
            raise ValueError("Unknown server id")

        self.servers[server_type].remove(server_id)
        return True
