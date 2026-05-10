class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for n in s:
            if n in '([{':
                stack.append(n)
            else:
                if not stack or stack[-1]!=mp[n]:
                    return False
                stack.pop()
        return len(stack)==0