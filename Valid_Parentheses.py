class Solution:
    
    def isValid(self, s: str) -> bool:

        rightbrackets = ['(', '{', '[']

        leftbrackets = []

        s = list(s)

        for b in s:

            if b in rightbrackets:
                leftbrackets.append(b)
            elif b == ')' and len(leftbrackets) != 0 and leftbrackets[-1] == '(':
                leftbrackets.pop()
            elif b == '}' and len(leftbrackets) != 0 and leftbrackets[-1] == '{':
                leftbrackets.pop()
            elif b == ']' and len(leftbrackets) != 0 and leftbrackets[-1] == '[':
                leftbrackets.pop()
            else:
                return False
        
        return leftbrackets == []

obj = Solution()
obj.isValid("{}")
