class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if (n == 0):
            return 1
        
        if (n == 1):
            return x
        
        if (n < 0):
            return 1.0 / self.myPow(x, -n)
        
        temp = self.myPow(x, int(n / 2))
        return (temp * temp * self.myPow(x, n % 2))
    

if __name__ == "__main__":
    sol = Solution()
    
    x = float(input("Input a floating number: "))
    n = int(input("Input an integer: "))
    
    print ("pow(%f, %d) = %f" %(x, n, sol.myPow(x, n)))