class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing bracket -> matching opening bracket
        match = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for ch in s:
            # If it is an opening bracket, push to stack
            if ch in "([{":
                stack.append(ch)
            else:
                # ch is a closing bracket, stack must not be empty
                if not stack:
                    return False
                # Top of stack must be the matching opening bracket
                if stack[-1] != match[ch]:
                    return False
                # Matched, so pop it
                stack.pop()

        # At the end, stack must be empty (no unclosed brackets)
        return len(stack) == 0
