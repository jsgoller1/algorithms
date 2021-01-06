"""
In his 2012 algos lecture series, Skiena demonstrates an O(n+m) algorithm for topological sorting a
graph with n nodes and m vertices by using the incoming degrees of the nodes (i.e. number of incoming
edges for each node), except he did it on the whiteboard and not on the slide deck / SMART board,
so I couldn't see how it worked. Can we re-derive his algorithm, and do better?

procedure top_order(adjacency_list)
  1) Start with an adjacency list representation of a graph.
    - if 1 maps to [2,3,4] in the adj list, it means 1 has outgoing edges to 2,3, and 4.

  2) Determine the incoming degrees of each node O(n + m)
  - Initialize an empty dict incoming_degree
  - For each node in the adj list, go through its adjacency list
    and increment the incoming_degree of each adjacent node
  - Initialize the queue with all nodes whose incoming degree is zero

  3) Remove nodes until our topological order is established, O(n+m)
  - Initialize empty list top_order
  - While the queue is nonempty:
    - Dequeue a node called curr
    - Decrement the incoming degree of each adjacent node to curr in the adjacency list
      - if any of these are set to zero, enqueue them
    - Append curr to top_order
    - delete curr from incoming_degrees

  4) Return top_order, unless incoming_degrees is nonempty (meaning a cycle occurred)

-----------------------
Let's say we have the graph:
1 -> 2    6 -> 8
|    |    ^    |
v    V    |    V
3 -> 4 -> 5 -> 7 -> 9
"""
import collections


def topological_sort(adj_list):
    """
    :type adj_list: dict, maps node_idx -> list[node_idxs]
    :rtype top_order: list[int], contains node idxs in topological ordering
    """
    # Establish incoming degrees, O(n + m)
    incoming_degree = collections.defaultdict(int)
    for node in adj_list.keys():
        incoming_degree[node] = 0 if node not in incoming_degree else incoming_degree[node]
        for adj_node in adj_list[node]:
            incoming_degree[adj_node] += 1

    # Determine topological ordering, O(n+m)
    top_order = []
    queue = collections.deque(
        [node for node in incoming_degree.keys() if incoming_degree[node] == 0])
    while queue:
        curr = queue.popleft()
        for adj_node in adj_list[curr]:
            incoming_degree[adj_node] -= 1
            if incoming_degree[adj_node] == 0:
                queue.append(adj_node)
        top_order.append(curr)
        del incoming_degree[curr]

    if incoming_degree != {}:
        raise ValueError(
            'Cycle detected in adjacency list; no topological ordering possible.')
    return top_order


if __name__ == '__main__':
    empty_adj_list = {}
    print(topological_sort(empty_adj_list))

    adj_list = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: [5],
        5: [6, 7],
        6: [8],
        7: [9],
        8: [7],
        9: []
    }
    print(topological_sort(adj_list))

    # If we now add links that make it into a cycle, the top sort fails
    adj_list[9].append(10)
    adj_list[10] = [8]
    print(topological_sort(adj_list))
