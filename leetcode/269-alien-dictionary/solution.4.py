"""
Topological ordering is only possible on a DAG; this question asks
"can we build a dag" from the words. 

Lexicographical ordering means that:
- words are sorted vertically
- if two words have same first n chars, they're sorted by the n+1 char

We can build our DG by going two words at a time, then check for cycles by DFSing from every node using
white/grey/black strategy for cycle detection and visiting each node at most once.  
"""


class Visited:
    def __init__(self):
        self.total = set()
        self.per_dfs = set()

    def reset_for_dfs(self):
        self.per_dfs = set()


class Solution:
    def constructGraph(self, words):
        graph = {c: [] for c in words[0]}
        word1_i, word2_i = 0, 1
        while word2_i < len(words):
            word1, word2 = words[word1_i], words[word2_i]
            # Ensure every letter in dictionary is represented in our graph
            for c in word2:
                graph[c] = [] if c not in graph else graph[c]

            # Find first non-matching pair of letters and add edge from c1
            # to c2
            if len(word1) > len(word2) and word1.startswith(word2):
                return False, {}

            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    graph[c1].append(c2)
                    break
            word1_i, word2_i = word1_i + 1, word2_i + 1

        return True, graph

    def hasCycles(self, graph, curr_c, visited, top_order):
        if curr_c in visited.total:
            return False
        if curr_c in visited.per_dfs:
            print(
                f"Found cycle. Visited {curr_c}; curr dfs visited is {visited.per_dfs}"
            )
            return True
        visited.per_dfs.add(curr_c)
        for next_c in graph[curr_c]:
            if self.hasCycles(graph, next_c, visited, top_order):
                return True
        visited.per_dfs.remove(curr_c)
        visited.total.add(curr_c)
        top_order.append(curr_c)
        return False

    def alienOrder(self, words: List[str]) -> str:
        valid_graph, graph = self.constructGraph(words)
        if not valid_graph:
            return ""

        visited = Visited()
        top_order = []
        for c in graph.keys():
            visited.reset_for_dfs()
            if self.hasCycles(graph, c, visited, top_order):
                return ""
        return "".join(top_order[::-1])
