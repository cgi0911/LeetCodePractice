class Solution(object):
    def _numDecodings(self, s):
        """
        :type s:str
        :rtype: int
        """
        if (s == ""):       return 1    # Reach end of string
        if (s[0] == "0"):   return 0    # No way to decode
        
        ways = 0
        
        if (int(s[0]) != 0):
            ways += self._numDecodings(s[1:])
            
        if (len(s) >= 2 and 1 <= int(s[0:2]) <= 26):
            ways += self._numDecodings(s[2:])
            
        return ways
        
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (s == ""):   return 0    # Corner case
        
        return self._numDecodings(s)
    
    
if __name__ == "__main__":
    sol = Solution()
    
    s = "000"
    print ("Original encoding:", s)
    print ("# of decoding ways =", sol.numDecodings(s))
    