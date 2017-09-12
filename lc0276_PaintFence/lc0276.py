class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # We iterate over the sequence of posts, starting from i = 2
        # For each i >= 2, there are two cases:
        #     Case 1: posts[i-1], posts[i-2] are of different colors
        #     Case 2: posts[i-1], posts[i-2] are of the same color
        # We store the possible ways of case1 and case2 in variables
        # ways_diff, ways_same, respectively
        #
        # Now we choose the color for posts[i]
        #     Given case 1, if we choose the same color as posts[i-1],
        #     variable ways_same becomes previous value of ways_diff.
        #     Given case 1, if we choose a different color from posts[i-1],
        #     we have (k-1) choices.
        #     Given case 2, we have no choice but choose a different color
        #     from posts[i-1], from which we have (k-1) choices.
        #     So ways_diff = (k-1) * previous value of (ways_same + ways_diff)
        
        if (n == 0):
            return 0
        if (n == 1):
            return k
        if (n == 2):
            return k * k
        
        ways_diff = k * (k - 1)
        ways_same = k
        
        for i in range(2, n):
            temp = ways_diff
            ways_diff = (k - 1) * (ways_same + ways_diff)
            ways_same = temp
            
        return (ways_same + ways_diff)