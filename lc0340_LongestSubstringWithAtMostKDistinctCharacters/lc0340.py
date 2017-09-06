class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if (k == 0):
            return 0
        
        max_len = 0
        st = 0
        last_occur = {}
        
        for i in range(len(s)):
            c = s[i]    # The new char to be included
            
            if (c in last_occur):
                last_occur[c] = i   # New char is already in the map
                
            else:
                if (len(last_occur) < k):
                    last_occur[c] = i   # Less than k unique chars. Simply include the new char
                else:
                    uniq = list(last_occur.keys ())
                    to_del = ''
                    min_last_occur = len(s) + 1
                    # To determine which old unique char to be excluded
                    for q in uniq:
                        if (last_occur[q] < min_last_occur):
                            to_del = q
                            min_last_occur = last_occur[q]
                    
                    st = min_last_occur + 1
                    del last_occur[to_del]  # Remove the old char from map
                    last_occur[c] = i       # Include the new char in map
            
            max_len = max(max_len, i - st + 1)  # Update max_len if needed
        
        return max_len
    
        
if __name__ == "__main__":
    sol = Solution()
    s = input("Input your string: ")
    
    print (sol.lengthOfLongestSubstringKDistinct(s, 3))
    