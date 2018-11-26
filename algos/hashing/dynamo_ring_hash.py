#!/bin/python
"""
Suppose you have a hash ring with 26 keys set (A:1, B:2, C:3, ..., Z:26) stored across 4 nodes. If
a 5th node were to join the ring randomly, how would you rebalance keys?

Secondly, suppose that instead of each node being responsible for keys up to the next node in the ring,
we replicated keys to the following K nodes - for example, if the order on the ring is node n1, n2, n3, n4
and K = 2, then if "cat = 1" is written to n1, it must also be written to n2 and n3.

This was written while trying to figure out ring hashing for Shriek (https://github.com/jsgoller1/shriek) based
on Dynamo's ring hash (specifically around preference lists).
---

Rebalancing plan:

Suppose we have a 4-partition ring, with partition ids 0, .25, .5, and .75.
When we add a key to our ring, the owner is determined by "sliding forward"
to the nearest node greater than or equal to the key - if we were to insert
"cat=foo" and hash(cat) = .73, then "cat=foo" would belong to node id .75,
as it is the first node whose id comes after the hash in the ring.

Suppose we wanted to add a new partition with id .85 (and that there is no
replication of keys; each key belongs to exactly one node). To rebalance the
keys, we would need to:
- find the nearest node (0) after our new node's id.
- obtain all keys in that node (e.g. copy and delete from it) whose hashes
are less than our new value (.85 and below)

When we have a replication strategy akin to Dynamo's where multiple
nodes own a single key, rebalancing also has to account for keys
that would be owned by a different node but are replicated to our new
node; if our 4-partition ring had a replication factor of 3, then node .85
would be responsible for a key that hashes to .24. Our new rebalancing
strategy to account for this is:

- Copy all keys from the nearest node (0) to the new node (.85)
- For each key k:
  - if .85 is on k's preference list, delete it from the node that was
  previously last on k's preference list
  - if .85 is not on the preference list, delete the key from .85.


Example:
Replication factor: 2
Keys: .20, .25, .55, .75, .90
Nodes: 0, .25, .5, .75

If we had a replication factor of 2, the key distribution would be:
(0): .55, .75, .90
(.25): .20, .25, .90
(.5): .20, .25,
(.75): .55, .75

If we add a new node (.85), then the new key distribution should be:
n1 (0): .90
n2 (.25): .20, .25, .90
n3 (.5): .20, .25,
n4 (.75): .55, .75
n5 (.85): .55, .75
"""

import zlib
import random


class RingHash():
    def __init__(self, partition_count=1, replication_factor=1):
        self.partition_count = max(partition_count, 1)
        self.replication_factor = min(
            max(replication_factor, 1), partition_count)
        self.ring_size = 1000  # 2**32
        self.partition_size = int(self.ring_size / partition_count)
        self.partitions = {}
        self.partition_ids = []

        for i in range(partition_count):
            partition_id = self.partition_size * i
            self.partitions[partition_id] = {}
            self.partition_ids.append(partition_id)

    def get_owners(self, key_hash):
        """
        Get all partitions that own a key
        """

        # Get first owner by walking ring backwards
        first_owner = 0
        for part_id in self.partition_ids[::-1]:
            if part_id > key_hash:
                first_owner = part_id
        first_owner_index = self.partition_ids.index(first_owner)

        # Get all following partitions mod ring size
        owners = []
        for i in range(self.replication_factor):
            partition_index = (first_owner_index+i) % self.partition_count
            owners.append(self.partition_ids[partition_index])

        return owners

    def add_partition(self, new_partition_id=None):
        """
        Add a partition to the partition list and rebalance the keys.
        See above for the rebalancing technique. If partition is not
        given or is invalid, randomly choose a new one.
        """

        while ((new_partition_id == None)) or (new_partition_id in self.partition_ids):
            new_partition_id = random.randint(0, self.ring_size)

        # Find the nearest partition
        nearest_part_id = self.get_owners(new_partition_id)[0]
        nearest_part = self.partitions[nearest_part_id]

        # Insert new partition into list so we can generate correct preference lists
        new_partition = {}
        self.partition_ids.append(new_partition_id)
        self.partition_ids.sort()
        self.partitions[new_partition_id] = new_partition

        # Create the new partition from keys in nearest partition
        for key in nearest_part.keys():
            key_hash = self.hash(key)
            pref_list = self.get_owners(key_hash)
            if new_partition_id in pref_list:
                new_partition[key] = nearest_part[key]

        # Delete new partition's keys from last owner
        # in old pref list; this must be done separately
        # to prevent attempting to modify a list while
        # using it for iteration
        for key in new_partition.keys():
            key_hash = self.hash(key)
            pref_list = self.get_owners(key_hash)
            last_owner = self.partition_ids.index(pref_list[-1])
            old_last = last_owner + 1 if last_owner < self.partition_count-1 else 0
            old_last_id = self.partition_ids[old_last]
            del self.partitions[old_last_id][key]
        print("Added new partition with id {0}".format(new_partition_id))
        print("="*100)

    def hash(self, key):
        """
        Hashing function for ring position
        """
        return zlib.crc32(key.encode()) % self.ring_size

    def hash_set(self, key, val):
        """
        Set a key in the ring
        """
        key_hash = self.hash(key)
        owners = self.get_owners(key_hash)
        for owner_id in owners:
            partition = self.partitions[owner_id]
            partition[key] = val

    def hash_get(self, key):
        """
        Get a key in the ring
        """
        owners = self.get_owners(key)
        return self.partitions[owners[0]][key]

    def show_key_owners(self, key):
        """
        Given a key, print all partitions that own it
        """
        owners = self.get_owners(key)
        owner_str = "key {0} on partitions: {1}".format(key, owners)
        print(owner_str)

    def show_partitions(self, show_keys=False):
        """
        Display all currently set keys and existing partitions
        """
        for i, part_id in enumerate(self.partition_ids):
            print("-" * 10)
            print("partition {0} (id {1})\n".format(i, part_id))
            if show_keys:
                partition = self.partitions[part_id]
                for key in partition.keys():
                    print("{0} ({1}) = {2}".format(
                        key, self.hash(key), partition[key]))
        print("="*100)


if __name__ == '__main__':
    # Establish ring hash
    PARTITION_COUNT = 10
    REPLICATION_FACTOR = 3
    rh = RingHash(PARTITION_COUNT, REPLICATION_FACTOR)

    # Set some keys and display them
    # Create A:1, B:2, C:3, etc. mappings
    # keys = {chr(i): i-64 for i in range(65, 91)}
    # for key in keys:
    #    rh.hash_set(key, keys[key])

    rh.hash_set('Joshua', 'Goller')
    rh.hash_set('Michael', 'McLoughlin')
    rh.hash_set('Rachel', 'Zilberg')
    rh.show_partitions(True)

    rh.add_partition(150)

    rh.show_partitions(True)
