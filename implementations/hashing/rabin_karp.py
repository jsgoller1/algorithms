"""
Hashing method based on the Rabin-Karp substring algorithm, as referenced
in The Algorithm Design Manual, chapter 12.1 about dictionaries.
"""


class linked_list_node():
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = None


class hash_table():
    def __init__(self, size=100):
        self.table = [None for i in range(size)]

    def rk_hash(self, string):
        hashval = 0
        for i, char in enumerate(string):
            hashval += 256 ** (len(string) - i + 1) * ord(char) % len(string)
        return hashval % len(self.table)

    def _get_node(self, key):
        ll = self.table[self.rk_hash(key)]
        while ll and ll.key != key:
            ll = ll.next
        if not ll:
            raise KeyError
        return ll

    def insert(self, key, value):
        try:
            ll = self._get_node(key)
            ll.value = value
        except KeyError:
            hashval = self.rk_hash(key)
            self.table[hashval] = linked_list_node(
                key, value, self.table[hashval])

    def get(self, key):
        return self._get_node(key).value


if __name__ == '__main__':
    ht = hash_table()
    ht.insert("foo", "bar")
    print(ht.get("foo"))
    ht.insert("foo", "baz")
    print(ht.get("foo"))
