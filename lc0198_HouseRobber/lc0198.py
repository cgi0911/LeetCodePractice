class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        global_max = 0
        imax = []
        
        for i in range(n):
            prev_max = 0
            if (i - 3 >= 0):    prev_max = max(prev_max, imax[i-3])
            if (i - 2 >= 0):    prev_max = max(prev_max, imax[i-2])
            curr_max = prev_max + nums[i]
            imax.append(curr_max)
            global_max = max(global_max, curr_max)
        
        return global_max
    

if __name__ == "__main__":
    sol = Solution()
    
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print (nums)
    print ("Max amount robbed =", sol.rob(nums))