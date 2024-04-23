class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n  # to handle cases where k is larger than the length of nums
        nums[:] = nums[-k:] + nums[:-k]  # rotate the array in-place

solution = Solution()

nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
solution.rotate(nums1, k1)
print("Example 1 Output:", nums1)
