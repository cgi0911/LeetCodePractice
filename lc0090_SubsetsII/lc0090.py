import random
import time

class Solution(object):
    def _subsetsWithDup(self, nums, start, partial, res):
        """
        :type nums: List[int]
        :type start: int
        :type partial: List[int]
        :type res: List[List[int]]
        :rtype: void
        """
        res.append(partial)
        
        n = len(nums)
        
        if (start >= n):
            return  # No next item to choose
        
        last = float("inf") # An impossible element
        
        for i in range(start, n):
            if (nums[i] == last):
                continue
            last = nums[i]
            self._subsetsWithDup(nums, i+1, partial + [nums[i]], res)   # Recursive call
        
    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        partial = []
        
        self._subsetsWithDup(sorted(nums), 0, partial, res) # Sort nums so that duplicates will be adjacent
        
        return res
    

if __name__ == "__main__":
    random.seed(time.time())
    sol = Solution()
    
    n = int(input("Input number of integers: "))
    nums = [random.randint(1, n) for i in range(n)]
    
    print ("nums =", str(nums))
    print ("sorted(nums) =", str(sorted(nums)))
    
    res = sol.subsetsWithDup(nums)
    
    print ("All possible subsets:")
    for ss in res:
        print (str(ss))
    print ("Number of subsets =", len(res))