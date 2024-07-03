class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in my_dict:
                return [index, my_dict[diff]]
            my_dict[num] = index
