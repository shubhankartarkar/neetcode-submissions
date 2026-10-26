class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict, tDict = {}, {}

        for word in s:
            if word in sDict:
                sDict[word] = sDict.get(word,1) + 1
            else:
                sDict[word] = 1
        
        for word in t:
            if word in tDict:
                tDict[word] = tDict.get(word,1) + 1
            else:
                tDict[word] = 1
                    
        return sDict == tDict
        
        