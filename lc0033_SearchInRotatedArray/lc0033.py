class Solution(object):
    def findMin(self, nums):
        """
        Search the index of min element in a rotated sorted array
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n - 1
        
        while (l < r):
            if (nums[l] < nums[r]):
                return l
            m = (l + r) // 2
            if (nums[m] > nums[r]):
                l = m + 1
            else:
                r = m
        return l    # l == r
                
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        
        # First, search the index of min element in the array
        offset = self.findMin(nums)
        print ("Offset =", offset)
        
        # Then we do a normal binary search
        l, r = 0, n - 1
        
        while (l <= r):
            m = (l + r) // 2
            if (nums[(m+offset)%n] == target):
                return ((m + offset) % n)
            if (nums[(m+offset)%n] < target):
                l = m + 1
            else:
                r = m - 1
        
        return -1   # Target not found
    
    
if __name__ == "__main__":
    sol = Solution()
    
    #n, shift, target = 10, 5, 4
    #nums = list(range(n))
    #nums = nums[n-shift:] + nums[0:n-shift]
    nums = [3, 1]
    target = 1
    
    print ("Array: %s" %(str(nums)))
    print ("Target: %d" %(target))
    print ("Position of target: %d" %(sol.search(nums, target)))