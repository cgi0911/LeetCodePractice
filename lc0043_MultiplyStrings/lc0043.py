#!/usr/bin/env python3

class Solution(object):
    def toDigit(self, digitStr):
        """
        :type digitStr: str
        :rtype: int
        """
        # We assume that digit is single character [0-9]
        return ord(digitStr[0]) - ord('0')
        
        
    def shiftLeft(self, num1, k):
        """
        :type digitStr: str
        :rtype: int
        """
        # First check if num1 is all-zero        
        isZero = True
        for i in range(len(num1)):
            if num1[i] != "0":  isZero = False
                
        if (isZero):
            return "0"
        else:
            return num1 + "0" * k 
        
    
    def add(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # We assume that both num1 and num2 are valid strings of integers and no leading zeros
        ret = ""
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        
        carry = 0
        while (p1 >= 0 or p2 >= 0):
            sumcarry = carry
            
            if (p1 >= 0):
                sumcarry += self.toDigit(num1[p1])
                p1 -= 1
            if (p2 >= 0):
                sumcarry += self.toDigit(num2[p2])
                p2 -= 1
    
            sum = sumcarry % 10
            carry = int(sumcarry / 10)
            ret = str(sum) + ret
            
        if (carry > 0):
            ret = str(carry) + ret
        
        return ret
    
    
    def multiplyOneDigit(self, num1, digitStr):
        """
        :type num1: str
        :type digitStr: str
        :rtype: str
        """
        # We assume that digit is single character [0-9], and num1 is a valid string of integer
        if (digitStr == "0"):
            return "0"
        
        if (digitStr == "1"):
            return num1
        
        ret = ""
        carry = 0
        digit = self.toDigit(digitStr)
        
        for i in range(len(num1) - 1, -1, -1):
            sumcarry = carry
            digit1 = self.toDigit(num1[i])
            sumcarry += digit1 * digit
            sum = sumcarry % 10
            carry = int(sumcarry / 10)
            ret = str(sum) + ret
            
        if (carry > 0):
            ret = str(carry) + ret
            
        return ret        
        
        
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """        
        ret = "0"
        
        if (num1 == "" or num2 == ""):
            return ""
        
        if (num1 == "0" or num2 == "0"):
            return "0"
        
        for i in range(len(num2) - 1, -1, -1):
            partial = self.multiplyOneDigit(num1, num2[i])
            partial = self.shiftLeft(partial, len(num2) - 1 - i)
            ret = self.add(partial, ret)
            
        return ret
    

if __name__ == "__main__":
    sol = Solution()
    
    num1 = input("Input num1: ")
    num2 = input("Input num2: ")
    
    print ("%s * %s = %s" %(num1, num2, sol.multiply(num1, num2)))
        