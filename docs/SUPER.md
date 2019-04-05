# The SUPER heuristic
This is the process I follow when I solve contest or interview programming problems, but it is also useful for software engineering in general. It is based on [Polya's problem solving method](https://math.berkeley.edu/~gmelvin/polya.pdf). The entire process can be captured in two steps:
- `DO NOT TRY SOLVING PROBLEMS YOU DO NOT UNDERSTAND.`
- `DO NOT WRITE CODE UNTIL YOU HAVE A PLAN.`

## State the problem
  * What are you trying solve?
  * What is the expected input? What is the expected output?
  * What constraints exist on the input? How large can it be? What range of values is expected?
  * What is the expected performance of the solution? What complexity classes are allowable?
  * For interviews and real-life problems: what is the expected usage pattern of the code you will write? Who will use it? How will they use it? Will it be an isolated function or a library in a larger codebase? How likely is it you will need to extend your solution to cover more cases once the initial ones are covered?

## Understand the problem
  * Try listing small inputs and what their correct output should be. If the input size can be between 0 and 10^6, try solving n=3, n=4, and n=5 by hand and seeing if a common pattern emerges.
  * Try drawing a picture. Really.
  * What cases _could_ occur given the problem statement, even if you don't expect them? List some of them. Is a null/empty input possible? What about a singleton input?
  * What work _must_ you do? Do you have to look at every portion of the input? Is there a way to avoid doing unnecessary work?
  * Does the problem feel like it can be "boiled down" to a common type of problem or problem you already solved? If the problem as stated is too complicated, try solving a simpler problem or reducing complexity and seeing if you can build off of that.
  * Are there obviously usable data structures or algorithms that could be used to make the solution trivial?
    * Avoid framing questions like `is this a dynamic programming problem` as opposed to `can I use dynamic programming here` - many problems can be solved by multiple approaches.
    * Try running through this list of approaches, asking some of the provided questions:
      * Linked lists
      * Array with two pointers / sliding window
      * Stack - `Should processing occur in last-in, first-out order?`
      * Queues - `Should processing occur in first-in, first out order?`
      * Trees - `Is there an obvious parent-child relationship? Can I exclude half the input data at each step?`
      * Graphs - `If I frame the problem using a graph, what would the nodes represent? What would the edges represent? Would it be directed? Cyclic? Weighted?`
      * Backtracking / exhaustive search - `Should I try every possible answer? Is it possible I might get to a partial answer but go down a wrong path and need to bail out?`
      * Dynamic programming - `Does a recurrence exist? Am I seeing that bigger cases are combinations of smaller cases?`
        * Some good clues that DP might work include prompts like `find the minimum number of ways` or `find the longest of many`, especially when the output doesn't require an explicit answer (e.g. if the question is `find the length of the longest common subsequence between two strings`, and the required output is the length, not the LCS itself).
      * Recursion - `What is my base case / termination condition? When do I need to recurse?`
      * Math - `Is there some simple equation that describes the problem and explicitly calculates the answer?`
      * Sorting - `Is the problem simpler to think about if the input is always in some order?`
      * Randomization - `Is the problem simpler to think about if the input is _never_ in any order? Does this remove some bad edge cases?`
      * Binary - `Can I represent the input or state with a bit string? As I evaluate the input, is a core question "do I include this part or not?" Can binary operations like XOR or AND be used to simplify mutating state?`

## Plan your approach
  * With above in mind, write pseudocode or a bulleted list of steps in plain language.
  * Try a few normal cases by hand.
  * Consider how your approach might fail with edge cases; try performing your pseudocode by hand on a few and seeing if it can be corrected.

## Execute your approach
  * Once you are 90% confident about your approach, create some test cases, implement the approach in real code, and run it against them.

## Review your answer
  * Who else has solved this problem? How performant is their solution?
  * Does your solution do any work it shouldn't? Are you creating any intermediary data structures (especially accidentally) that are hurting performance?
  * How short can you make your code without making it unreadable?
  * Are you reinventing the wheel? Can you rely more on standard libraries or lanaguage primatives?

**What I do when I get stuck on an interview/contest problem (in order)**
  1. Try multiple approaches, sometimes over several days.
  1. If discussions exist (LeetCode problem discussions, forum posts, etc.), check the titles (but not the bodies) of the posts; the title can be a helpful clue , e.g. `concise Java DP approach` or `Python 12 lines, O(n^2 * m)`.
  1. Google to see if it would be hard to solve without
  having learned about it first, e.g. [Manacher's algorithm](https://en.wikipedia.org/wiki/Longest_palindromic_substring) for longest palindromic substrings or the [longest common subsequence problem](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem).
  1. Look at hints, if any are given.
  1. Ask a friend for advice.
  1. If it's a dynamic programming problem, consider the advice below.
  1. Finally, if all else fails, look at the solution and mark the problem below for reattempting later.
