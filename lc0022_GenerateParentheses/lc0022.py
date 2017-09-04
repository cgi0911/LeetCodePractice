class Solution(object):
    def _generateParenthesis(self, res, l, r, partial):
        if (l == r == 0):
            res.append(partial)
            return

        if (l >= r):
            # Must put a left parenthesis
            self._generateParenthesis(res, l-1, r, partial + '(')
        else:
            if (l > 0):
                self._generateParenthesis(res, l-1, r, partial + '(')
            if (r > 0):
                self._generateParenthesis(res, l, r-1, partial + ')')


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self._generateParenthesis(res, n, n, "")
        return res


if __name__ == "__main__":
    sol = Solution()
    n = int(input("# of parenthesis pairs: "))

    res = sol.generateParenthesis(n)

    for s in res:
        print (s)