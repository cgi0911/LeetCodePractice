class Solution(object):
    def _subsets(self, nums, start, partial, res):
        """
        :type nums: List[int]
        :type start: int
        :type partial: List[int]
        :type res: List[List[int]]
        """
        res.append(partial)
        
        n = len(nums)
        
        if (start >= n):
            return
        
        for i in range(start, n):
            self._subsets(nums, i+1, partial + [nums[i]], res)
        
        
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        partial = []
        
        self._subsets(nums, 0, partial, res)
        
        return res
    

if __name__ == "__main__":
    sol = Solution()
    
    n = int(input("Number of integers: "))
    nums = list(range(n))
    
    print ("Set of distinct integers:", str(nums))
    
    res = sol.subsets(nums)
    
    print ("All possible subsets:")
    
    for ss in res:
        print (str(ss))
        
    print ("Number of all possible subsets =", len(res))