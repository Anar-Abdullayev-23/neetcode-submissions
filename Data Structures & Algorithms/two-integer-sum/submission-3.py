class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            n = target - v
            if n in nums:
                j = nums.index(n)
                if i != j:
                    return [j, i]