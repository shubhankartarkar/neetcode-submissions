class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}

        if len(s) != len(t):
            return False
        
        for word in s:
            if word in sMap:
                sMap[word] = sMap.get(word,1) + 1
            else:
                sMap[word] = 1

        for word in t:
            if word in tMap:
                tMap[word] = tMap.get(word,1) + 1
            else:
                tMap[word] = 1
        
        return sMap == tMap
        