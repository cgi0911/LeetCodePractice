class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0         # To memorize max NRC substring length
        last_occur = {}
        st = 0              # Start of current NRC substring

        for i in range(len(s)):
            c = s[i]

            if (not c in last_occur):
                last_occur[c] = i

            elif (c in last_occur):
                if (last_occur[c] < st):
                    last_occur[c] = i
                else:
                    st = last_occur[c] + 1
                    last_occur[c] = i

            max_len = max(max_len, i - st + 1)

        return max_len


if __name__ == "__main__":
    sol = Solution()
    s = raw_input("Input your string: ")

    print (sol.lengthOfLongestSubstring(s))