class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_word = str(x)
        length = len(original_word)

        for i in range(length // 2):
            if original_word[i] != original_word[length - 1 - i]:
                return False
        return True
