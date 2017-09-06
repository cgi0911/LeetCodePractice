class Solution(object):
    def _searchSqrt(self, x, l, r):
        """
        :type x: int
        :type st: int
        :type ed: int
        :rtype: int
        """
        if (l == r): return l
        
        m = int((l + r + 1) / 2)    # ceil((l+r)/2)
                
        if (m * m > x):
            return self._searchSqrt(x, l, m - 1)
        if (m * m <= x):
            return self._searchSqrt(x, m, r)
        
        
    
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x < 0):
            return -1
        
        if (x == 0 or x == 1):
            return x
        
        return self._searchSqrt(x, 1, x)
    
    
if __name__ == "__main__":
    sol = Solution()
    
    x = int(input("Input x: "))
    
    print ("int(sqrt(x)) =", sol.mySqrt(x))