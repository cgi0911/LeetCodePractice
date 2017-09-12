class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        
        if (n == 0):
            return 0
        
        imin_r = [costs[0][0]]
        imin_b = [costs[0][1]]
        imin_g = [costs[0][2]]
        
        for i in range(1, n):
            min_r = costs[i][0] + min(imin_b[-1], imin_g[-1])
            min_b = costs[i][1] + min(imin_r[-1], imin_g[-1])
            min_g = costs[i][2] + min(imin_r[-1], imin_b[-1])
            imin_r.append(min_r)
            imin_b.append(min_b)
            imin_g.append(min_g)
            
        print (imin_r)
        print (imin_b)
        print (imin_g)
        return min(imin_r[-1], min(imin_b[-1], imin_g[-1]))
        
        
if __name__ == "__main__":
    sol = Solution()
    
    costs = [[17,2,17],[16,16,5],[14,3,19]]
    
    print (sol.minCost(costs))