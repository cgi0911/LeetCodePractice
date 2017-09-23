class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (s == ""):   return 0    # Corner case
        
        n = len(s)
        res_list = [0 for i in range(n+1)]  # Dictionary for storing results
                                            # Key is index, and value is # of decoding ways of s[key:]
        res_list[n] = 1        
        
        for i in range(n-1, -1, -1):            
            if (s[i] == '0'):
                continue
                        
            res_list[i] += res_list[i+1]
            
            if (i < n - 1 and 1 <= int(s[i:i+2]) <= 26):
                res_list[i] += res_list[i+2]
        
        return res_list[0]
            
        
if __name__ == "__main__":
    sol = Solution()
    
    s = "123"
    print ("Original encoding:", s)
    print ("# of decoding ways =", sol.numDecodings(s))
    