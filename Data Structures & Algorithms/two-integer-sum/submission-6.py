class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            n = target - v
            if n in seen:
                return [seen[n], i]
            seen[v] = i