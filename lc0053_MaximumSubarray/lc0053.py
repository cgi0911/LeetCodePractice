class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # This is a classic dynamic programming problem.
        # We iterate over nums[0] ... nums[n-1], when n = len(nums)
        # For each i, we record cumulative sum of a "positive-sum" subarray
        # ending at nums[i]. Obviously, c[i] = c[i-1] + nums[i]
        # However, if c[i] becomes zero, we know that it will only contribute
        # negatively to the cumulative sum. So we discard previous cumulative
        # sum and start over from zero.
        ret = float("-inf")
        
        c = 0
        
        for num in nums:
            c += num
            if (c > ret): ret = c
            c = max(c, 0)
                
        return ret
    

if __name__ == "__main__":
    sol = Solution()
    
    nums = [-2,1,-3,-4,-1,2,1,-5,4]
    print (nums)
    print ("Maximum subarray sum =", sol.maxSubArray(nums))