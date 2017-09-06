class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if (n <= 1):
            return
        
        k = 0   # Number of zeroes traversed so far
        
        for i in range(n):
            if (nums[i] == 0):
                k += 1
            else:
                if (k > 0):
                    nums[i - k] = nums[i]
        
        for i in range(n - k, n):
            nums[i] = 0