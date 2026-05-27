# Problem: LeetCode 26 - Remove Duplicates from Sorted Array
# Pattern: Two-Pointer (Fast & Slow / Same Direction)
# Time Complexity: O(n)
# Space Complexity: O(1) In-place

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        slow = 0
        
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                
        return slow + 1