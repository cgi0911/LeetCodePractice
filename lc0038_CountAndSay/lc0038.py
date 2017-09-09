class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if (n <= 0):
            return "0"
        
        if (n == 1):
            return "1"
        
        s = self.countAndSay(n - 1)
        last_digit = s[0]
        last_count = 1
        digits = []
        counts = []
        
        for i in range(1, len(s)):
            if (s[i] == last_digit):
                last_count += 1
            else:
                digits.append(last_digit)
                counts.append(last_count)
                last_digit = s[i]
                last_count = 1
                
        digits.append(last_digit)
        counts.append(last_count)
        
        ret = ""
        
        for i in range(len(digits)):
            ret = ret + str(counts[i]) + str(digits[i])
        
        return ret
    
    
if __name__ == "__main__":
    sol = Solution()
    
    n = int(input("Input n: "))
    
    print ("countAndSay(%d) = %s" %(n, sol.countAndSay(n)))