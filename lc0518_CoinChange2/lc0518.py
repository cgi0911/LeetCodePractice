class Solution(object):
    def __init__(self):
        self.subprobs = {}  # Key: two-tuple (amount, max_coin) -> Value: Number of combinations
    
    def _change(self, amount, coins, last_coin):
        # coins must be pre-sorted in ascending order
        if (amount == 0):
            return 1
        
        if ((amount, last_coin) in self.subprobs):
            return (self.subprobs[(amount, last_coin)])
        
        ret = 0
        
        for j in coins:
            if (j > last_coin):  break
            if (amount - j >= 0):
                ret += self._change(amount-j, coins, j)
        
        self.subprobs[(amount, last_coin)] = ret
        return ret
                    
        
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """        
        if (amount == 0):
            return 1
        
        if (len(coins) == 0):
            return 0
        
        # Again this is a classic DP problem
        coins = sorted(coins)
        return (self._change(amount, coins, coins[-1]))
    

if __name__ == "__main__":
    sol = Solution()
    
    coins = [1, 2, 5]
    amount = 10
    
    print ("Available coins:", str(coins))
    print ("# of combinations that sum up to %d = %d" %(amount, sol.change(amount, coins)))
