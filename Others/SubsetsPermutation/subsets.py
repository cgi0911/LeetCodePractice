import time
import random

class Solution(object):
    def _SubsetsWithoutDup(self, nums, start, partial, res):
        """
        Recursive routines of SubsetsWithoutDup.
        :type nums: List(int)
        :type start: int
        :type partial: List(int)
        :type res: List(List(int))
        :rtype: void, results are appended to res
        """
        res.append(partial)
        
        n = len(nums)        
        if (start >= n):
            # We've reached end of array. return.             
            return
        
        for i in range(start, n):
            self._SubsetsWithoutDup(nums, i+1, partial + [nums[i]], res)
        
        
    def SubsetsWithoutDup(self, nums):
        """
        Given an integer array, in which all elements are unique, return all
        possible unordered subsets formed by elements in this array.
        :type nums: List(int)
        :rtype: List(List(int))
        """
        ret = []    # A list to store all result subsets
        partial = []
        
        self._SubsetsWithoutDup(sorted(nums), 0, partial, ret)
            # Use sorted(nums) so that the results will be sorted
            
        return ret
        
        
        
    def _SubsetsWithDup(self, nums, start, partial, res):
        """
        Recursive routines of SubsetsWithoutDup.
        :type nums: List(int)
        :type start: int
        :type partial: List(int)
        :type res: List(List(int))
        :rtype: void, results are appended to res
        """
        res.append(partial)
        
        n = len(nums)
        if (start >= n):
            # We've reached end of array. Return.
            return
        
        last = None # Record last element we've traversed
        for i in range(start, n):
            if (nums[i] == last):   continue
                # This is important. For each round of recursive call,
                # we allow only 'one' of a sequence of duplicated elements
                # to be included in the results. By doing this we can
                # ensure unique results.
            last = nums[i]
            self._SubsetsWithDup(nums, i+1, partial + [nums[i]], res)
            
        
    def SubsetsWithDup(self, nums):
        """
        Given an integer array, in which duplicated elements may be included,
        return all possible unique unordered subsets formed by elements in this array.
        :type nums: List(int)
        :rtype: List(List(int))
        """
        ret = []    # A list to store all result subsets
        partial = []
        
        self._SubsetsWithDup(sorted(nums), 0, partial, ret)
            # Use sorted(nums) so that 1. duplicated elements will be adjacent
            # 2. results will be sorted as well.
            
        return ret
    
    
if __name__ == "__main__":
    random.seed(time.time())
    sol = Solution()
    
    hasDup = int(input("Has duplications? (1/0) "))
    n = int(input("Number of integers: "))
    
    nums = []
    if (hasDup == 0):
        nums = list(range(1, n+1))
    else:
        nums = [random.randint(1, n) for i in range(n)]
        
    print ("Original array sorted:")
    print (str(sorted(nums)))
    
    res = []
    if (hasDup == 0):
        res = sol.SubsetsWithoutDup(nums)
    else:
        res = sol.SubsetsWithDup(nums)
        
    print ("All subsets from the array elements:")
    for ss in res:
        print (str(ss))
        
    print ("Number of subsets =", len(res))