class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        stack = []
        
        stack.append(s[0])
        for i in range(1, len(s)):
            if stack and stack[-1] != s[i] and stack[-1].upper() == s[i]:
                stack.pop()
            elif stack and stack[-1] != s[i] and stack[-1].lower() == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        
        return "".join(stack)