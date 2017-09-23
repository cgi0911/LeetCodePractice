import pprint

class Solution(object):
    def _exist(self, board, word, start, used):
        """
        :type board: List[List[]]
        :type word: str
        :type start: (int, int)
        :type used: set((int, int))
        """
        n, m = len(board), len(board[0])
        x, y = start[0], start[1]
        
        if (start in used):
            return False    # Reached a traversed cell
        
        if (x >= n or x < 0 or y >= m or y < 0):
            return False    # Out of bound
        
        if (word[0] != board[x][y]):
            return False    # Failed match
        
        if (len(word) == 1):
            return True     # Last match
        
        ret = False
        used.add(start)
        if   (self._exist(board, word[1:], (x+1, y), used)):  ret = True
        elif (self._exist(board, word[1:], (x-1, y), used)):  ret = True
        elif (self._exist(board, word[1:], (x, y+1), used)):  ret = True
        elif (self._exist(board, word[1:], (x, y-1), used)):  ret = True
        used.remove(start)
        return ret
        
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n, m = len(board), len(board[0])
        
        if (n == 0 or m == 0):
            return False
        
        for i in range(n):
            for j in range(m):
                used = set()    # To record traversed cells
                # Return true if any search is true
                if self._exist(board, word, (i, j), used): return True
                
        return False
                
                
if __name__ == "__main__":
    sol = Solution()
    pp = pprint.PrettyPrinter(indent=2)
    
    board = [
             ['A','B','C','E'],
             ['S','F','C','S'],
             ['A','D','E','E']
            ]
    word = "ABFK"
    
    print ("Board:")
    pp.pprint(board)
    print ("Word:", word)
    print ("Word can be found in board?", str(sol.exist(board, word)))