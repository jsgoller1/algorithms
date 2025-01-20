"""
Initial plan:
    - start island id at 1, count at 0
    - go through positions. each time an island is added with no neighbors, 
      fill its cell with island id and bump count.
    - if an island is added and it has a neighbor, count each neighbor cell with different IDs. Overwrite them
      with new island's ID (bfs/dfs), and reduce island count for number of islands joined 
    - return island count at end
Flaws:
    - Doing bfs/dfs overwrites can have pathological edge case devolving to O((n x m)^2) - imagine a case where 
      positions contains every cell in the grid, in incrementing order ([0,0], [0,1], [0,2], ...)

Better approach:
    - Initialize UF that uses Union by rank, also island id and count
    - For each position, fill with id:
        - If filled in with no neighbors, add 1 to count and increment id 
        - If neighbors, union them. Only decrement count if filled cell has 2 or more neighbors, since we're joining them
            - will need to check roots of all neighbors (edge case: c shaped island with new cell making it into a ring)
    - should be O(n x m) for space, not sure on time; we could need to do union/find for each cell as described above. 
"""



class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        pass
