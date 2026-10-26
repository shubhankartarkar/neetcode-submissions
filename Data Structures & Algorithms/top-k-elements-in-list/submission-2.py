class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        freq = [[] for i in range(len(nums) + 1)]
    
        for num in nums:
            if num in numMap:
                numMap[num] = numMap.get(num,1) + 1
            else:
                numMap[num] = 1
    
    
        for key, value in numMap.items():
            freq[value].append(key)
            
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k: 
                    return res
            