class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        k = 0
        for i in nums:
            if i not in result:
                result.append(i)
                nums[k] = i 
                k += 1
        return k
