class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return path
        is_abs = path[0] == "/"
        stack = []
        dirs = [item for item in path.split("/") if item]
        for subdir in dirs:
            if subdir == "..":
                if len(stack) and stack[-1] != "..":
                    stack.pop()
                elif not is_abs:
                    stack.append(subdir)
            elif subdir == ".":
                continue
            else:
                stack.append(subdir)
        return ("/" if is_abs else "") + "/".join(stack)


s = Solution()
cases = [
    ("", ""),
    ("/home/", "/home"),
    ("home/", "home"),
    ("/../../../home/", "/home"),
    ("../../../home/", "../../../home"),
    ("../home/../../home/", "../../home")

]
for path, expected in cases:
    actual = s.simplifyPath(path)
    assert actual == expected, f"{expected} != {actual}"
