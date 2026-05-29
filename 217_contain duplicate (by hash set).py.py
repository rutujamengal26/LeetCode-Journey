class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()  # This is your empty memory box
        
        for num in nums:
            if num in seen:  # Instantly checks if we've seen this before
                return True
            seen.add(num)    # Otherwise, remember this number
            
        return False