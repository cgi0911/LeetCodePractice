# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        k = 0
        
        while (n > 0):
            x = read4(buf)
            xx = min(x, n)
            k += xx
            n -= xx
            if (x < 4):
                break
        
        return k