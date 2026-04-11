class Solution:
    def rob(self, nums: list[int]) -> int:
        prev, curr = 0, 0
        
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        
        return curr

        