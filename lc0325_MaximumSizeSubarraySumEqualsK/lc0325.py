class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Note that sum(nums[i...j]) = sum(nums[0...j]) - sum(nums[0...i-1])
        # (Inclusive of i and j)
        # We can iterate through nums. For each index i, we compute sum(nums[0...i])
        # We store it in a dict, where the key is sum(nums[0...i]) and value
        # is a list of indices i.
        # We can also lookup whether (k - sum(nums[0...i])) is in the dict
        # If yes, we derive the subarray length and compare against maximum
        max_len = 0
        res_dict = {0: [-1]}
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            if (curr_sum in res_dict):
                res_dict[curr_sum].append(i)
            else:
                res_dict[curr_sum] = [i]
            
            if ((curr_sum - k) in res_dict):
                index_list = res_dict[curr_sum - k]
                for idx in index_list:
                    curr_len = i - idx
                    max_len = max(curr_len, max_len)
        
        print (res_dict)
        
        return max_len
    
    
if __name__ == "__main__":
    sol = Solution()
    
    nums = [1, -1, 5, -2, 3]
    k = 3
    max_len = sol.maxSubArrayLen(nums, k)
    print ("nums = ", str(nums))
    print ("maxSubArrayLen(nums, %d) = %d" %(k, max_len))