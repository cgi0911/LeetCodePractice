import pprint

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
                
                
if __name__ == "__main__":
    sol = Solution()
    pp = pprint.PrettyPrinter(indent=2)
    
    board = [
             ['A','B','C','E'],
             ['S','F','C','S'],
             ['A','D','E','E']
            ]
    word = "ABCB"
    
    print ("Board:")
    pp.pprint(board)
    print ("Word:", word)
    print ("Word can be found in board?", str(sol.exist(board, word)))