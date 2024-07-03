class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        for num, count in count_dict.items():
            if count == 1:
                return num
