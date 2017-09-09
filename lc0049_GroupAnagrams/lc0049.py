class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        myMap = {}  # Map for grouping anagrams
        
        for s in strs:
            k = ''.join(sorted(s))  # k means 'key'
            
            if (k in myMap):
                myMap[k].append(s)
            else:
                myMap[k] = [s]
                
        ret = []
        
        for k in myMap.keys():
            ret.append(sorted(myMap[k]))        
        
        ret = sorted(ret, key=lambda x: x[0])
        
        return ret
    
    
if __name__ == "__main__":
    sol = Solution()
    
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    print ("Grouping anagrams for %s" %(str(strs)))
    
    res = sol.groupAnagrams(strs)
    
    print ("Result:")
    for a in res:
        print (a)