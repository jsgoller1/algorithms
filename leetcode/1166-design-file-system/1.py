class FileSystem:

    def __init__(self):
        self.root = (None, {})

    def createPath(self, path: str, value: int) -> bool:
        path = [parent for parent in path.split("/") if parent != ""]
        val, children = self.root
        for parent in path[:-1]:
            if parent not in children:
                return False
            val, children = children[parent]
        if path[-1] in children:
            return False
        else:
            children[path[-1]] = (value, {})
            return True

    def get(self, path: str) -> int:
        val, children = self.root
        path = [parent for parent in path.split("/") if parent != ""]
        for parent in path:
            if parent not in children:
                return -1
            val, children = children[parent]
        return val


# Your FileSystem object will be instantiated and called as such:
fs = FileSystem()
creates = [
    ["/leet", 1, True],
    ["/leet/code", 2, True],
    ["/derp/herp", 4, False],
    ["/leet/code", 4, False],
]
for path, val, expected in creates:
    fs.createPath(path, val)
gets = [
    ["/leet", 1],
    ["/leet/code", 2],
    ["/derp/herp", -1],
]
for path, expected in gets:
    actual = fs.get(path)
    assert actual == expected, f"get {path}: {expected} != {actual}"
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
