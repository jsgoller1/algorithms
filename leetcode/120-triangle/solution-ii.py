"""
6/12/22

In: arr of arr; at least 1 subarr of length 1, each subarr is one longer than prev; each val in arr is in [-10000, 10000]
Out: int, minimum sum from top row to bottom
-----
- min path from row 1 to row 2 is not necessarily in min path from row 1 to 3
- not asked to keep track of path, just sum
- global sum will be combination of shortest path from step to step
    - keep track of shortest way to get to each layer from top to bottom; shortest way to get single top element is shortest global

pseudo(pyramid)
    if only one layer, return single element
    otherwise, start at n-1 layer:
        for ith item in n-1 layer, replace it with min(n-1[i]+n[i], n-1[i]+n[i+1])
    repeat until we get to 0th layer, return result 

requires extra storage equal to longest (bottom) layer; 

recursive(layer_idx, row_idx):
    if layer_id == n-1:
        return pyramid[layer_idx][row_idx]
    return min(pyramid[layer_idx][row_idx] + recursive(layer_idx+1, row_idx),
               pyramid[layer_idx][row_idx] + recursive(layer_idx+1, row_idx+1))
    
recursive approach easier to code but will require an intermediary stack frame
for each item in pyramid; 200(1+200)/2 = 20,000; will require recursion depth up to 200, but python default on leetcode is 550k
----
Minor adjustments; needed cache and some code reorg; took ~40min 

"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.cache = {}
        return self.recurse(triangle, 0, 0)
    
    def recurse(self, pyramid, layer_i, row_i):
        if layer_i == len(pyramid)-1:
            return pyramid[layer_i][row_i]
        if (layer_i, row_i) not in self.cache:     
            self.cache[(layer_i, row_i)] = min(pyramid[layer_i][row_i] + self.recurse(pyramid, layer_i+1, row_i),
                                               pyramid[layer_i][row_i] + self.recurse(pyramid, layer_i+1, row_i+1))
        return self.cache[(layer_i, row_i)] 