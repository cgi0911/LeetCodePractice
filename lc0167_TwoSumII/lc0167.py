class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        myDict = {}
        
        # Create a dict mapping numbers to their indices
        for i in range(len(numbers)):
            if not numbers[i] in myDict:
                myDict[numbers[i]] = []
            myDict[numbers[i]].append(i)
            
        # Iterate over the numbers list for num1, and its index
        # Since we know that num1 + num2 == target, we know number1 <= target / 2
        # Then we lookup number2 in myDict
        for idx1 in range(len(numbers)):
            num1 = numbers[idx1]
            if num1 > target/2:
                return [-1, -1]     # We no we have no num1 choices
            num2 = target - num1
            if num2 in myDict:
                for idx2 in myDict[num2]:
                    if idx2 > idx1:
                        return [idx1 + 1, idx2 + 1]     # The problem asked for non zero-based indices
                    
        return [-1, -1] # No available pairs found