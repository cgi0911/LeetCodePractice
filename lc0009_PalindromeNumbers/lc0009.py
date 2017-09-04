class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False    # Negative number is not a palindrome
         
        rev = 0
        last = 0

        while (rev < x):
            last = x
            rev = rev * 10 + x % 10
            x = int(x / 10)
            
        return (rev == x or rev == last)
    

if __name__ == "__main__":
    sol = Solution()
    x = 121
    print (x, "\n%s" %(sol.isPalindrome(x)))
            