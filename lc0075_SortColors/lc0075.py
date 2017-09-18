import random
import time

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Intuitively we simply need to do a generic sorting (quicksort, etc.) to sort the colors, which
        # is of time complexity O(n log n).
        #
        # However, since there are only three colors red, white and blue (represented by integers 0, 1, 2, respectively),
        # we are able to do it in one pass, with time complexity O(n).
        
        n = len(nums)
        
        r, b = 0, n - 1     # Indices where we would like to put red and blue elements
        i = 0               # The iterator index
        
        while (i <= b):
            if (nums[i] == 0):
                nums[i], nums[r] = nums[r], nums[i]     # Swap to position r if we see a red object
                r += 1
                i += 1
                continue
            if (nums[i] == 2):
                nums[i], nums[b] = nums[b], nums[i]     # Swap to position b if we see a blue object
                b -= 1                
                # Since we may swap another blue object to position i, do not increment i here.
                continue
            i += 1  # If we see a white object, increment i.
                

if __name__ == "__main__":
    random.seed(time.time())
    sol = Solution()
    
    n = int(input("Number of elements: "))
    
    nums = [random.randint(0, 2) for i in range(n)]    
    
    print ("Original array:", str(nums))
    sol.sortColors(nums)
    print ("Sorted array:", str(nums))
                