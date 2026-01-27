class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in pairs.values():      # opening bracket
                stack.append(ch)
            else:                         # closing bracket
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return not stack
