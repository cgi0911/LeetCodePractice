class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self._removeInvalidParentheses(s, lp, rp, remove_list, -1, res)
        
        return res
    
    
if __name__ == "__main__":
    sol = Solution()
    
    #s = "()())()"
    s = "())())()("
    print ("Original string:", s)
    res = sol.removeInvalidParentheses(s)
    print ("Strings resulting from removal of invalid parentheses:", str(res))
    
        