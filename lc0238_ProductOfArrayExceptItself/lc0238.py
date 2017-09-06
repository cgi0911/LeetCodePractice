class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ret = [1] * n
        
        if (n <= 1):    return 1
        
        l_prod = 1
        r_prod = 1
        
        for i in range(0, n):
            ret[i] = l_prod
            l_prod *= nums[i]
            
        for i in range(n - 1, -1, -1):
            ret[i] *= r_prod
            r_prod *= nums[i]
            
        return ret