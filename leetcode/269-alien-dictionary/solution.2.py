from typing import List


def create_letter_dag(words):
    """
    Create DAG by doing letter-by-letter
    comparisons on each word as described above.
    """
    # Every letter in given input should be added to the DAG
    all_letters = set()
    for word in words:
        all_letters |= set(word)
    successors = {letter: set() for letter in all_letters}

    # Word-by-word comparison to establish ordering
    prev = words[0]
    for word in words[1:]:
        i = 0
        shorter_len = min(len(prev), len(word))
        while i < shorter_len and prev[i] == word[i]:
            i += 1
        # Invalid: matched up until end of one, but shorter comes after
        if (i >= shorter_len and len(prev) > len(word)):
            return {}
        successors[prev[i]].add(word[i]) if i < shorter_len else None
        prev = word
    return successors


def visit(letter, dag, visited, ancestors, t_order):
    """
    Standard DFS for topological sort 
    """
    if letter in visited:
        return True
    if letter in ancestors or not dag:
        return False
    ancestors.add(letter)
    for child in dag[letter]:
        if not visit(child, dag, visited, ancestors, t_order):
            return False
    ancestors.remove(letter)
    visited.add(letter)
    t_order.append(letter)
    return True


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Create DAG from letters, then launch DFS and
        only return top ordering if we visit every 
        node without hitting a cycle.
        """
        dag = create_letter_dag(words)
        roots = set(dag.keys())
        for successors in dag.values():
            roots -= successors

        visited = set()
        t_order = []
        while roots:
            letter = roots.pop()
            if not visit(letter, dag, visited, set(), t_order):
                return ""
        return ''.join(t_order[::-1]) if len(t_order) == len(dag) else ""


s = Solution()
cases = [
    (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
    (["z", "x"], "zx"),
    (["z", "x", "z"], ""),
    (["abc", "ab"], ""),
    (["z", "z"], "z"),
    (["dvpzu", "bq", "lwp", "akiljwjdu", "vnkauhh", "ogjgdsfk", "tnkmxnj",
      "uvwa", "zfe", "dvgghw", "yeyruhev", "xymbbvo", "m", "n"], "")
]
for word_list, expected in cases:
    actual = s.alienOrder(word_list)
    assert actual == expected, f"{word_list}: {expected} != {actual}"
