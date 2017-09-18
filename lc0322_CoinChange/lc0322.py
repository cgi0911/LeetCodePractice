class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # This is also a classic dynamic programming problem with optimal substructure.
        # Here we use tabulation (bottom-up) approach.
        
        # Boundary conditions        
        if (amount == 0):
            return 0
        
        # Tabulation of initial cases
        subprobs = {}   # A dict storing subproblem results, where the key is the amount and
                        # value is coinChange result
        for c in coins:
            subprobs[c] = 1     # Single coin cases
        
        # Start DP
        for i in range(1, amount+1):
            if (i in subprobs): continue
                
            n_coins = float("inf")
            for c in coins:
                # Scan through the cases that "last coin" is c, obviously, when the
                # last coin is c, the minimum number of coins needed would be
                # coinChange(coins, i-c) + 1
                # Then we compare over all cases to choose the minimum
                if ((i - c) in subprobs):
                    n_coins = min(n_coins, subprobs[i-c] + 1)
                    
            if (n_coins != float("inf")):
                subprobs[i] = n_coins   # At the end of iteration, record the subproblem's result if available
            
        
        # Finally return the result. Return 0 if unavailable.
        if (amount in subprobs):
            return subprobs[amount]        
        else:
            return -1

if __name__ == "__main__":
    sol = Solution()
    
    coins = [2, 5, 10]
    amount = 8
    
    print ("Available coins:", str(coins))
    print ("Min # of coins needed to sum up to %d = %d" %(amount, sol.coinChange(coins, amount)))