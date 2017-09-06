class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """        
        ret = ""
                
        while (n != 0):
            n -= 1    
            ret = chr(ord('A') + n % 26) + ret
            n = int (n / 26)
            
        return ret
    
    
if __name__ == "__main__":
    sol = Solution()
    n = int(input("Input column number: "))
    
    print ("Its column title is", sol.convertToTitle(n))