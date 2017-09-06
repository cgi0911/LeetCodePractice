# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def searchFirstBadVersion(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        if (l == r):
            return l
        
        m = int((l + r) / 2)        
        
        if (isBadVersion(m)):
            return self.searchFirstBadVersion(l, m)     # We got a one at midpoint. Include it and search the left half
        else:
            return self.searchFirstBadVersion(m+1, r)   # We got a zero at midpoint. Exclude it and search the right half
    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (not isBadVersion(n)):
            return -1   # No bad version at all, if last version is good
        
        f = self.searchFirstBadVersion(1, n)
        
        if (isBadVersion(f)):
            return f
        else:
            return -1   # This should not happen, but for sanity.