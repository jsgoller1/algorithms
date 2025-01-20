from test_framework import generic_test

"""
Normal way to do this: 
    - split based on "/"
    - for each item:
        - push if not ., ..
        - skip .
        - pop on ..
    - join via "/", prepend / if abspath, return 

What is the expectation for handling relpaths with .. beyond original, i.e.
"foo/bar/../../.."? Should that return ".."? 
    - let's assume yes for now 
    - odd cases:
        - foo/bar/../../../baz -> ../baz 
        - foo/bar/../../../baz/../.. -> ../..
        - for abspath, push '..' to empty stack and don't pop it?
"""

def shortest_equivalent_path(path: str) -> str:
    if not path:
        return ''
    is_abspath = path[0] == '/'
    dirs = [dirname for dirname in path.split("/") if dirname not in set(["", "."])]
    stack = []
    for dirname in dirs:
        if dirname == ".." and is_abspath:
            if stack:
                stack.pop()
        elif dirname == ".." and not is_abspath:
            if stack and stack[-1] != "..":
                stack.pop()
            else:
                stack.append(dirname)
        else:
            stack.append(dirname)
    return ("/" if is_abspath else "") + '/'.join(stack)

for path, shortest in [
    ("", ""),
    ("/", "/"),
    ("..", ".."),
    ("/../../../..", "/"),
    ("../../..", "../../.."),
    ("/../../../../foo", "/foo"),
    ("/foo/bar/baz", "/foo/bar/baz"),
    ("/foo/../bar", "/bar"),
    ("foo/../bar", "bar"),
    ("foo/../../bar", "../bar")
]:
    actual = shortest_equivalent_path(path)
    assert shortest == actual, f"{path}: {shortest} != {actual}"

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
