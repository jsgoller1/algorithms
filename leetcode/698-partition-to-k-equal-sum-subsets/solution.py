class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        nums.sort(reverse=True) 
        buck, kSum = [0] * k, sum(nums) // k
        
        def dfs(idx):
            if idx == len(nums): 
                return len(set(buck)) == 1 # every bucket sums to target
            for i in range(k):
                buck[i] += nums[idx]
                if buck[i] <= kSum and dfs(idx + 1): 
                    return True
                buck[i] -= nums[idx]
                if buck[i] == 0: 
                    break
            return False
        return dfs(0)

    
# Annotated and slower-but-clearer version of @jingkuan's solution based on @chemikadze's
# solution using @chengyuge925's solution.
class Solution:
    def canPartitionKSubsets(self, nums, k):
        buckets = [0]*k
        target = sum(nums) // k

        # We want to try placing larger numbers first
        nums.sort(reverse=True)


        # DFS determines which bucket to put the 'current element' (nums[idx] ) into
        def dfs(idx):
            # If we've placed all of the items, we're done;
            # check if we correctly made k equal subsets of 
            # size sum(nums) // k
            if idx == len(nums):
                return set(buckets) == set([target])

            # For each bucket
            for i in range(k):
                # Try adding the current element to it
                buckets[i] += nums[idx]

                # If it's a valid placement and we correctly placed the next element, we're
                # done placing the current element.
                if buckets[i] <= target and dfs(idx + 1):
                    return True

                # Otherwise, remove the current element from the ith bucket and 
                # try the next one. 
                buckets[i] -= nums[idx]

                # This is an optimization that is not strictly necessary. 
                # If bucket[i] == 0, it means:
                #   - We put nums[idx] into an empty bucket
                #   - We tried placing every other element after and failed.
                #   - We took nums[idx] out of the bucket, making it empty again. 
                # So trying to put nums[idx] into a _different_ empty bucket will not produce
                # a correct solution; we will just waste time (we place elements left to right,
                # so if this bucket is now empty, every one after it is too).
                #
                # Otherwise (bucket[i] > 0), we just go to the next bucket and 
                # try placing nums[idx] there. If none of them work out, we wind up
                # breaking out of the loop when range(k) ends and returning False. 
                if buckets[i] == 0:
                    break

            # We couldn't place the current element anywhere that 
            # leads to a valid solution, so we will need to backtrack
            # and try something else. 
            return False

        # Start by trying to place nums[0]
        return dfs(0)