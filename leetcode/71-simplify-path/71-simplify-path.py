class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = [item for item in path.split("/") if item]
        stack = []
        for item in dirs:
            if item == ".":
                continue
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        return "/"+"/".join(stack)


s = Solution()
for i, case in enumerate([
    ("/home/", "/home"),
    ("/home/..", "/"),
    ("/home/...", "/home/..."),
    ("/", "/")

]):
    path, expected = case
    actual = s.simplifyPath(path)
    assert actual == expected, f"i - {path}: {actual} != {expected}"
