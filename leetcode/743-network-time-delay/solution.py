"""
There are N network nodes, labelled 1 to N. Given times, a list
of travel times as directed edges times[i] = (u, v, w), where u
is the source node, v is the target node, and w is the time it
takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes
to receive the signal? If it is impossible, return -1.

Note:
- N will be in the range [1, 100].
- K will be in the range [1, N].
- The length of times will be in the range [1, 6000].
- All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.
---------------------------------
In: list of list of ints (times), int N (how many nodes), starting point (K)
Out: int, time it takes for each node to recieve the signal

- This question is basically asking "If we find the shortest past from K to every
other node in the graph, which path is the longest?"
- We can accomplish this with a modified Djikstra's algorithm; we initialize a shortest
path dictionary with each node mapped to inf, and then proceed to find the shortest path
to each node until we cannot reach any other nodes.
- If we don't visit every node, return -1. Otherwise, return the max value within our path dictionary.
----------------------------------
ndt(times, count, start):
  shortests = {i: inf for i from 1 to count inclusive; set k to 0}
  longest = -inf
  al = {node: list of edges with node as source, in (weight,label) format}
  # current distance, node label - each of these initialized to edge weight
  pq = heap(edges with k as source)
  visited = 0
  while(pq):
    distance, curr = pq.pop()
    visited += 1
    for child in al[curr]:
      child_distance = distance + child[0]
      if shortests[child] = inf:
        pq.push((child_distance, child))
      if distance < shortests[child]:
        shortests[child] = distance
        longest = max(distance, longest)

  if visited < count:
    return -1
  return longest
--------------------------------------------
- Made a dumb mistake about inputs; node A can have multiple edges to B. There's
a few ways we can handle this, but since we only need to consider the lowest-weight
edge, the easiest thing to do is filter these out during the creation of the adjacency list

- Shortest path from 3->1 is 3->5->4->1

- The issue I was having with this was that nodes were only added to the queue the first time they
were discovered; although nodes should never be visited twice, if a shorter path to a node is discovered
between the time when it is initially pushed and when the initial push would be popped, the shorter
path should be taken first. I had to adjust the algorithm to account for this by allowing multiple edges
leading to the same node to be on the priority queue as long as they didn't lead to nodes being revisited.

- _Djikstra's algorithm finds the shortest path to every node in the graph_.

- If you use heapq.heappop(), make sure to use heapq.heappush(), not list.append().
"""

import heapq

class Solution:
    def networkDelayTime(self, times, N, K):
        shortest_path = {i: float('inf') if i !=
                         K else 0 for i in range(1, N + 1)}
        visited = set()
        adj_list = {i: {} for i in range(1, N + 1)}
        for edge in times:
            src, dst, weight = edge
            if dst not in adj_list[src]:
              adj_list[src][dst] = weight
            else:
              adj_list[src][dst] = min(adj_list[src][dst], weight)
        pq = [(0, K)]

        while pq:
            distance, curr = heapq.heappop(pq)
            if curr in visited:
              continue
            visited.add(curr)

            for child in adj_list[curr]:
                weight = adj_list[curr][child]
                child_distance = distance + weight
                if child_distance < shortest_path[child]:
                    shortest_path[child] = child_distance
                    heapq.heappush(pq, (child_distance, child))

        longest = max(shortest_path.values())
        return [longest, -1][longest == float('inf')]


if __name__ == '__main__':
    s = Solution()
    assert s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert s.networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1) == 3
    assert s.networkDelayTime([[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]], 5, 3) == 59
    huge_graph = [[10,9,79],[15,10,58],[14,4,99],[14,12,29],[12,15,26],[1,15,78],[2,11,88],[7,3,4],[3,1,52],[11,3,91],[11,12,11],[5,10,81],[1,7,44],[12,13,52],[3,14,83],[10,4,26],[5,9,72],[5,14,32],[13,10,32],[15,6,2],[3,9,18],[1,11,45],[5,8,98],[7,13,33],[1,2,59],[4,11,79],[11,1,12],[8,5,79],[2,14,93],[3,6,53],[11,10,40],[14,2,33],[4,9,61],[3,8,10],[10,7,1],[8,3,58],[1,12,20],[5,1,51],[7,1,37],[9,7,34],[9,10,48],[8,4,90],[12,1,92],[6,4,99],[2,15,3],[2,3,80],[2,4,60],[15,14,75],[2,7,20],[15,8,20],[5,12,19],[13,3,74],[7,5,6],[9,6,73],[9,14,49],[15,1,56],[8,2,10],[7,9,9],[12,5,67],[6,3,29],[9,4,38],[6,9,42],[5,3,57],[3,2,48],[12,6,77],[10,15,15],[12,4,68],[14,1,52],[13,4,80],[4,1,84],[14,10,68],[2,12,81],[2,1,31],[6,14,52],[7,8,68],[4,12,73],[8,14,88],[13,5,92],[6,1,3],[9,11,80],[3,15,23],[15,4,84],[5,11,41],[7,11,42],[11,7,86],[9,15,63],[1,4,36],[3,13,82],[6,15,91],[13,6,64],[14,11,32],[11,5,68],[6,5,55],[4,5,35],[13,1,1],[4,10,47],[12,9,1],[7,10,44],[3,7,23],[8,12,68],[8,6,13],[2,9,19],[10,6,91],[7,12,80],[8,7,12],[4,7,4],[9,2,67],[14,9,29],[15,13,80],[6,8,62],[15,12,36],[1,3,48],[2,10,67],[9,13,55],[11,6,62],[8,11,92],[13,15,30],[4,13,97],[5,4,25],[4,2,9],[15,5,5],[15,2,45],[10,8,23],[14,5,43],[5,13,98],[14,13,73],[4,8,29],[10,5,0],[11,13,68],[9,12,91],[12,2,56],[9,1,23],[14,6,80],[9,5,10],[12,11,89],[5,15,94],[7,2,20],[3,12,89],[2,13,9],[11,2,1],[10,13,85],[6,10,76],[1,10,2],[14,15,20],[3,11,15],[11,8,62],[12,7,63],[8,15,91],[8,10,30],[12,3,80],[5,7,94],[13,2,60],[14,8,77],[10,12,67],[13,8,9],[13,11,48],[5,6,77],[10,3,51],[4,15,84],[13,12,10],[13,14,28],[4,6,46],[3,10,53],[14,7,48],[10,11,21],[15,11,99],[12,10,93],[11,14,73],[15,3,81],[2,5,22],[12,8,20],[6,13,24],[8,13,41],[8,9,98],[2,6,98],[7,15,27],[6,11,15],[7,14,72],[10,14,96],[1,8,18],[1,6,2],[3,4,78],[4,3,10],[11,4,54],[12,14,40],[3,5,63],[10,2,94],[1,9,57],[6,12,12],[9,8,37],[8,1,77],[13,7,80],[10,1,25],[9,3,37],[4,14,28],[1,13,88],[1,5,45],[7,4,65],[6,2,19],[11,15,37],[7,6,90],[2,8,1],[1,14,63],[5,2,47],[15,9,34],[11,9,41],[15,7,90],[13,9,45],[14,3,34],[6,7,44]]
    assert s.networkDelayTime(huge_graph, 15, 9) == 49