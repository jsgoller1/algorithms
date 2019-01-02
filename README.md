# programming-problems
Solutions to all of my [LeetCode problems](https://leetcode.com/jsgoller1/), programming competition and interview questions, and some algorithms / data structures implemented for practice.

## 2019 Goal
I am attempting to complete a total of 52 programming contests and 300 online problems in 2019 (having already done 120 problems and 8 contests already). I am counting contest problems towards my total problem count.
### Current progress
#### Problems: 121/420
  - LeetCode: 121
#### Contests (virtual): 8/60
  - LeetCode: #87, #100, #105, #112, #98, #89, #82
  - CodeForces: #511

## Problems to revisit
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
#### Contest problems
  - #825 (LeetCode Weekly #82)
  - #888 (LeetCode Weekly #98)
  - #898 (LeetCode Weekly #100)
  - #918 (LeetCode Weekly #105)
  - #945 (LeetCode Weekly #112)
  - #947 (LeetCode Weekly #112)
#### Can be improved
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

## What I do when I get stuck on a problem (in order)
  1. Try multiple approaches, sometimes over several days.
  1. If discussuions exist (LeetCode problem discussions, forum posts, etc.), check the titles (but not the bodies) of the posts; the title can be a helpful clue , e.g. `concise Java DP approach` or `Python 12 lines, O(n^2 * m)`.
  1. Google to see if it would be hard to solve without
  having learned about it first, e.g. [Manacher's algorithm](https://en.wikipedia.org/wiki/Longest_palindromic_substring) for longest palindromic substrings or the [longest common subsequence problem](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem).
  1. Look at hints, if any are given.
  1. Ask a friend for advice.
  1. If it's a dynamic programming problem, consider the advice below.
  1. Finally, if all else fails, look at the solution and mark the problem below for reattempting later.

  I typically review the solutions to contest problems after the contest ends, unless I'm pretty sure I can finish them with more time.

## Stuck on dynamic programming?
Don't fret - dynamic programming is hard to grasp at first, and everyone struggles with it (including me)! I did the following things to learn dynamic programming:
- Watch Steve Skiena's lectures on YouTube about DP from his 2012 algorithms class.
- Read the DP chapter in _The Algorithm Design Manual_.
- Read these Wikipedia articles:
  - [Recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science))
  - [Dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming)
  - [Optimal substructure](https://en.wikipedia.org/wiki/Optimal_substructure)
  - [Overlapping subproblems](https://en.wikipedia.org/wiki/Overlapping_subproblems)
  - [Longest common subsequence](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)
  - [Wagner-Fischer Algorithm](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm)
  - [Partition problem](https://en.wikipedia.org/wiki/Partition_problem#Pseudo-polynomial_time_algorithm)
  - [Djikstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Dynamic_programming_perspective)
- Try 20 dynamic programming problems on LeetCode / HackerRank / etc., even if you need to look at the solution; the best advice I ever heard about mastering DP was `don't assume dynamic programming is "too hard" for you until you've solved 20 problems using it`.
- Take Bradfield School of Computer Science's Problem Solving with Algorithms and Data Structures class, if you can.

