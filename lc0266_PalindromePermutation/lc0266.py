class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mySet = set()
        
        for c in s:
            if (c in mySet):
                mySet.remove(c)
            else:
                mySet.add(c)
                
        return (len(mySet) <= 1)