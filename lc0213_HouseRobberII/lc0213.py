class Solution(object):
    def linearRob(self, nums):
        n = len(nums)
        
        if (n == 0):
            return 0
        
        imax = []
        global_max = 0
        
        for i in range(n):
            prev_max = 0
            if (i - 3 >= 0):    prev_max = max(prev_max, imax[i-3])
            if (i - 2 >= 0):    prev_max = max(prev_max, imax[i-2])
            curr_max = nums[i] + prev_max
            imax.append(curr_max)
            global_max = max(global_max, curr_max)
            
        return global_max
    
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Assume there are n houses, arranged in a circular manner, i.e.
        # houses[0] is a neighbor of houses[n-1].
        # 
        # Here we have two cases:
        #     Case 1: houses[0] is robbed, so houses[n-1] and houses[1]
        #             cannot be robbed. The rest are free to choose.
        #     Case 2: houses[0] is not robbed, so the rest are free to choose.
        #
        # This reduces the House Robber II problem down to House Robber I
        # problem, where the houses are arranged in a linear manner.
        # The total amount robbed will be:
        #   (nums[0] + linearRob(nums[2:n-1])) + linearRob(1:n-1)
        n = len(nums)
        
        if (n == 0):    return 0
        if (n == 1):    return nums[0]
        if (n == 2):    return max(nums[0], nums[1])
        
        return max(nums[0] + self.linearRob(nums[2:n-1]), self.linearRob(nums[1:]))
        
        
if __name__ == "__main__":
    sol = Solution()
    
    nums = [1, 3, 1]
    
    print (nums)
    print ("Max robbed =", sol.rob(nums))