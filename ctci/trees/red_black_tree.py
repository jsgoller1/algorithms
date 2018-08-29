import random

class red_black_node:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

class rb_tree:
    def __init__(self):
        self.root = None
        self.empty = True

    def insert(self, key, value):
        self.__insert(self.root, key, value)

    def __insert(self, root, key, val):
        if root is None: # First insertion
            # print "Setting root key " + str(key) + " to " + str(val)
            self.root = red_black_node(key, val)
        elif root.key < key:
            if root.right is None:
                # print "Setting key " + str(key) + " to " + str(val)
                root.right = red_black_node(key, val)
            else:
                self.__insert(root.right, key, val)
        else:
            if root.left is None:
                # print "Setting key " + str(key) + " to " + str(val)
                root.left = red_black_node(key, val)
            else:
                self.__insert(root.left, key, val)

    def retrieve(self, key):
        return self.__retrieve(self.root, key)

    def __retrieve(self, root, key):
#        print "At " + str(root.key) + " with key " + str(key)
        if (key > root.key):
            if root.right:
#                print "Traversing right..."
                return self.__retrieve(root.right, key)
            else:
#                print "Key " + str(key) + " is greater than " + str(root.key) + " but the right subtree is empty!"
                return None
        elif key < root.key:
            if root.left:
#                print "Traversing left..."
                return self.__retrieve(root.left, key)
            else:
#                print "Key " + str(key) + " is smaller than " + str(root.key) + " but the left subtree is empty!"
                return None
        else:
#            print "At correct node, returning value " + root.value + "..."
            return root.value

    # DFS methods
    def traverse_preorder(self, expected):
        print "Preorder traversal"
        print "Expected sequence: " + expected
        print "==================="
        self.__traverse_preorder(self.root)

    def __traverse_preorder(self, root):
        print root.key, root.value
        if root.left:
            self.__traverse_preorder(root.left)
        if root.right:
            self.__traverse_preorder(root.right)

    def traverse_inorder(self, expected):
        print "In-order traversal"
        print "Expected sequence: " + expected
        print "==================="
        self.__traverse_inorder(self.root)

    def __traverse_inorder(self, root):
        if root.left:
            self.__traverse_inorder(root.left)
        print root.key, root.value
        if root.right:
            self.__traverse_inorder(root.right)

    def traverse_postorder(self, expected):
        print "Postorder traversal"
        print "Expected sequence: " + expected
        print "==================="
        self.__traverse_postorder(self.root)

    def __traverse_postorder(self, root):
        if root.left:
            self.__traverse_postorder(root.left)
        if root.right:
            self.__traverse_postorder(root.right)
        print root.key, root.value

    # TODO: BFS
    def traverse_levelorder(self, root):
        pass

if __name__ == '__main__':
    # The below is ugly and I apologize in advance to my future self. Basically,
    # populate the tree with this dict of values and use a random number for the key
    # then randomly retrieve one of them. There's a lot of icky casting so we don't
    # have to know the key value before it's randomly generated - the tree is a bit
    # more convincingly functional this way.
    rbt = rb_tree()
    values = ['aleph', 'bet', 'gimmel', 'daled', 'hei', 'vav', 'zayin']
    keys = [3, 1, 2, 0, 5, 6, 4 ]
    for key in keys:
        rbt.insert(key, values[key])
        print "Inserted (k/v): ", key, values[key]
    lookup_val = random.randint(0, len(values)-1)
    ascii_tree ="""
                 3
              1    5
            0  2  4  6
    """
    print ascii_tree
    print "Retrieving", values[lookup_val], "at key", lookup_val
    print "Retrieved", rbt.retrieve(lookup_val)
    rbt.traverse_preorder("3 1 0 2 5 4 6")
    # Postorder:
    rbt.traverse_postorder("0 2 1 4 6 5 3")
    rbt.traverse_inorder("0 1 2 3 4 5 6")
