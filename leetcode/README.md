# leetcode

## TODO: general review
- 56: https://leetcode.com/problems/merge-intervals/description/
- 42: https://leetcode.com/problems/trapping-rain-water/
- 59: https://leetcode.com/problems/spiral-matrix-ii/
- 301: https://leetcode.com/problems/remove-invalid-parentheses/
- 489: https://leetcode.com/problems/robot-room-cleaner/

## TODO: Topological sort review 
- 207: https://leetcode.com/problems/course-schedule/
- 210: https://leetcode.com/problems/course-schedule-ii/
- 269: https://leetcode.com/problems/alien-dictionary/

## TODO: Union Find review
Some of these can be done easily with BFS/DFS
- 130: https://leetcode.com/problems/surrounded-regions/
- 200: https://leetcode.com/problems/number-of-islands/
- 305: https://leetcode.com/problems/number-of-islands-ii/description/
- 695: https://leetcode.com/problems/max-area-of-island/
- 827: https://leetcode.com/problems/making-a-large-island/

## TODO: sweep line algorithms
- 149-max-points-on-a-line.py

## TODO: unsolved or resolve
- 4: I did solve this one without looking at the answer, but in nlogn time when a log(n) solution was required. It worked but I looked at the solution afterwords to see the log(n) technique.
- 5-longest-palindromic-substring-manacher.py
- 11: tried multiple failed approaches over a few days
- 31: Looked at related topics dropdown and discussion titles; consulted Skiena (14.4) then Knuth (7.2)
- 94: Have not ever implemented in-order or post-order DFS for trees, looked them up on Wikipedia
- 126-word-ladder-ii.py
- 297-serialize-deserialize-binary-tree.py
- 301-remove-invalid-parentheses
- 309-best-time-to-buy-and-sell-stock-with-cooldown.py
- 417-pacific-atlantic-flow.py: Looked at titles, got to a solution that misses only one cell on the last test case but does almost exactly what every other solution does.
- 516-longest-palindromic-subsequence.py
- 560-subarray-sum-equals-k.py: looked at unhelpful hint
- 647: trying to understand DP
- 720-longest-word-in-dictionary.py
- 748-shortest-completing-word.py
- 750: already had correct algorithm minus one detail.
- 790: trying to understand DP
- 797-all-paths-from-source-to-target.py
- 825-friends-of-appropriate-ages.py
- 854-k-similar-strings.py
- 855-exam-room.py
- 862-shortest-subarray-with-sum-at-least-k.py
- 889-construct-binary-tree-from-preorder-and-postorder-traversal.py
- 891-sum-of-subsequence-widths.py
- 894: wasn't familiar enough with array representations of trees
- 904: didn't look at solution, but checked "related topics" and saw "two pointers"
- 919-complete-binary-tree-inserter.py
- 920-number-of-music-playlists.py: thought the problem required hard combinatorics knowledge (was also a contest problem)

## TODO: improvement
- #2 probably has an in-place solution
- #4 needs to be redone because I did an O(n*log(n)) solution when I should've done an O(log(n)) one
- #5 has a linear time solution (Manacher's algorithm)
- #37 took 1.6 seconds and only beat 6% of solutions
- #76 only beat .99% of solutions
- #94 can be implemented using threaded BSTs / Morris traversal
- #130 only beat #17.26% of solutions
- #133 only beat 16% of solutions
- #138 has a O(c) space solution
- #148 is technically not O(c) for space because it uses recursion (thereby relying on the stack)
- #207 has a solution that does not involve deleting nodes from the graph
- #238 has a O(c) space solution that I sketched out but didn't implement
- #329 only ran faster than 2% of solutions despite having an O(mn) solution (best for that problem)
- #378 was solved with a brute force solution, and has a O(N) solution for an N x M matrix; see [this solution](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85170/O(n)-from-paper.-Yes-O(rows).) and [this paper](http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf)
- #665 has a linear space solution
- #861 should be redone with goroutines
