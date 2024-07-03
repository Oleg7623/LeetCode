class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_of_unique = set()
        for num in nums:
            if num in set_of_unique:
                return True
            else:
                set_of_unique.add(num)
        return False