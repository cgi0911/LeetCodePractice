# Refer to http://www.geeksforgeeks.org/longest-increasing-subsequence/

class Solution(object):
    def __init__(self):
        self.global_max = -1
        self.lookup = {}
    
    def _lengthOfLIS(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        # Consider the subproblem: denote the max length of LIS ending at nums[i] by L[i]
        # L[i] = L[j] + 1 if j < i and nums[j] <= nums[i]
        # L[i] = 1 if no such j exists
        
        # Already stored
        if (n in self.lookup):
            return self.lookup[n]
        
        # Base case: LIS ending with nums[0]
        max_lis_for_n = 1
        if (n == 0):            
            max_lis_for_n = 1
                
        # For n > 1, we scan through L[i], i = 0 .. n-1
        # For each i, we check two conditions: 1. this i yields highest LIS length
        # 2. nums[i] <= nums[n]
        else:
            for i in range(0, n):
                max_lis_for_i = self._lengthOfLIS(nums, i)
                if (nums[i] < nums[n]):
                    max_lis_for_n = max(max_lis_for_n, max_lis_for_i + 1)

        self.lookup[n] = max_lis_for_n
        self.global_max = max(self.global_max, max_lis_for_n)
        
        #print ("L[%d] = %d" %(n, max_lis_for_n))
        return max_lis_for_n
        
        
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return 0
        
        else:
            self._lengthOfLIS(nums, len(nums) - 1)
            return self.global_max
        

if __name__ == "__main__":
    sol = Solution()
    
    nums = range(5000)
    print ("Original array:", nums)
    print ("Max LIS length:", sol.lengthOfLIS(nums))
        