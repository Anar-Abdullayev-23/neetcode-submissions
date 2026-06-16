class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        r = -1
        for i in range(len(nums2)):
            nums1[r] = nums2[i]
            r -= 1
        nums1.sort()        