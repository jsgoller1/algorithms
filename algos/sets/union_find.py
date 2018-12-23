"""
Implements a union-find, based on Skiena's description
in the Algorithm Design Manual. Skiena's implementation
only supports integers, and at that can only support
ranges of integers from 1 to n, which is not very useful
beyond the demonstrated use for Kruskal's algorithm. In
this implementation, I would like to be able to store
unspecified amounts and types of things, as well as
add() and remove() them.
"""


class union_find():
    """
    Implements a union-find data structure
    """

    def __init__(self, base_set):
        self.parent = {item: item for item in base_set}
        self.size = {item: 1 for item in base_set}

    def add(self, item):
        """
        Add an item to the union-find structure.
        """
        if item not in self.parent:
            self.parent[item] = item

    def remove(self, item):
        """
        Remove an item from the union-find structure. There are
        some tricky edge cases to handle here:
        - If the size of X's subtree is only 1,
        we can safely delete X.
        - Else:
        - If X has a parent, replace all of X's
        children with X's parent, then delete it.
        - If X is the root of its parent tree, then
        get its first child, make that the root, and
        then change all other children's parents to it.
        """
        if item not in self.parent:
            return

        if self.size[item] > 1:
            new_parent = None
            for child in self.parent:
                if child != item and self.parent[child] == item:
                    if new_parent == None:
                        new_parent = child
                        self.size[child] = self.size[item] - 1
                    self.parent[child] = new_parent

        del self.parent[item]
        del self.size[item]

    def find(self, item):
        """
        Obtain the root of an item's tree.
        """
        if item not in self.parent:
            raise ValueError("{0} not in union-find.".format(item))

        while self.parent[item] != item:
            item = self.parent[item]
        return item

    def same_component(self, item1, item2):
        return self.find(item1) == self.find(item2)

    def union(self, item1, item2):
        """
        Place two items in the same set by merging their trees
        together at the parent; this should really be called
        "join".
        """
        p1 = self.find(item1)
        p2 = self.find(item2)
        if self.size[p1] >= self.size[p2]:
            self.size[p1] += self.size[p2]
            self.parent[p2] = p1
        else:
            self.size[p2] += self.size[p1]
            self.parent[p1] = p2


if __name__ == '__main__':
    uf = union_find([i for i in range(15)])
    for i in range(2, 15):
        uf.union(1, i)
    uf.remove(1)
    uf.add(666)
    print(uf.parent)
    print(uf.find(2))
    print(uf.find(3))
