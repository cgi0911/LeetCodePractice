class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        
        bulbs = [False] * n
        
        for i in range(1, n + 1):
            k = i - 1
            while (k <= n - 1):
                bulbs[k] = not bulbs[k]
                k += i
        
        count = 0
        for b in bulbs:
            if b:
                count += 1
                
        return count
    

if __name__ == "__main__":
    sol = Solution()
    print (999999, sol.bulbSwitch(999999))
    