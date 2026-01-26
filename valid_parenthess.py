class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        for char in s:
            if char in chars.keys():
                stack.append(char)
            elif char in chars:
