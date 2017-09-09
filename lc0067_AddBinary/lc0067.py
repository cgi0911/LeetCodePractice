class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        pa, pb = len(a) - 1, len(b) - 1
        ret = ""
        
        carry = 0
        while (pa >= 0 or pb >= 0):
            sumcarry = carry
            
            if (pa >= 0):
                sumcarry += int(a[pa])
                pa -= 1
            
            if (pb >= 0):
                sumcarry += int(b[pb])
                pb -= 1
                
            sum = sumcarry % 2
            carry = int(sumcarry / 2)
            
            ret = str(sum) + ret
            
        if (carry > 0):
            ret = str(carry) + ret
            
        return ret

    
if __name__ == "__main__":
    sol = Solution()
    a = "11"
    b = "1"
    
    print (a, "+", b, "=")
    print (sol.addBinary(a, b))