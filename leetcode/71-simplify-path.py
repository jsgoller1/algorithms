"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
- path = "/home/", => "/home"
- path = "/a/./b/../../c/", => "/c"
- path = "/a/../../b/../c//.//", => "/c"
- path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory, so it can be ignored in a simplified path.
Additionally, a double period ("..") moves up a directory, so it cancels out whatever the last directory was. For more
information, look here: https://en.wikipedia.org/wiki/Path_(computing)#Unix_style
--------------------------------
In: string
Out: string

- This feels like a stack problem; going up a dir or down is like pushing or popping on a stack
- Could we split on '/', and then push each item on the stack, ignoring '.' and popping on '..'?
- What edge cases exist?
  - empty path
  - ////////////// -> /
  - "/a//b////c/d//././/.."
    - 'a', 'b', 'c', 'd', '.', '.' '..' -> /a/b/c/
    - could if we get a '..' on an empty stack, just ignore it; i.e. /home/joshua/../../../../../../etc is just '/etc/
-----------------------------
- split on '/'
- push items into stack:
  - ignore on '.'
  - pop on '..', ignore if empty
- finally, pop items from stack:
  - final = /popped + final
---
Strategy seems to work, but some corner cases:
  - what does "" mean? Should that be an empty string?
"""


class Solution(object):
    def simplifyPath(self, path):
        stack = []
        directories = [directory for directory in path.split('/') if directory]
        for directory in directories:
            if directory == '..':
                stack = stack[:-1]
            elif directory != '.':
                stack.append(directory)

        simplifiedPath = '/'
        while stack:
            simplifiedPath += stack[0]
            stack = stack[1:]
            if stack:
                simplifiedPath += '/'
        return simplifiedPath


if __name__ == '__main__':
    s = Solution()
    assert s.simplifyPath("/home/") == "/home"
    assert s.simplifyPath("////////") == "/"
    assert s.simplifyPath("") == "/"
    assert s.simplifyPath("/a/./b/../../c/") == "/c"
    assert s.simplifyPath("/a/../../b/../c//.//") == "/c"
    assert s.simplifyPath("/a//b////c/d//././/..") == "/a/b/c"
