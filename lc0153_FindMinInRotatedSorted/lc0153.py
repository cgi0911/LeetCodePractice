class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)        
        l, r = 0, n - 1
        
        while (l < r):
            if (nums[l] < nums[r]):
                return nums[l]
            m = (l + r) // 2
            if (nums[m] > nums[r]):
                l = m + 1
            else:
                r = m
        return nums[l]
    

if __name__ == "__main__":
    sol = Solution()
    nums = list(range(1, 11))
    n = len(nums)
    shift = 2
    nums = nums[n-shift:] + nums[0:n-shift]
    
    print ("Original array: %s" %(str(nums)))
    print ("Minimum is %d" %(sol.findMin(nums)))