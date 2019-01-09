# programming-problems
Solutions to all of my [LeetCode problems](https://leetcode.com/jsgoller1/), programming competition and interview questions, and some algorithms / data structures implemented for practice. Problems that I need to reattempt are listed in `unsolved/unsolved.md`.

## 2019 Goal
I am attempting to complete a total of 52 programming contests and 300 online problems in 2019 (having already done 120 problems and 8 contests in 2018). I am counting contest problems towards my total problem count.
### Current progress
#### Problems: 129/420
  - LeetCode: 127
    - Easy: 32
    - Medium: 81
    - Hard: 16
#### Contests (virtual): 8/60
  - LeetCode: #87, #100, #105, #112, #98, #89, #82
  - CodeForces: #511

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
* **What I do when I get stuck on a problem (in order)**
  1. Try multiple approaches, sometimes over several days.
  1. If discussuions exist (LeetCode problem discussions, forum posts, etc.), check the titles (but not the bodies) of the posts; the title can be a helpful clue , e.g. `concise Java DP approach` or `Python 12 lines, O(n^2 * m)`.
  1. Google to see if it would be hard to solve without
  having learned about it first, e.g. [Manacher's algorithm](https://en.wikipedia.org/wiki/Longest_palindromic_substring) for longest palindromic substrings or the [longest common subsequence problem](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem).
  1. Look at hints, if any are given.
  1. Ask a friend for advice.
  1. If it's a dynamic programming problem, consider the advice below.
  1. Finally, if all else fails, look at the solution and mark the problem below for reattempting later.

## Struggling with dynamic programming?
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

