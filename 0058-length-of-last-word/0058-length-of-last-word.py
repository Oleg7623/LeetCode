class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        last_word = words[-1]
        return len(last_word)
