class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return (''.join(sorted(s)) == ''.join(sorted(t)))
    
    
if __name__ == "__main__":
    sol = Solution()
    
    s = "rat"
    t = "car"
    
    print ("%s and %s are anagrams? %s" %(s, t, str(sol.isAnagram(s, t))))