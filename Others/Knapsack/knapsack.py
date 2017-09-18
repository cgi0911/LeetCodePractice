# The classic Knapsack problem
# Given n items, for each item there is an associated weight (uint) and a value (uint).
# Each item is either selected (denoted by 1) or not selected (denoted by 0).
#
# Now, select among the n items, such that the total value of the selected items
# is maximized, subject to the constraint of knapsack capacity - total weight of the
# selected items is less than or equal to a constant W.

import random

class Solution(object):
    def __init__(self):
        self.subprobs = {}  # Store the result of subproblems

    
    def _knapSack(self, val, wt, n, cap):
        """
        :type val: List(int)
        :type wt: List(int)
        :type cap: int
        :rtype: int
        """
        # Given values and weights of n items, select among these items
        # such that their total value is maximized, while total weight
        # does not exceed cap. Return the total value.
        
        # Solution:
        # This is a classic dynamic programming problem.
        # 
        # For item i, we can either select it or not.
        #
        # Consider the 'selected' case, then its optimal total value is
        # wt[i] + knapsack(items[0..i-1], cap - wt[i])
        # 
        # Consider the 'not selected' case, then its optimal total value is
        # knapsack(items[0..i-1], cap)
        #
        # So knapsack(items[0..i-1], cap) =
        #    max(wt[i] + knapsack(items[0..i-1], cap - wt[i]),
        #        knapsack(items[0..i-1], cap))
        #
        # Each subproblem is identified by two state variables, # of items, i,
        # and capacity limit, c.
        
        if ((n, cap) in self.subprobs):
            return self.subprobs[(n, cap)]
        
        if (n == 0):
            return 0
        
        if (cap < 0):
            return 0
        
        if (n == 1):
            if (wt[0] < cap):
                return wt[0]
            else:
                return 0
        
        res = max(self._knapSack(val, wt, n-1, cap-wt[n]) + val[n],
                  self._knapSack(val, wt, n-1, cap) )

        self.subprobs[(n, cap)] = res
        return res
    
    
    def knapSack(self, val, wt, cap):
        """
        :type val: List(int)
        :type wt: List(int)
        :type cap: int
        :rtype: int
        """
        n = len(val)
        
        return self._knapSack(val, wt, n, cap)
        