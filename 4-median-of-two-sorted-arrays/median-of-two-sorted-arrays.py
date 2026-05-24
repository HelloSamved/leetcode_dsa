class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = nums1 + nums2
        merged_array.sort()

        n = len(merged_array)

        if n % 2 == 0:
            i1 = (n // 2) - 1
            i2 = n // 2
            median = (merged_array[i1] + merged_array[i2]) / 2
        else:
            median = merged_array[n // 2]

        return median