from test_framework import generic_test


"""
Allowed chars:
- . (current path)
- .. (parent dir)
- / (subdir)
- alphanum (dir name)
- empty (same as .)

cases:
    - empty
    - /////// -> / 
    - / -> / 
    - /../.. -> /
    - ../.. -> ../..
    - derp -> derp
    - /derp -> /derp
    - /derp/.. -> /
    - derp/.. -> empty? 
    - derp/../.. -> ..

- Paths can be absolute (begin at '/') or relative (begin at current dir)
- for abspaths, / is highest parent; any '..' from '/' yields '/'
- for relpaths, each '..' either pops the last known dir, or appends '..' 
"""


def shortest_equivalent_path_first(path: str) -> str:
    """
    - is absolute? (first char)
    - split path on '/' 
    - keep stack
    - for each item in path list:
        - if char is ., skip it
        - if item is alphanum, push it
        - if item is ..:
            - if dir is absolute, pop if stack is nonempty, else skip
            - if dir is rel, pop if stack is nonempty and stack top not .., else push  
    - return joined stack; prepend '/' is absolute path
    """
    if not path:
        return path
    absolute = path[0] == '/'

    stack = []
    dirs = [item for item in path.split('/') if item]
    for item in dirs:
        if item == "..":
            if absolute and stack:
                stack.pop()
            elif not absolute and (not stack or stack[-1] == ".."):
                stack.append(item)
            elif not absolute and stack and stack[-1] != "..":
                stack.pop()
        elif item == ".":
            continue
        else:
            stack.append(item)

    return ("/" if absolute else "") + "/".join(stack)


def shortest_equivalent_path(path: str) -> str:
    if not path:
        return path

    stack = []
    for item in (item for item in path.split('/') if (item and item != ".")):
        if item == "..":
            if stack and (path[0] == '/' or stack[-1] != ".."):
                stack.pop()
            else:
                stack.append(item)
        else:
            stack.append(item)

    return ("/" if path.startswith('/') else "") + "/".join(stack)


if __name__ == '__main__':
    cases = [
        ("", ""),
        ("///////", "/"),
        ("/", "/"),
        ("/../..", "/"),
        ("../..", "../.."),
        ("derp", "derp"),
        ("/derp", "/derp"),
        ("/derp/..", "/"),
        ("derp/..", ""),
        ("derp/../..", "..")
    ]
    for path, expected in cases:
        actual = shortest_equivalent_path(path)
        assert actual == expected, f"{path}: {actual} != {expected}"

    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
