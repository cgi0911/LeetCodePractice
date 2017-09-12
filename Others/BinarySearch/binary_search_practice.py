class Solution(object):
    def findFirst(self, nums, target):
        n = len(nums)            
        l, r = 0, n - 1
        
        while (l <= r):
            m = (l + r) // 2
            if ((m == 0 or nums[m] > nums[m-1]) and nums[m] == target):
                return m
            if (nums[m] < target):
                l = m + 1
            else:
                r = m - 1
                
        return -1
        
        
    def findLast(self, nums, target):
        n = len(nums)
        l, r = 0, n - 1
        
        while (l <= r):
            m = (l + r) // 2
            if ((m == n - 1 or nums[m] < nums[m+1]) and nums[m] == target):
                return m
            if (nums[m] > target):
                r = m - 1
            else:
                l = m + 1
        
        return -1
    
    
    def findMinRotated(self, nums):
        n = len(nums)
        l, r = 0, n - 1
        
        while (l < r):
            if (nums[l] < nums[r]):
                return l
            
            m = (l + r) // 2
            
            if (nums[l] <= nums[m]):
                l = m + 1
            else:
                r = m
        return 0
                

if __name__ == "__main__":
    sol = Solution()
    
    nums = [1, 1, 2, 2, 2, 3, 3, 5, 5, 6, 7, 8]
    target = 4
    
    print (nums)
    print ("First %d at %d" %(target, sol.findFirst(nums, target)))
    print ("Last  %d at %d" %(target, sol.findLast(nums, target)))
    
    n = 20
    nums2 = list(range(n))
    shift = 1
    nums2 = nums2[n-shift : n] + nums2[0 : n-shift]
    print (nums2)
    print ("Min at %d" %(sol.findMinRotated(nums2)))