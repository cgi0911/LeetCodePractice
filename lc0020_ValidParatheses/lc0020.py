class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []    # Empty list as stack
        match = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if (c == '(' or c == '[' or c == '{'):
                stk.append(c)
            elif (c == ')' or c == ']' or c == '}'):
                if (len(stk) == 0):
                    return False    # Nothing in stack to match
                elif (stk.pop() != match[c]):
                    return False

        if (len(stk) > 0):
            return False    # Still unmatched parentheses in stack
        else:
            return True


if __name__ == "__main__":
    sol = Solution()
    s = "()[{}]"
    print (sol.isValid(s))