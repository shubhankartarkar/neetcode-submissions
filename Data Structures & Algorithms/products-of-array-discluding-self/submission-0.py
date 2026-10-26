class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
    
        for idx, i in enumerate(nums):
            product = 1
            for idx2 ,  j in enumerate(nums):
                if idx2 != idx:
                    product = j * product
            output.append(product)
        return output
            