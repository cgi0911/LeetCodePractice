import random

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myDict = {}

        # Create a map that maps number to its position (ID)
        for i in range(len(nums)):
            if not nums[i] in myDict:
                myDict[nums[i]] = []
            myDict[nums[i]].append(i)

        # Now search for a pair that adds up to target
        for i in range(len(nums)):
            n = nums[i]
            m = target - n
            if m in myDict:
                for q in myDict[m]:
                    if q != i:
                        return [i, q]

        return [-1, -1]


if __name__ == "__main__":
    sol = Solution()

    #nums = random.sample(range(20), 20)
    #target = 20

    #print (nums)
    print (sol.twoSum([3, 2, 4], 6))