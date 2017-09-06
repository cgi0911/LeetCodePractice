class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, m = len(haystack), len(needle)
        ret = -1
        
        if (n < m):
            return ret   # Invalid cases
        
        for i in range(0, n - m + 1):
            is_match = True
            
            for j in range(0, m):
                if (haystack[i+j] != needle[j]):
                    is_match = False
                    break
                    
            if (is_match):
                return i
            
        return ret
                    