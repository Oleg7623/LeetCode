class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remain, combination, start):
            if remain == 0:
                result.append(list(combination))
                return 
            if remain  < 0:
                return 
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(remain - candidates[i], combination, i)
                combination.pop()
        result = []
        backtrack(target, [], 0)
        return result
