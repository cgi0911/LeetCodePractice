class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)        
        
        if (n == 0):
            return [-1, -1]
            
        # Search for the first occurrence of target
        l, r = 0, n - 1
        while (l < r):
            m = int((l + r) / 2)
            if (nums[m] < target):
                l = m + 1
            elif (nums[m] == target):
                r = m
            else:
                r = m - 1
        
        if (nums[l] != target):
            return [-1, -1] # Target not found
        
        st = l
        
        # Search for the last occurrence of target
        l, r = 0, n - 1
        while (l < r):
            m = int((l + r + 1) / 2)
            if (nums[m] < target):
                l = m + 1
            elif (nums[m] == target):
                l = m
            else:
                r = m - 1
        
        return [st, r]

    
if __name__ == "__main__":
    sol = Solution()
    #nums = [5,7,7,8,8,10]
    #target = 8
    nums = [2, 2]
    target = 1
    
    print (str(sol.searchRange(nums, target)))