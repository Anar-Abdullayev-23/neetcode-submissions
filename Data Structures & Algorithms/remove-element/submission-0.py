class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        expectedNums = []

        for i in nums:
            if i != val:
                expectedNums.append(i)

        for j in range(len(expectedNums)):
            nums[j] = expectedNums[j]

        return len(expectedNums)