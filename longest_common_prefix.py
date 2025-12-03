class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        min_word = min(strs)
        max_word = max(strs)

        i = 0
        while i < len(min_word) and i < len(max_word) and min_word[i] == max_word[i]:
            i += 1
        return min_word[:i]