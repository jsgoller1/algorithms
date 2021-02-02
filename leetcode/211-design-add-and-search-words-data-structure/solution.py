class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_leaf = False


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = TrieNode()
                node.children[letter] = new_node
                node = new_node
        node.is_leaf = True

    def _search(self, word, i, node):
        if i == len(word):
            return node.is_leaf
        if word[i] == ".":
            for child in node.children.values():
                if self._search(word, i+1, child):
                    return True
            return False
        if word[i] not in node.children:
            return False
        return self._search(word, i+1, node.children[word[i]])

    def search(self, word: str) -> bool:
        return self._search(word, 0, self.root)


null, true, false = None, True, False
cases = [
    [
        ["addWord", "addWord", "search", "search", "search", "search", "search", "search", "search", "search"],
        [["a"], ["ab"], ["a"], ["a."], ["ab"], [".a"], [".b"], ["ab."], ["."], [".."]],
        [null, null, true, true, true, false, true, false, true, true]
    ]
]
wd = WordDictionary()
for commands, args, expecteds in cases:
    for i, _ in enumerate(commands):
        command = commands[i]
        arg = args[i][0]
        expected = expecteds[i]
        if command == "addWord":
            wd.addWord(arg)
        else:
            actual = wd.search(arg)
            assert expected == actual, f"{command,arg}: {expected} != {actual}"
