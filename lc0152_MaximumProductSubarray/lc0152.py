class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return 0
        
        ret = imax = imin = nums[0]
        
        for i in range(1, len(nums)):
            # If nums[i] is a negative number...
            if (nums[i] < 0):
                imax, imin = imin, imax
            
            imax = max(nums[i], nums[i] * imax)
            imin = min(nums[i], nums[i] * imin)
            
            ret = max(ret, imax)
        
        return ret
                
    
if __name__ == "__main__":
    sol = Solution()
    
    #nums = [2, 3, -2, 4]
    nums = [2, 3, -4, 5, 6, -4]
    #nums = [-2]
    print (nums)
    print ("Maximum product of all subarrays =", sol.maxProduct(nums))