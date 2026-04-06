class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {']': '[', ')': '(', '}': '{'}

        for i in s:
            if i in map.values():
                stack.append(i)
            else:
                if not stack or stack[-1] != map[i]:
                    return False
                stack.pop()

        return len(stack) == 0