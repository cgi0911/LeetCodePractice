class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        st = 0
        last_occur = {}
        
        for i in range(len(s)):
            c = s[i]    # The new char to be included
            
            if (c in last_occur):
                last_occur[c] = i   # New char is already in the map
                
            else:
                if (len(last_occur) < 2):
                    last_occur[c] = i   # Less than 2 unique chars. Simply include the new char
                else:
                    uniq = list(last_occur.keys ())
                    to_del = ''
                    # To determine which old unique char to be excluded
                    if (last_occur[uniq[0]] < last_occur[uniq[1]]):
                        to_del = uniq[0]
                        st = last_occur[uniq[0]] + 1    # Update st to exclude the old char
                    else:
                        to_del = uniq[1]
                        st = last_occur[uniq[1]] + 1
                    del last_occur[to_del]  # Remove the old char from map
                    last_occur[c] = i       # Include the new char in map
            
            max_len = max(max_len, i - st + 1)  # Update max_len if needed
        
        return max_len
    
        
if __name__ == "__main__":
    sol = Solution()
    s = input("Input your string: ")
    
    print (sol.lengthOfLongestSubstringTwoDistinct(s))
    