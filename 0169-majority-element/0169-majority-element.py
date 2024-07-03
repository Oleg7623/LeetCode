class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_list = {}
        for num in nums:
            if num in count_list:
                count_list[num] += 1
            else:
                count_list[num] = 1
        for num in count_list:
            if count_list[num] > len(nums) / 2:
                return num