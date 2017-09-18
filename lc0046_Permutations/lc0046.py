class Solution(object):
    def _permute(self, unused, partial, res):
        """
        :type nums: List[int]
        :type unused: Set[int]
        :type partial: List[int]
        :type 
        """
        if (len(unused) == 0):  # A permutation is ready when all items are used
            res.append(partial)
            return
        
        unused_list = list(unused)
        
        for n in unused_list:
            unused.remove(n)
            self._permute(unused, partial+[n], res)
            unused.add(n)
        
        
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if (len(nums) == 0):
            return []
        
        partial = []
        res = []
        unused = set(nums)
        
        self._permute(unused, partial, res)
        
        return res
    
    
if __name__ == "__main__":
    sol = Solution()
    
    n = int(input("Number of integers: "))
    
    nums = list(range(1, n+1))
    
    print ("Original list:", str(nums))
    
    res = sol.permute(nums)    
    print ("All permutations:")
    for p in res:
        print (str(p))
    print ("# of permutations =", len(res))