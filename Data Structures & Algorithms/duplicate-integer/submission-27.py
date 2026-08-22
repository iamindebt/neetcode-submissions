class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        for n in nums:
            numbers.add(n)
        if len(numbers) != len(nums):
            return True
        else:
            return False