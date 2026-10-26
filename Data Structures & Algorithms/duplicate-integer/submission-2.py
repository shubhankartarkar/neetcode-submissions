class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found_elements = set()

        for i in range(len(nums)):
            if nums[i] in found_elements:
                return True
            found_elements.add(nums[i])
        return False