# programming-problems
Solutions to all of my [LeetCode problems](https://leetcode.com/jsgoller1/), programming competition and interview questions, and some algorithms / data structures implemented for practice.


## 2018 Goal
I am attempting to complete a total of 15 programming contests and 150 LeetCode problems in 2018 (30 easy, 80 medium, 40 hard), with at least 20 problems solved using dynamic programing (a friend once advised `don't assume dynamic programming is "too hard" for you until you've solved 20 problems using it`). I am counting contest problems towards my total problem count.

## Current progress: 120/150
- Easy: 31/30
- Medium: 77/80
- Hard: 12/40
- Contests (virtual): 8
  - LeetCode: #87, #100, #105, #112, #98, #89, #82
  - CodeForces: #511
- Dynamic programming: 22/20

### Problems to reattempt (viewed solution)
#### Couldn't complete myself
  - #11: tried multiple failed approaches over a few days
  - #31: Looked at related topics dropdown and discussion titles; consulted Skiena (14.4) then Knuth (7.2)
  - #94: Have not ever implemented in-order or post-order DFS for trees, looked them up on Wikipedia
  - #647: trying to understand DP
  - #750: already had correct algorithm minus one detail.
  - #790: trying to understand DP
  - #894: wasn't familiar enough with array representations of trees
  - #904: didn't look at solution, but checked "related topics" and saw "two pointers"
  - #920: thought the problem required hard combinatorics knowledge (was also a contest problem)

#### Contest problems (I tend to always read solutions after a contest)
  - #825 (LeetCode Weekly #82)
  - #888 (LeetCode Weekly #98)
  - #898 (LeetCode Weekly #100)
  - #918 (LeetCode Weekly #105)
  - #945 (LeetCode Weekly #112)
  - #947 (LeetCode Weekly #112)

### Problems to revisit / improve
  - #2 probably has an in-place solution
  - #5 has a linear time solution (Manacher's algorithm)
  - #37 took 1.6 seconds and only beat 6% of solutions
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

## How I work on programming problems
I follow a modified form of [Polya's problem solving method](https://math.berkeley.edu/~gmelvin/polya.pdf) that I call `SUPER`:
* **State the problem**
  * What are you trying solve?
  * What is the expected input? What is the expected output?
  * What constraints exist on the input? How large can it be? What range of values is expected?
  * What is the expected performance of the solution? What complexity classes are allowable?
* **Understand the problem**
  * What cases _could_ occur, even if you don't expect them? List some of them. Is a null/empty input possible? What about a singleton input?
  * What work _must_ you do? Do you have to look at every portion of the input? Is there a way to avoid doing unnecessary work?
  * Does the problem feel like it can be "boiled down" to a common type of problem? Are there obviously usable data structures or algorithms (e.g. graph search, stacks, etc) that could be used to make the solution trivial?
* **Plan your approach**
  * Write pseudocode, with above in mind.
  * Consider how your approach might fail with edge cases; try performing your pseudocode by hand on a few and seeing if it can be corrected.
* **Execute your approach**
  * Once you are 90% confident about your approach, create some test cases, implement the approach in real code, and run it against them.
* **Review your answer**
  * Who else has solved this problem? How performant is their solution?
  * Does your solution do any work it shouldn't? Are you creating any intermediary data structures (especially accidentally) that are hurting performance?
  * How short can you make your code without making it unreadable?
  * Are you reinventing the wheel? Can you rely more on standard libraries or lanaguage primatives?

When I get stuck on a problem, I will usually do the following things in order:
  - Try multiple approaches, sometimes over several days.
  - If discussuions exist (LeetCode problem discussions, forum posts, etc.), check the titles (but not the bodies) of the posts; the title can be a helpful clue , e.g. `concise Java DP approach` or `Python 12 lines, O(n^2 * m)`.
  - Google to see if it would be hard to solve without
  having learned about it first, e.g. [Manacher's algorithm](https://en.wikipedia.org/wiki/Longest_palindromic_substring) for longest palindromic substrings or the [longest common subsequence problem](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem).
  - Look at hints, if any are given.
  - Ask a friend for advice.
  - Finally, if all else fails, look at the solution and mark the problem below for reattempting later.

I typically review the solutions to contest problems after the contest ends, unless I'm pretty sure I can finish them with more time.
