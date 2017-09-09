import sys
import time
import random

class Solution(object):
    def __init__(self, dp=True):
        """
        dp means using dynamic programming
        """
        self.dpMap = {}     # Memorization map for dynamic programming
                            # Key is (x, y) and value is # of paths to (n, m)
        self.dp = dp
        
    
    def _countPaths(self, cells, n, m, x, y):
        """
        Given a labyrinth with dimensions n by m, with some cells blocked out,
        count the number of shortest paths from (x, y) to (n - 1, m - 1).
        Note: The dimensions n is # of rows, and m is # of columns.
        If (x, y) is a blocked-out cell, we shall return 0.
        :type cells: List(List(bool))
        :type n: int
        :type m: int
        :type x: int
        :type y: int
        """
        
        if (self.dp):
            if ((x, y) in self.dpMap):  return self.dpMap[(x, y)]
        if (cells[x][y] == True):   return 0
        if (x == n - 1 and y == m - 1):     return 1
        
        
        k = 0
        if (x + 1 < n):     k += self._countPaths(cells, n, m, x + 1, y)
        if (y + 1 < m):     k += self._countPaths(cells, n, m, x, y + 1)

        if (self.dp):
            self.dpMap[(x, y)] = k  # Memorization for dynamic programming
        return k
        
        
    def countPaths(self, cells, n, m):
        """
        Given a labyrinth with dimensions n by m, with some cells blocked out,
        count the number of shortest paths from (0, 0) to (n - 1, m - 1).
        Note:
        - The dimensions n is # of rows, and m is # of columns.
        - (0, 0) is at the top left corner of the labyrinth.
        - For each cell, False denotes valid cells, while True is blocked-out.
        :type cells: List(List(bool))
        :type n: int
        :type m: int
        """ 
        return self._countPaths(cells, n, m, 0, 0)
        
        
if __name__ == "__main__":
    random.seed(time.time())
    
    sol1 = Solution(dp = True)
    sol2 = Solution(dp = False)
    
    n = int(input("Input n: "))
    m = int(input("Input m: "))
    b = int(input("Input # of blocked-out cells: "))
    
    if (b > n * m - 2):
        print ("Invalid parameters!")
        sys.exit(1)
    
    # Initialize the cell labyrinth with all False
    cells = [[False] * m for i in range(n)]
    
    # Build a population list (all cells except (0, 0) and (n - 1, m - 1))
    # for randomly sample b blocked cells.
    population = []
    for i in range(n):
        for j in range(m):
            if ((i, j) == (0, 0) or (i, j) == (n - 1, m - 1)):  continue
            else:   population.append((i, j))
    
    # Select and mark blocked cells
    blocked = random.sample(population, b)  
    for blk in blocked:
        x, y = blk
        cells[x][y] = True
        
    # Print the labyrinth
    print ("The labyrinth:")
    for i in range(n):
        for j in range(m):
            print ("%d " %(cells[i][j]), end='')
        print ("")
    
    # Solve the problem with DP
    st = time.time()
    n_paths1 = sol1.countPaths(cells, n, m)
    t1 = time.time() - st
    print ("There are %d shortest paths between (0, 0) and (%d, %d)"
           %(n_paths1, n - 1, m - 1))
    print ("Time elapsed with DP: %f" %(t1))
    
    # Solve the problem without DP
    st = time.time()
    n_paths2 = sol2.countPaths(cells, n, m)
    t2 = time.time() - st    
    print ("There are %d shortest paths between (0, 0) and (%d, %d)"
           %(n_paths2, n - 1, m - 1))
    print ("Time elapsed without DP: %f" %(t2))
